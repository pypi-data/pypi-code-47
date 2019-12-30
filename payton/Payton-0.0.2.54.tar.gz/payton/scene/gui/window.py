from enum import Enum
from typing import Any, Callable, Dict, Optional, Tuple

import numpy as np

from payton.scene.gui.base import Shape2D, Text
from payton.scene.shader import Shader


class Theme:
    """Main theme definitions for window elements
    """

    def __init__(self):
        self.opacity = 0.9

        self.background_color: Tuple[float, float, float] = [0.05, 0.05, 0.05]
        self.text_color: Tuple[float, float, float] = [1.0, 1.0, 1.0]
        self.title_background_color: Tuple[float, float, float] = [
            235 / 255,
            210 / 255,
            52 / 255,
        ]
        self.title_text_color: Tuple[float, float, float] = [0.0, 0.0, 0.0]


class WindowAlignment(Enum):
    """Window alignment

    Note that, in fixed cases (left, top, right, bottom) Width / Height
    information will be over-ridden.
    """

    FREE = "free"
    LEFT = "left"
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"


class WindowElement(Shape2D):
    def __init__(
        self,
        width: int = 400,
        height: int = 300,
        left: int = 10,
        top: int = 10,
        align: WindowAlignment = WindowAlignment.FREE,
        theme: Optional[Theme] = None,
        **kwargs,
    ):
        kwargs["position"] = (left, top, 0)
        kwargs["size"] = (width, height)
        super().__init__(**kwargs)
        self._init: bool = False
        self.align = align
        self.theme = theme if theme is not None else Theme()
        self.material.opacity = self.theme.opacity

    def _reposition(self):
        if self.align == WindowAlignment.LEFT:
            self.position = [0.0, 0.0, 0.0]
            self.size = (self.size[0], self._parent_height)
        elif self.align == WindowAlignment.RIGHT:
            self.position = [self._parent_width - self.size[0], 0.0, 0.0]
            self.size = (self.size[0], self._parent_height)
        elif self.align == WindowAlignment.TOP:
            self.position = [0.0, 0.0, 0.0]
            self.size = (self._parent_width, self.size[1])
        elif self.align == WindowAlignment.BOTTOM:
            pos = [0, self._parent_height - self.size[1], 0]
            self.position = pos
            self.size = (self._parent_width, self.size[1])

    def draw(self):
        self._reposition()

    def render(
        self,
        lit: bool,
        shader: Shader,
        parent_matrix: Optional[np.ndarray] = None,
        _primitive: int = None,
    ) -> None:
        """Render the Text

        This calls the render method of
        `payton.scene.geometry.base.Object.render` then renders the text on top
        of the rectangle.
        """
        if not self._init:
            self.draw()

        super().render(lit, shader, parent_matrix)

    def add_child(self, name, obj: Shape2D) -> bool:  # type: ignore
        if obj.position[0] > self.size[0]:
            obj.position[0] = self.size[0] - 1
        total_v = obj.position[0] + obj.size[0]
        exceed = int(total_v - self.size[0])
        if exceed > 0:
            obj.size = (obj.size[0] - exceed, obj.size[1])

        if obj.position[1] > self.size[1]:
            obj.position[1] = self.size[1] - 1
        total_v = obj.position[1] + obj.size[1]
        exceed = int(total_v - self.size[0])
        if exceed > 0:
            obj.size = (obj.size[0], obj.size[1] - exceed)

        super().add_child(name, obj)
        obj.set_parent_size(self.size[0], self.size[1])


class Window(WindowElement):
    def __init__(
        self,
        title: str = "",
        width: int = 400,
        height: int = 300,
        left: int = 10,
        top: int = 10,
        align: WindowAlignment = WindowAlignment.FREE,
        theme: Optional[Theme] = None,
        **kwargs: Dict[str, Any],
    ):
        """Initialize Window

        @NOTE: I am aware that I could have just define "title" as other
               elemenets are already arguments of WindowElement but some
               code hinting and completion tools are a bit stupid. They
               can not inherit from parent class.
        """
        super().__init__(
            width=width,
            height=height,
            left=left,
            top=top,
            align=align,
            theme=theme,
            **kwargs,
        )
        self.title = title
        self.add_child(
            "title",
            Text(
                position=(0, 0, 0),
                size=(self.size[0], 20),
                label=self.title,
                # bgcolor=self.theme.title_background_color,
                color=self.theme.title_text_color,
                opacity=0.5,
            ),
        )

    def draw(self):
        super().draw()
        w, h = self.size[0], self.size[1]
        self.clear_triangles()
        if not self._init:
            self.add_triangle(
                [[0, 22, 1], [w, h, 1], [w, 22, 1]],
                texcoords=[[0, 0], [1, 1], [1, 0]],
                colors=[
                    self.theme.background_color,
                    self.theme.background_color,
                    self.theme.background_color,
                ],
            )
            self.add_triangle(
                [[0, 22, 1], [0, h, 1], [w, h, 1]],
                texcoords=[[0, 0], [0, 1], [1, 1]],
                colors=[
                    self.theme.background_color,
                    self.theme.background_color,
                    self.theme.background_color,
                ],
            )
            self.add_triangle(
                [[0, 0, 1], [w - 1, 22, 1], [w - 1, 0, 1]],
                texcoords=[[0, 0], [1, 1], [1, 0]],
                colors=[
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                ],
            )
            self.add_triangle(
                [[0, 0, 1], [0, 22, 1], [w - 1, 22, 1]],
                texcoords=[[0, 0], [1, 1], [1, 0]],
                colors=[
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                ],
            )
            self._init = True


class Panel(WindowElement):
    def draw(self):
        super().draw()
        w, h = self.size[0], self.size[1]
        self.clear_triangles()
        if not self._init:
            self.add_triangle(
                [[0, 0, 1], [w, h, 1], [w, 0, 1]],
                texcoords=[[0, 0], [1, 1], [1, 0]],
                colors=[
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                ],
            )
            self.add_triangle(
                [[0, 0, 1], [0, h, 1], [w, h, 1]],
                texcoords=[[0, 0], [0, 1], [1, 1]],
                colors=[
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                    self.theme.title_background_color,
                ],
            )
            self.add_triangle(
                [[1, 1, 1], [w - 1, h - 1, 1], [w - 1, 1, 1]],
                texcoords=[[0, 0], [1, 1], [1, 0]],
                colors=[
                    self.theme.background_color,
                    self.theme.background_color,
                    self.theme.background_color,
                ],
            )
            self.add_triangle(
                [[1, 1, 1], [1, h - 1, 1], [w - 1, h - 1, 1]],
                texcoords=[[0, 0], [0, 1], [1, 1]],
                colors=[
                    self.theme.background_color,
                    self.theme.background_color,
                    self.theme.background_color,
                ],
            )

            self._init = True


class Button(Panel):
    def __init__(
        self,
        label: str,
        width: int = 400,
        height: int = 300,
        left: int = 10,
        top: int = 10,
        align: WindowAlignment = WindowAlignment.FREE,
        theme: Optional[Theme] = None,
        on_click: Optional[Callable] = None,
        **kwargs: Any,
    ):
        kwargs["on_click"] = on_click
        super().__init__(
            width=width,
            height=height,
            left=left,
            top=top,
            align=align,
            theme=theme,
            **kwargs,
        )

        self._label = label
        self.text = Text(
            position=(0, 0, 1),
            size=(10, 10),
            label=label,
            color=self.theme.text_color,
        )
        self.add_child("label", self.text)

    def draw(self, **kwargs):
        super().draw()
        size = self.text.text_size
        x = (self.size[0] / 2) - (size[0] / 2)
        y = (self.size[1] / 2.0) - (size[1] / 2) - 4
        self.text.label = self._label
        self.text.position = [x, y]
        self.text.size = (size[0], size[1] + 4)

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, text: str):
        self._label = text
        self.text.label = self._label
