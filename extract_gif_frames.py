#!/usr/bin/env python3
"""Извлекает кадры гифки в отдельные PNG для просмотра."""
from PIL import Image

im = Image.open('/root/github-profile/assets/mascot-loop.gif')
for i in range(im.n_frames):
    im.seek(i)
    im.convert('RGBA').save(f'/tmp/gif-frame-{i}.png')
    print(f'frame {i} saved')
