# -*- coding: utf-8 -*-
"""
This is the default configuration for producing reveal.js slides with pandoc

See for more info:
https://github.com/jgm/pandoc/wiki/Using-pandoc-to-produce-reveal.js-slides
"""

# Themes
# beige, black, blood, league, moon, night, serif, simple, sky,
# solarized, white
REVEAL_THEME = "black"

REVEAL_CONFIG = {
    # Transition style
    # default/cube/page/concave/zoom/linear/fade/none
    "transition": "default",
}

# Slide levels for pandoc
# See http://pandoc.org/MANUAL.html#structuring-the-slide-show
REVEAL_PANDOC_SLIDE_LEVEL = 1
