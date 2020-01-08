from .._colormaps import _linear3color

discrete = ["#3385D1", "#FFA733", "#C86151", "#337C9B", "#FFD81A", "#38A161", "#77A186", "#A3AA6F", "#826BA1"]

sequential = _linear3color("#3385D1", "#66A4Dc", "#CCE1F3")

diverging = _linear3color("#77A186", "#EFEFEF", "#337C9B",10)

diverging_blue_orange_18 = _linear3color("#FFA733", "#EFEFEF", "#337C9B",18)
diverging_blue_orange_10 = _linear3color("#FFA733", "#EFEFEF", "#337C9B",10)

sequential_blue_yellow_18 = _linear3color("#337C9B","#FFD81A","#EFEFEF",18)
sequential_blue_yellow_10 = _linear3color("#337C9B","#FFD81A","#EFEFEF",10)

sequentialminus = _linear3color("#C86151", "#FFA733", "#FFD81A")
