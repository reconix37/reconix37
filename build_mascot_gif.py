#!/usr/bin/env python3
"""Собирает петлю-гифку из 4 эмоций маскота Дани."""
from PIL import Image

emotions = ['idle', 'happy', 'surprised', 'skeptical']
frames = []
for e in emotions:
    im = Image.open(f'/root/portfolio/public/mascot/mascot-{e}.png').convert('RGBA')
    im = im.resize((220, 232), Image.LANCZOS)
    frames.append(im)

# петля: idle → happy → surprised → skeptical → idle (замкнутая)
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
