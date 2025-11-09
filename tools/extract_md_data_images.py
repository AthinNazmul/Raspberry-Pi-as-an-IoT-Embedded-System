#!/usr/bin/env python3
import os
import re
import base64
import sys
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
ASSETS_ROOT = ROOT / "assets"

# Regex to find lines like: [image1]: <data:image/png;base64,AAAA...>
# We allow label chars up to ']' and capture mime type and base64 body until '>'
DATA_IMG_RE = re.compile(r"^\[([^\]]+)\]:\s*<data:(image/[a-zA-Z0-9.+-]+);base64,([^>]+)>", re.MULTILINE)

EXT_MAP = {
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/gif": "gif",
    "image/svg+xml": "svg",
    "image/webp": "webp",
}

def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    # replace non-alnum with hyphens
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch)
        else:
            out.append('-')
    slug = ''.join(out)
    # collapse multiple hyphens
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-') or 'assets'


def ensure_unique_path(dirpath: Path, basename: str, ext: str) -> Path:
    candidate = dirpath / f"{basename}.{ext}"
    i = 2
    while candidate.exists():
        candidate = dirpath / f"{basename}-{i}.{ext}"
        i += 1
    return candidate


def process_markdown(md_path: Path) -> int:
    rel_dir = md_path.parent.relative_to(ROOT)
    if rel_dir == Path('.'):
        slug = 'root'
    else:
        # use the last segment as chapter folder name
        slug = slugify(rel_dir.name)
    target_dir = ASSETS_ROOT / slug
    text = md_path.read_text(encoding='utf-8')

    replacements = []
    count = 0
    for m in DATA_IMG_RE.finditer(text):
        label = m.group(1).strip()
        mime = m.group(2).strip().lower()
        b64 = m.group(3).strip()
        ext = EXT_MAP.get(mime)
        if not ext:
            print(f"Skipping unsupported mime {mime} in {md_path}", file=sys.stderr)
            continue
        try:
            data = base64.b64decode(b64, validate=True)
        except Exception:
            # Fallback without strict validation
            data = base64.b64decode(b64)
        target_dir.mkdir(parents=True, exist_ok=True)
        base = slugify(label)
        out_path = ensure_unique_path(target_dir, base, ext)
        out_path.write_bytes(data)
        rel_out = os.path.relpath(out_path, start=md_path.parent)
        new_def = f"[{label}]: <{rel_out}>"
        replacements.append((m.span(), new_def))
        count += 1

    if replacements:
        # apply replacements from end to start to keep indices valid
        new_text = []
        last_idx = 0
        for (start, end), new_def in sorted(replacements, key=lambda x: x[0][0]):
            new_text.append(text[last_idx:start])
            new_text.append(new_def)
            last_idx = end
        new_text.append(text[last_idx:])
        md_path.write_text(''.join(new_text), encoding='utf-8')
    return count


def main():
    total = 0
    files = []
    for p in ROOT.rglob('*.md'):
        files.append(p)
    files.sort()
    for md in files:
        n = process_markdown(md)
        if n:
            print(f"Converted {n} image(s) in {md.relative_to(ROOT)}")
            total += n
    print(f"Total images converted: {total}")

if __name__ == '__main__':
    main()
