#!/usr/bin/env python3
"""Собирает гифку из 3 эмоций с ПРОЗРАЧНЫМ фоном.
disposal=2 (restore to background) — чтобы не было мерцания/шлейфа."""
from PIL import Image

emotions = ['happy', 'surprised', 'skeptical']
frames = []
for e in emotions:
    im = Image.open(f'/root/portfolio/public/mascot/mascot-{e}.png').convert('RGBA')
    im = im.resize((220, 232), Image.LANCZOS)
    frames.append(im)

frames[0].save(
    '/root/github-profile/assets/mascot-3emotions.gif',
    save_all=True,
    append_images=frames[1:],
    duration=600,
    loop=0,
    optimize=False,   # optimize=True ломает прозрачность между кадрами
    disposal=2,
    transparency=0,
)
im = Image.open('/root/github-profile/assets/mascot-3emotions.gif')
print('frames:', im.n_frames, 'size:', im.size)
print('mode:', im.mode, '| transparency in info:', 'transparency' in im.info)
import os
print('bytes:', os.path.getsize('/root/github-profile/assets/mascot-3emotions.gif'))
