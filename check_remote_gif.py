#!/usr/bin/env python3
"""Качает гифку с GitHub и считает кадры — проверка кэша camo."""
import urllib.request
from PIL import Image
import io

urls = [
    'https://raw.githubusercontent.com/reconix37/reconix37/main/assets/mascot-loop.gif',
    'https://github.com/reconix37/reconix37/raw/main/assets/mascot-loop.gif',
]
for url in urls:
    try:
        data = urllib.request.urlopen(url, timeout=15).read()
        im = Image.open(io.BytesIO(data))
        hashes = []
        for i in range(im.n_frames):
            im.seek(i)
            import hashlib
            hashes.append(hashlib.md5(im.convert('RGB').tobytes()).hexdigest()[:8])
        print(url.split('/')[-1], '| bytes:', len(data), '| frames:', im.n_frames, '| unique:', len(set(hashes)), '|', hashes)
    except Exception as e:
        print(url, 'FAIL:', e)
