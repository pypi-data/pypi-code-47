from .colors import *
from .scales import *

fontFamily = "'Open Sans', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'"


def altair_template():
    # Typography
    font = fontFamily
    labelFont = fontFamily 
    sourceFont =fontFamily
    # Colors
    main_palette = discrete
    sequential_palette = sequential
    return {
        "config": {
            "title": {
                "fontSize": 15,
                "font": font,
                "fontColor": fontColor
            },
            "axisX": {
                "domainColor": axisColor,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "titleFont": font,
                "titleFontSize": 12,
                "titlePadding": 10,
            },
            "axisY": {
                "gridColor": gridColor,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
            },
            "range": {
                "category": discrete,
                "diverging": sequential,
            },
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "", # set it to no-title by default
            },
            "view": {
                "stroke": "transparent", 
            },
            "area": {
               "fill": markColor,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
           },
           "trail": {
               "color": markColor,
               "stroke": markColor,
           },
           "path": {
               "stroke": markColor,
               "strokeWidth": 0.5,
           },
           "point": {
               "filled": True,
           },
           "text": {
               "font": sourceFont,
               "color": markColor,
               "fontSize": 11,
               "align": "right",
               "fontWeight": 400,
               "size": 11,
           }
        }
    }