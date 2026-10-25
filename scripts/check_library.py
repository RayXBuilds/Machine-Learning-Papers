#!/usr/bin/env python3
"""Validate historical blobs and local Markdown links; no network required."""
import argparse
import json
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tree-json', type=Path, help='Validate a proposed path-to-Git-entry JSON tree')
    args = parser.parse_args()
    if args.tree_json:
        tree = json.loads(args.tree_json.read_text())
    else:
        tree = {}
        for entry in git('ls-tree', '-rz', 'HEAD').split(b'\0'):
            if not entry:
                continue
            meta, path = entry.split(b'\t', 1)
            mode, kind, sha = meta.decode().split()
            tree[path.decode()] = dict(mode=mode, type=kind, sha=sha)
        # Include unstaged/untracked text edits for normal contribution checks.
        for folder in ('docs', 'papers', 'library'):
            for path in (ROOT / folder).rglob('*.md'):
                tree.setdefault(path.relative_to(ROOT).as_posix(), {})
    def read(path):
        file = ROOT / path
        if file.is_file():
            return file.read_text()
        return git('show', 'HEAD:' + path).decode()
    errors = []
    manifest = json.loads(read('docs/migration-2026-10-26.json'))
    records = manifest['files']
    if len(records) != manifest['pdf_count'] or len({r['new_path'] for r in records}) != len(records):
        errors.append('Migration count mismatch or duplicate destination')
    for record in records:
        path = record['new_path']
        if tree.get(path, {}).get('sha') != record['git_blob_sha']:
            errors.append('Historical PDF missing/changed in Git tree: ' + path)
        if record['old_path'] in tree:
            errors.append('Old PDF path still tracked: ' + record['old_path'])
        # A full checkout may contain uncommitted binary changes.
        local = ROOT / path
        if local.is_file():
            actual = git('hash-object', '--', path).decode().strip()
            if actual != record['git_blob_sha']:
                errors.append('Historical PDF changed in working tree: ' + path)
    texts = {path: read(path) for path in tree if path.endswith('.md')}
    def anchors(text):
        result = set(re.findall(r'<a\s+id="([^"]+)"', text))
        seen = {}
        for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
            heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading)
            slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            result.add(slug + ('-' + str(count) if count else ''))
        return result
    anchor_map = {path: anchors(text) for path, text in texts.items()}
    checked = 0
    for path, text in texts.items():
        # Examples in fenced code blocks are not live links.
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for href in re.findall(r'\]\(([^)\n]+)\)', text):
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(parsed.path))) if parsed.path else path
            if target not in tree:
                if target + '/README.md' in tree:
                    target += '/README.md'
                else:
                    errors.append(f'{path}: missing link target {href}')
                    continue
            if parsed.fragment and target in anchor_map and unquote(parsed.fragment) not in anchor_map[target]:
                errors.append(f'{path}: missing anchor {href}')
            checked += 1
    ids = {}
    for path, text in texts.items():
        if path.startswith('papers/') and not path.endswith('/README.md'):
            match = re.search(r'^id: (.+)$', text, re.M)
            topic = re.search(r'^primary_topic: (.+)$', text, re.M)
            if not match or not topic or topic.group(1) != path.split('/')[1]:
                errors.append('Missing ID or mismatched topic: ' + path)
            elif match.group(1) in ids:
                errors.append('Duplicate article ID: ' + match.group(1))
            else:
                ids[match.group(1)] = path
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(records)} unchanged historical PDFs, {len(ids)} unique articles, {len(texts)} Markdown files, {checked} local links/anchors')
    return 0

if __name__ == '__main__':
    sys.exit(main())
