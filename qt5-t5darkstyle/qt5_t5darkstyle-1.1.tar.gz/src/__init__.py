"""
Dark Stylesheet for QT5
=======================
the css and icons were inspired by https://github.com/ColinDuquesnoy/QDarkStyleSheet
which are Copyright (c) 2013-2018 Colin Duquesnoy

Usage:
from qt5_t5darkstyle import darkstyle_css
widget.setStylesheet(darkstyle_css())

or set your own colors with:
widget.setStylesheet(darkstyle_css(MY_COLORS_DICT))
"""
import os
from qt5_t5darkstyle import darkstyle_res


DARKSTYLE_CSS_COLORS = {
    "foreground_color":             "#ffffff",
    "background_color":             "#333333",
    "tooltip_background_color":     "#ffff77",
    "tooltip_border_color":         "#cccc55",
    "tooltip_color":                "#000000",
    "selection_background_color":   "#006600",
    "selection_highlight_color":    "#99ff99",
    "border_color":                 "#666666",
    "disabled_color":               "#bbbbbb",
    "edit_background_color":        "#000000",
    "scroll_background_color":      "#000000",
    "scroll_foreground_color":      "#00aa00",
    "button_background_color":      "#555555",
}


def darkstyle_css(colors_dict=None):
    if colors_dict is None:
        colors_dict = DARKSTYLE_CSS_COLORS
    f = open(os.path.join(os.path.dirname(__file__), "darkstyle.css"))
    css = f.read()
    f.close()
    for k, v in colors_dict.items():
        keyWithParentheses = "<%s>" % k
        while keyWithParentheses in css:
            css = css.replace(keyWithParentheses, v)
    return css
