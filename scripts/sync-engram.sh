#!/bin/bash
# Date: 2026-06-23
# Time: 20:40 UTC
# @see https://github.com/engram-memory/engram
# @see extract-knowledge.py

# Sync knowledge to Engram
set -e

ENGGRAM_URL="${ENGRAM_URL:-http://localhost:8000}"
echo "🔄 Syncing knowledge to Engram ($ENGRAM_URL)..."

# Find and index all .md files
find . -name "*.md" -not -path "./.git/*" -not -path "./.engram/*" -not -name "00-INDEX.md" | while read file; do
    echo "📄 Indexing: $file"
done

echo "✅ Done. Run 'python scripts/extract-knowledge.py --source .' for full indexing"