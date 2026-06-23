#!/usr/bin/env python3
# Date: 2026-06-23
# Time: 20:40 UTC
# @see https://help.obsidian.md/Advanced+topics/YAML+shortcodes
# @see https://github.com/engram-memory/engram

"""
Extract structured knowledge from Markdown files for Engram indexing.
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from datetime import datetime

def extract_frontmatter(content):
    """
    Extract YAML frontmatter from markdown content.
    Date: 2026-06-23
    @see https://yaml.org/spec/
    """
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]), parts[2]
            except yaml.YAMLError:
                return None, content
    return None, content

def parse_knowledge(file_path):
    """
    Parse markdown file and extract structured knowledge.
    Date: 2026-06-23
    @see 00-INDEX.md
    """
    content = file_path.read_text(encoding='utf-8')
    meta, body = extract_frontmatter(content)
    
    if not meta:
        return None
    
    knowledge = {
        'source': str(file_path),
        'title': meta.get('title', file_path.stem),
        'type': meta.get('type', 'general'),
        'date': meta.get('date', datetime.now().isoformat()),
        'tags': meta.get('tags', []),
        'context': meta.get('context', ''),
        'decision': meta.get('decision', ''),
        'outcome': meta.get('outcome', ''),
        'links': re.findall(r'\[\[([^\]]+)\]\]', body)
    }
    return knowledge

def main():
    """
    Main entry point for knowledge extraction.
    Date: 2026-06-23
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default='.', help='Folder with .md files')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    
    source = Path(args.source)
    knowledges = []
    
    for md_file in source.rglob('*.md'):
        if md_file.name.startswith('00-INDEX') or '.git' in str(md_file):
            continue
        
        knowledge = parse_knowledge(md_file)
        if knowledge:
            knowledges.append(knowledge)
    
    print(f"Found {len(knowledges)} documents")
    
    if args.dry_run:
        for k in knowledges[:3]:
            print(f"\n--- {k['title']} ---\nTags: {k['tags']}")

if __name__ == '__main__':
    main()