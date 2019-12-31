'''
Clipboard Pygame: an implementation of the Clipboard using pygame.scrap.

.. warning::

    Pygame has been deprecated and will be removed in the release after Kivy
    1.11.0.
'''

__all__ = ('ClipboardPygame', )

from kivy.utils import platform
from kivy.core.clipboard import ClipboardBase
from kivy.utils import deprecated

if platform not in ('win', 'linux', 'macosx'):
    raise SystemError('unsupported platform for pygame clipboard')

try:
    import pygame
    import pygame.scrap
except:
    raise


class ClipboardPygame(ClipboardBase):

    _is_init = False
    _types = None

    _aliases = {
        'text/plain;charset=utf-8': 'UTF8_STRING'
    }

    @deprecated(
        msg='Pygame has been deprecated and will be removed after 1.11.0')
    def __init__(self, *largs, **kwargs):
        super(ClipboardPygame, self).__init__(*largs, **kwargs)

    def init(self):
        if ClipboardPygame._is_init:
            return
        pygame.scrap.init()
        ClipboardPygame._is_init = True

    def get(self, mimetype='text/plain'):
        self.init()
        mimetype = self._aliases.get(mimetype, mimetype)
        text = pygame.scrap.get(mimetype)
        return text

    def put(self, data, mimetype='text/plain'):
        self.init()
        mimetype = self._aliases.get(mimetype, mimetype)
        pygame.scrap.put(mimetype, data)

    def get_types(self):
        if not self._types:
            self.init()
            types = pygame.scrap.get_types()
            for mime, pygtype in list(self._aliases.items())[:]:
                if mime in types:
                    del self._aliases[mime]
                if pygtype in types:
                    types.append(mime)
            self._types = types
        return self._types
