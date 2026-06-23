#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

YAML_FILES = [
    'source/rules.yaml',
    'stash/override.yaml',
    'stash/rules.yaml',
    'stash/external-providers.yaml',
]
URL_FILES = [
    'quantumult-x/external-filter-remote.conf',
    'loon/external-remote-rules.conf',
    'stash/external-providers.yaml',
]


def check_yaml():
    for rel in YAML_FILES:
        yaml.safe_load((ROOT / rel).read_text(encoding='utf-8'))
    print(f'yaml_ok {len(YAML_FILES)} files')


def collect_urls():
    urls = []
    for rel in URL_FILES:
        text = (ROOT / rel).read_text(encoding='utf-8')
        urls.extend(re.findall(r'https://[^\s,]+', text))
    unique = []
    for url in urls:
        if url not in unique:
            unique.append(url)
    return unique


def check_urls():
    failures = []
    for url in collect_urls():
        try:
            code = subprocess.check_output(
                ['curl', '-L', '--retry', '2', '--connect-timeout', '10', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
                text=True,
                stderr=subprocess.DEVNULL,
                timeout=40,
            ).strip()
        except Exception as exc:
            failures.append((type(exc).__name__, url))
            continue
        if code != '200':
            failures.append((code, url))
    if failures:
        print('url_check_failed')
        for code, url in failures:
            print(code, url)
        return False
    print(f'url_ok {len(collect_urls())} urls')
    return True


def main():
    check_yaml()
    if '--urls' in sys.argv:
        if not check_urls():
            return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
