#!/usr/bin/env python3
"""Собирает петлю-гифку из 3 эмоций маскота: happy → surprised → skeptical."""
from PIL import Image

emotions = ['happy', 'surprised', 'skeptical']
frames = []
for e in emotions:
    im = Image.open(f'/root/portfolio/public/mascot/mascot-{e}.png').convert('RGBA')
    im = im.resize((220, 232), Image.LANCZOS)
    frames.append(im)

# петля: happy → surprised → skeptical → happy (замкнутая)
frames.append(frames[0])

frames[0].save(
    '/root/github-profile/assets/mascot-loop.gif',
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0,
    optimize=True,
    disposal=2,
)
im = Image.open('/root/github-profile/assets/mascot-loop.gif')
print('frames:', im.n_frames, 'size:', im.size)
import os
print('bytes:', os.path.getsize('/root/github-profile/assets/mascot-loop.gif'))
