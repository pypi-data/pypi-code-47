from ..detect import Detection


class Annotation(Detection):
    """Annotation with a boc and a label.

    :param str label: the label of the annotation
    :param float x_min: the x-coordinate of the left side of the rectangle
    :param float y_min: the y-coordinate of the top side of the rectangle
    :param float x_max: the x-coordinate of the right side of the rectangle
    :param float y_max: the y-coordinate of the bottom side of the rectangle
    """
    def __init__(self, label: str, x_min: float, y_min: float,
                 x_max: float, y_max: float):
        super().__init__(x_min, y_min, x_max, y_max)
        self.label = label

    def __eq__(self, other):
        if not isinstance(other, Annotation):
            return False
        if not super().__eq__(other):
            return False
        return self.label == other.label

    def to_tuple(self):
        return (self.label, self.x_min, self.y_min, self.x_max, self.y_max)

    def __iter__(self):
        return iter(self.to_tuple())

    def __hash__(self):
        return hash(tuple(self))
