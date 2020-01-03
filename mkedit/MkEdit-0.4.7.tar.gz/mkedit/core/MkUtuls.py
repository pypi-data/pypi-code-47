#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mistune import Markdown, Renderer, escape


class MkRenderer(Renderer):
    def __init__(self, **kwargs):
        Renderer.__init__(self, **kwargs)

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """

        code = code.rstrip('\n')
        print(code)
        if lang and lang == "mermaid":
            code = escape(code, smart_amp=False)
            return '<div class="mermaid">%s\n</div>\n' % code

        return Renderer.block_code(self, code, lang)


class MkUtuls:
    def __init__(self):
        renderer = MkRenderer(escape=True, hard_wrap=True)
        self.markdown = Markdown(renderer=renderer)

    def parse(self, txt):
        return self.markdown.parse(txt)
