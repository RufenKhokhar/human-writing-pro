"""Validate this package's simple schema and local Markdown references."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'human-writing-pro'


def validate():
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    assert re.fullmatch(r'\d+\.\d+\.\d+', version), 'Invalid VERSION'
    text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    assert front, 'Missing frontmatter'
    header = front.group(1)
    assert re.search(r'^name: human-writing-pro$', header, re.M), 'Wrong skill name'
    desc = re.search(r'^description: (.+)$', header, re.M)
    assert desc and 0 < len(desc.group(1)) <= 1024, 'Invalid description'
    assert 'license: MIT' in header, 'Missing license metadata'
    assert f'  version: "{version}"' in header, 'Version mismatch'
    assert len(text.splitlines()) < 500, 'Entry point too long'
    assert (SKILL / 'LICENSE').read_bytes() == (ROOT / 'LICENSE').read_bytes()
    assert (SKILL / 'agents' / 'openai.yaml').is_file()
    for file in ROOT.rglob('*.md'):
        if any(p in {'dist', '.git', '__pycache__'} for p in file.relative_to(ROOT).parts):
            continue
        content = file.read_text(encoding='utf-8')
        assert '[TODO:' not in content, f'Unfinished scaffold: {file}'
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if link.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            path = (file.parent / link.split('#')[0]).resolve()
            assert path.is_relative_to(ROOT), f'Link leaves package: {file}: {link}'
            assert path.exists(), f'Broken local link: {file}: {link}'
    return version


if __name__ == '__main__':
    print(f'Package valid: {validate()}')
