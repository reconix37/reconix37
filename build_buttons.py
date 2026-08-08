#!/usr/bin/env python3
"""Собирает кнопки-плашки для GitHub README: тёмный rounded rect + иконка + текст.
Каждая кнопка — отдельный SVG файл в assets/buttons/, на белом фоне.
Стиль: графит #1F1D1A, белый текст, скругление 8, моноширинный шрифт.
"""
import re, pathlib

BTN_DIR = pathlib.Path('/root/github-profile/assets/buttons')
BG = '#1F1D1A'
FG = '#FFFFFF'
H = 36
ICON_SIZE = 18
PAD = 12

def load_icon(name):
    raw = (BTN_DIR / f'{name}.svg').read_text()
    # вытаскиваем path из simple-icons (fill=currentColor) или lucide (stroke)
    paths = re.findall(r'<path[^>]*d="([^"]+)"', raw)
    if not paths:
        raise ValueError(f'no path in {name}.svg')
    d = ' '.join(paths)
    stroke = 'stroke="currentColor" stroke-width="2"' if 'stroke' in raw else ''
    return f'<path d="{d}" {stroke}/>'

def make_button(name, label, icon=None):
    icon = icon or name
    body = load_icon(icon)
    # грубая оценка ширины: PAD + icon + gap + text
    text_w = len(label) * 8.2
    W = int(PAD + ICON_SIZE + 8 + text_w + PAD)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{BG}"/>
  <g fill="{FG}" transform="translate({PAD},{(H-ICON_SIZE)/2}) scale({ICON_SIZE/24})">
    {body}
  </g>
  <text x="{PAD+ICON_SIZE+8}" y="{H/2+5}" font-family="SFMono-Regular, Consolas, monospace" font-size="13" fill="{FG}">{label}</text>
</svg>'''
    (BTN_DIR / f'btn-{name}.svg').write_text(svg)
    print(f'btn-{name}.svg  {W}x{H}  label={label!r}')

make_button('telegram', 'Telegram', 'telegram')
make_button('linkedin', 'LinkedIn', 'linkedin')
make_button('github', 'GitHub', 'github')
make_button('portfolio', 'Portfolio', 'portfolio')
