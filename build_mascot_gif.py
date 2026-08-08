#!/usr/bin/env python3
"""Собирает гифку ровно из 3 эмоций: happy → surprised → skeptical.
Без дубликатов, RGB с белым фоном (никакой прозрачности — нет артефактов)."""
from PIL import Image

emotions = ['happy', 'surprised', 'skeptical']
frames = []
for e in emotions:
    im = Image.open(f'/root/portfolio/public/mascot/mascot-{e}.png').convert('RGBA')
    # белый фон вместо прозрачности — чтобы не было моргания при смене кадров
    bg = Image.new('RGB', im.size, (255, 255, 255))
    bg.paste(im, mask=im.split()[3])
    bg = bg.resize((220, 232), Image.LANCZOS)
    frames.append(bg)

frames[0].save(
    '/root/github-profile/assets/mascot-loop.gif',
    save_all=True,
    append_images=frames[1:],
    duration=600,
    loop=0,
    optimize=True,
    disposal=2,
)
im = Image.open('/root/github-profile/assets/mascot-loop.gif')
print('frames:', im.n_frames, 'size:', im.size)
import os
print('bytes:', os.path.getsize('/root/github-profile/assets/mascot-loop.gif'))
