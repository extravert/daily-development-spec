#!/usr/bin/env python3
"""
Export daily-development-spec progress files to structured JSON.

Parses MASTER.md and per-phase detail files from docs/progress/,
outputting a single JSON object suitable for import into external
project management tools (Linear, Jira, Notion, etc.).

Usage:
    python export-progress.py [docs/progress/]

If no path is given, defaults to docs/progress/ relative to cwd.
"""

import json
import re
import sys
from pathlib import Path


def parse_master(master_path: Path) -> dict:
    """Parse MASTER.md and extract project-level metadata."""
    text = master_path.read_text(encoding="utf-8")

    # Extract task name from title: "# <Task Name> -- Progress Tracker"
    title_match = re.search(r"^#\s+(.+?)\s*(?:--|-{1,3})\s*Progress Tracker", text, re.MULTILINE)
    task_name = title_match.group(1).strip() if title_match else "Unknown"

    # Extract dates from blockquote metadata
    started = _extract_field(text, "Started")
    last_updated = _extract_field(text, "Last Updated")

    # Extract phase checklist entries
    # Format: - [ ] Phase 1: <name> (0/N tasks) or - [x] Phase 1: <name> (N/N tasks)
    phase_pattern = re.compile(
        r"-\s+\[([xX ])\]\s+Phase\s+(\d+):\s+(.+?)\s+\((\d+)/(\d+)\s+tasks?\)",
        re.MULTILINE,
    )
    phases = []
    for m in phase_pattern.finditer(text):
        done_flag = m.group(1).strip().lower() == "x"
        phases.append({
            "id": int(m.group(2)),
            "name": m.group(3).strip(),
            "completed_tasks": int(m.group(4)),
            "total_tasks": int(m.group(5)),
            "done": done_flag,
        })

    return {
        "task": task_name,
        "started": started,
        "last_updated": last_updated,
        "phases": phases,
    }


def parse_phase_file(phase_path: Path) -> list[dict]:
    """Parse a phase detail file and extract individual tasks."""
    text = phase_path.read_text(encoding="utf-8")

    tasks = []
    # Split on task entries: - [ ] **Task N.M**: ...
    task_blocks = re.split(r"(?=^-\s+\[[xX ]\]\s+\*\*Task\s+)", text, flags=re.MULTILINE)

    for block in task_blocks:
        task_match = re.match(
            r"-\s+\[([xX ])\]\s+\*\*Task\s+([\d.]+)\*\*:\s+(.+)",
            block,
        )
        if not task_match:
            continue

        done = task_match.group(1).strip().lower() == "x"
        task_id = task_match.group(2).strip()
        title = task_match.group(3).strip()

        priority = _extract_field(block, "Priority")
        effort = _extract_field(block, "Effort")
        acceptance = _extract_field(block, "Acceptance")

        tasks.append({
            "id": task_id,
            "title": title,
            "done": done,
            "priority": priority,
            "effort": effort,
            "acceptance": acceptance,
        })

    return tasks


def _extract_field(text: str, field_name: str) -> str:
    """Extract a field value from '- Field: value' or '> **Field**: value' patterns."""
    patterns = [
        rf"[-*]\s+{field_name}:\s*(.+)",
        rf">\s+\**{field_name}\**:\s*(.+)",
    ]
    for pattern in patterns:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            value = m.group(1).strip()
            if value and value != "_none yet_":
                return value
    return ""


def export_progress(progress_dir: Path) -> dict:
    """Build the complete export structure from a progress directory."""
    master_path = progress_dir / "MASTER.md"
    if not master_path.exists():
        print(f"Error: {master_path} not found.", file=sys.stderr)
        sys.exit(1)

    result = parse_master(master_path)

    # Enrich each phase with task details from its dedicated file
    for phase in result["phases"]:
        phase_id = phase["id"]
        # Find matching phase file: phase-N-<name>.md
        candidates = list(progress_dir.glob(f"phase-{phase_id}-*.md"))
        if candidates:
            phase["tasks"] = parse_phase_file(candidates[0])
        else:
            phase["tasks"] = []

    # Compute summary
    total_tasks = sum(p["total_tasks"] for p in result["phases"])
    completed_tasks = sum(p["completed_tasks"] for p in result["phases"])
    result["summary"] = {
        "total_phases": len(result["phases"]),
        "completed_phases": sum(1 for p in result["phases"] if p["done"]),
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress_percent": round(completed_tasks / total_tasks * 100, 1) if total_tasks > 0 else 0,
    }

    return result


def main():
    if len(sys.argv) > 1:
        progress_dir = Path(sys.argv[1])
    else:
        progress_dir = Path("docs/progress")

    if not progress_dir.is_dir():
        print(f"Error: directory {progress_dir} does not exist.", file=sys.stderr)
        sys.exit(1)

    result = export_progress(progress_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
