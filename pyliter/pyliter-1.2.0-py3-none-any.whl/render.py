""" python rendering pyglet Window
"""

import pyglet
from .document import PythonDocument
from .color import Color


class PythonRender(pyglet.window.Window):
    def __init__(
        self,
        fileobj,
        start_line,
        line_count,
        style_book: dict = None,
        preview: bool = False,
        transparent: bool = False,
    ):
        """Render syntax-highlighted Python code to a window using
        the supplied style_book.

        :param fileobj:     file-like object containing Python text
        :param start_line:  line to begin rendering
        :param line_count:  number of lines to render
        :param style_book:  dictionary of style dictionaries
        :param preview:     controls whether the render text is displayed
        :param transparent: render with a transparent background if true
        """

        self.preview = preview

        self.document = PythonDocument(fileobj, start_line, line_count, style_book)

        width, height = self.document.dimensions

        self.layout = pyglet.text.layout.TextLayout(
            self.document, width, height, multiline=True
        )
        self.layout.x = self.margin
        self.layout.y = self.margin

        try:
            caption = fileobj.name
        except AttributeError:
            caption = "stdin"

        super().__init__(
            width=width + (self.margin * 2),
            height=height + (self.margin * 2),
            visible=preview,
            caption=caption,
        )

        bg = Color(*self.document.background_color)
        if transparent:
            bg.alpha.value = 0

        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        pyglet.gl.glClearColor(*bg.rgba_f)

        vwidth, vheight = self.get_viewport_size()
        if (self.width, self.height) != (vwidth, vheight):
            pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
            pyglet.gl.glLoadIdentity()
            pyglet.gl.glOrtho(0, vwidth, 0, vheight, -1, 1)
            pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)

    @property
    def margin(self):
        """Pixels between edges and layout.
        """
        return 0

    def on_draw(self):
        """Clear the window and draw it's contents (again).
        """
        self.clear()
        self.layout.draw()

    def save(self, filename: str):
        """Saves the contents of this window to filename.
        """

        if not filename:
            return

        image = pyglet.image.get_buffer_manager().get_color_buffer()

        if (self.width, self.height) != self.get_viewport_size():
            image = image.get_region(0, 0, self.width, self.height)

        image.save(filename)

    def run(self, filename: str = None):
        """Start up a pyglet event loop if in preview mode, otherwise
        call this object's on_draw method, save buffer contents to a
        file and call it a day.
        """
        if not self.preview:
            self.on_draw()
            self.save(filename)
            return

        pyglet.app.run()
