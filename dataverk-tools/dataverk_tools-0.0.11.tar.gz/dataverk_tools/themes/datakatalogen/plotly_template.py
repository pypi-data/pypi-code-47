from .colors import fontColor
from .scales import diverging, sequential, sequentialminus
import plotly.graph_objects as go
import plotly.io as pio

plotly_template = pio.templates["plotly_white"]

plotly_template.layout.colorscale = go.layout.Colorscale(
    diverging=diverging,
    sequential=sequential,
    sequentialminus=sequentialminus
)

plotly_template.layout.font = go.layout.Font(
    color = fontColor,
    family = "'Open Sans', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'"
)

plotly_template.layout.colorway = ("#3385D1", "#FFA733", "#C86151", "#337C9B", "#FFD81A", "#38A161", "#77A186", "#A3AA6F", "#826BA1")




