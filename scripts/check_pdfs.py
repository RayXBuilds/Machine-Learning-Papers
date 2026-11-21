"""Check the PDF inventory, canonical paths, exact bytes and links in Chinese guides."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def check_pdfs(*, show_pending=False):
    records = json.loads((ROOT / 'docs/pdfs.json').read_text())
    guides = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'papers').glob('*/*.md')
              if p.name != 'README.md'}
    if set(records) != guides:
        raise ValueError('PDF inventory and guides disagree: ' + str(set(records) ^ guides))
    historical = {r['new_path']: r['git_blob_sha'] for r in
                  json.loads((ROOT / 'docs/migration-2026-10-26.json').read_text())['files']}
    pending = []
    digests = {}
    expected = set()
    for guide, record in records.items():
        path = record.get('path')
        if not path:
            if not record.get('reason') or not record.get('source_url'):
                raise ValueError(f'{guide}: missing PDF needs a source and reason')
            pending.append((guide, record))
            continue
        canonical = Path('pdfs', *Path(guide).parts[1:]).with_suffix('.pdf').as_posix()
        if path != canonical and path not in historical:
            raise ValueError(f'{guide}: unexpected PDF path {path}')
        if path == canonical:
            expected.add(path)
        if not all(record.get(k) for k in ('source_url', 'retrieved', 'version', 'bytes', 'sha256', 'pages')):
            raise ValueError(f'{guide}: incomplete PDF provenance')
        if f'](../../{quote(path)})' not in (ROOT / guide).read_text():
            raise ValueError(f'{guide}: missing direct link to PDF')
        file = ROOT / path
        if path in historical and not file.is_file():
            data = subprocess.check_output(['git', 'cat-file', 'blob', historical[path]], cwd=ROOT)
        else:
            data = file.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if not data.startswith(b'%PDF-') or b'%%EOF' not in data[-8192:] or len(data) != record['bytes'] or digest != record['sha256']:
            raise ValueError(f'{path}: unexpected PDF contents')
        if digest in digests and digests[digest] != path:
            raise ValueError(f'{path}: duplicate PDF bytes at {digests[digest]}')
        digests[digest] = path
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'pdfs').rglob('*.pdf')}
    if actual != expected:
        raise ValueError('PDF inventory and files disagree: ' + str(actual ^ expected))
    if show_pending:
        for guide, record in pending:
            print(f"{guide}\t{record['source_url']}\t{record['reason']}")
    print(f'PASS: {len(guides)} PDF records, {len(expected)} new-library files, SHA-256 verified')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pending', action='store_true', help='List guides still lacking a PDF after checking the inventory')
    check_pdfs(show_pending=parser.parse_args().pending)
