from .._colormaps import _linear3color
from .scales import discrete, sequential

fontColor = "#000000"
axisColor = '#EBF0F8'
gridColor = '#DFE8F3'
background = "#FFFFFF"
markColor = discrete[0]

colorscale = [[i/10,color] for i, color in enumerate(sequential)]
colorscale_diverging = [[i/10,color] for i, color in enumerate(sequential)]
colorscale_sequential = [[i/10,color] for i, color in enumerate(sequential)]
colorscale_sequentialminus = [[i/10,color] for i, color in enumerate(sequential)]
