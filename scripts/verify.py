#!/usr/bin/env python3
"""Verify the plugin package, pinned upstream and opaque sample color pairs.

This checks the bundled example, not computed styles in a consuming app.
"""

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ('connect', 'design', 'mockup', 'review', 'setup', 'states', 'style', 'system')
MOVED = ('colors', 'contrast', 'figcraft', 'figma', 'motion', 'patterns', 'responsive', 'typography')
DESCRIPTION_LIMIT = 300


def check_package():
    manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    assert manifest['name'] == 'design'
    assert (ROOT / manifest['icon']).is_file(), 'Plugin icon missing'
    expected = set(ENTRY)
    actual = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    assert actual == expected, f'Skill inventory mismatch: {actual ^ expected}'
    for path in (ROOT / 'skills').glob('*/SKILL.md'):
        text = path.read_text()
        assert text.startswith('---\n'), f'Missing frontmatter: {path}'
        frontmatter = text.split('---', 2)[1]
        assert re.search(r'^name: ' + re.escape(path.parent.name) + r'$', frontmatter, re.M)
        assert re.search(r'^description: .+', frontmatter, re.M)
    docs = [ROOT / 'README.md', ROOT / 'UPSTREAM.md', *(ROOT / 'skills').rglob('*.md')]
    for path in docs:
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[a-z]+://', link) or link.startswith('#'):
                continue
            target = link.split('#', 1)[0]
            assert (path.parent / target).exists(), f'Broken link: {path}: {link}'
    print(f'Package: {len(actual)} skills, manifest, icon and local links verified')


def check_structure():
    skills = {p.parent.name: p.read_text() for p in (ROOT / 'skills').glob('*/SKILL.md')}
    visible = sorted(s for s, text in skills.items()
                     if not re.search(r'^disable-model-invocation: true$', text, re.M))
    assert visible == sorted(ENTRY), f'Only the entry skills are visible to Claude: {visible}'
    for skill, text in skills.items():
        hidden = re.search(r'^disable-model-invocation: true$', text, re.M)
        assert hidden or not re.search(r'^user-invocable: false$', text, re.M), (
            f'user-invocable: false saves no context: {skill}'
        )
        description = re.search(r'^description: (.*)$', text, re.M).group(1)
        assert len(description) <= DESCRIPTION_LIMIT, f'Description over {DESCRIPTION_LIMIT}: {skill}'
    linked = '\n'.join(skills.values())
    references = sorted((ROOT / 'skills').glob('*/references/*.md'))
    for path in references:
        text = path.read_text()
        assert f'references/{path.name}' in linked, f'Reference not linked from a SKILL.md: {path}'
        for link in re.findall(r'\]\(([^)#]+\.md)', text):
            target = (path.parent / link).resolve()
            assert target.parent.name != 'references', f'Reference links a reference: {path}: {link}'
        if text.count('\n') > 100:
            assert re.search(r'^## Contents$', text[:600], re.M), f'Missing table of contents: {path}'
    pattern = re.compile(r'design:(' + '|'.join(MOVED) + r')\b(?!-)')
    for path in [ROOT / 'README.md', ROOT / 'USAGE.md', *(ROOT / 'skills').rglob('*.md')]:
        found = pattern.search(path.read_text())
        assert not found, f'Moved skill named as a skill: {path}: {found.group(0)}'
    print(f'Structure: {len(visible)} entry skills, {len(references)} references verified')


def check_upstream():
    lock = json.loads((ROOT / 'upstream.lock.json').read_text())
    assert re.fullmatch(r'[0-9a-f]{40}', lock['commit']), 'Unpinned upstream commit'
    base = ROOT / 'upstream/impeccable'
    expected = set()
    for entry in lock['files']:
        path = base / entry['path']
        assert path.resolve().is_relative_to(base.resolve()), 'Unsafe upstream path'
        assert not path.is_symlink(), f'Unexpected upstream symlink: {path}'
        data = path.read_bytes()
        digest = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
        assert digest == entry['blob'], f'Upstream content changed: {entry["path"]}'
        if entry['mode'] == '100755':
            assert path.stat().st_mode & 0o111, f'Launcher not executable: {path}'
        expected.add(entry['path'])
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}
    assert expected == actual, f'Unexpected upstream inventory: {expected ^ actual}'
    for required in ('LICENSE', 'NOTICE.md', 'SKILL.md', 'scripts/VERSION', 'scripts/engine-checksums.txt'):
        assert required in expected, f'Upstream dependency missing: {required}'
    json.loads((base / 'scripts/data/font-index.json').read_text())
    print(f'Upstream: {len(expected)} exact Git blobs verified at {lock["commit"][:12]}')


def luminance(color):
    assert re.fullmatch(r'#[0-9a-fA-F]{6}', color), f'Expected opaque sample hex: {color}'
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def ratio(first, second):
    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


def check_sample_colors():
    css = (ROOT / 'skills/design/assets/theme.css').read_text()
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    blocks = re.findall(r'([^{}]+)\{([^{}]*)\}', css)
    assert len(blocks) == 2, 'Sample verifier expects two flat theme blocks'
    surfaces = ('bg-1', 'bg-2', 'overlay', 'field')
    count = 0
    for selector, declarations in blocks:
        tokens = dict(re.findall(r'--([\w-]+):\s*([^;]+);', declarations))
        pairs = [('fg-1', 'bg-1', 4.5), ('fg-2', 'bg-2', 4.5)]
        pairs += [(f'{role}-foreground', role, 4.5) for role in ('overlay', 'field')]
        pairs += [(f'{role}-foreground', role, 4.5) for role in ('accent', 'success', 'warning', 'danger', 'info')]
        pairs += [('accent-foreground', state, 4.5) for state in ('accent-hover', 'accent-pressed')]
        pairs += [('field-foreground', 'field-hover', 4.5)]
        pairs += [(foreground, surface, minimum) for surface in surfaces for foreground, minimum in
                  (('muted', 4.5), ('link', 4.5), ('control-border', 3), ('focus-ring', 3))]
        for foreground, background, minimum in pairs:
            measured = ratio(tokens[foreground], tokens[background])
            assert measured >= minimum, (
                f'{selector.strip()}: {foreground}/{background} = {measured:.4f}, needs {minimum}'
            )
            count += 1
    print(f'Sample palette: {count} opaque pairs passed across light/dark themes')
    print('Not assessed: real app styles, transparency, images, focus geometry or rendered layouts')


def main():
    check_package()
    check_structure()
    check_upstream()
    check_sample_colors()


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, KeyError, ValueError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
