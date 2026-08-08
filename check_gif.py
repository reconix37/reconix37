#!/usr/bin/env python3
"""Проверяет, что гифка реально анимированная (кадры отличаются)."""
from PIL import Image
import hashlib

im = Image.open('/root/github-profile/assets/mascot-3emotions.gif')
print('frames:', im.n_frames, 'loop:', im.info.get('loop'), 'duration:', im.info.get('duration'))

hashes = []
for i in range(im.n_frames):
    im.seek(i)
    hashes.append(hashlib.md5(im.convert('RGB').tobytes()).hexdigest()[:8])
print('frame hashes:', hashes)
print('unique frames:', len(set(hashes)))
