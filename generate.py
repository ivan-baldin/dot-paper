#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cairosvg

generate_grid_sizes = [5, 7, 10]
settings = dict(
    dot_size=0.15, dot_color='rgb(200,200,200)',
    units='mm', width=210, height=297,
    margin=5, export_fmt='a4-{grid_size}{units}.pdf',
)

template = '''<?xml version="1.0" standalone="yes"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
		width="{width}{units}" height="{height}{units}" viewBox="0 0 {width} {height}">
    <defs>
        <pattern id="grid" x="0" y="0" width="{grid_w}" height="{grid_h}" patternUnits="userSpaceOnUse">
            <circle cx="{dot_x}" cy="{dot_y}" r="{dot_size}" fill="{dot_color}" />
        </pattern>
    </defs>
    <rect x="{margin}" y="{margin}" width="{pattern_w}" height="{pattern_h}" fill="url(#grid)" />
</svg>
'''

settings.update(
    pattern_w=settings['width']-2*settings['margin'],
    pattern_h=settings['height']-2*settings['margin'],
)

for grid_size in generate_grid_sizes:
    settings.update(
        grid_size=grid_size, grid_w=grid_size, grid_h=grid_size,
        dot_x=grid_size/2, dot_y=grid_size/2, 
    )

    img = template.format(**settings).encode('utf-8')
    cairosvg.svg2pdf(bytestring=img, write_to=settings['export_fmt'].format(**settings))
