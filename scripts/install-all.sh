#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Installing daily-development-spec ==="
echo ""

echo "[1/2] Installing to Cursor..."
bash "$SCRIPT_DIR/install-cursor.sh"
echo ""

echo "[2/2] Installing to Codex..."
bash "$SCRIPT_DIR/install-codex.sh"
echo ""

echo "=== Done ==="
echo ""
echo "For Claude Code:"
echo "  /plugin add extravert/daily-development-spec"
echo "  /plugin install daily-development-spec@latest"
