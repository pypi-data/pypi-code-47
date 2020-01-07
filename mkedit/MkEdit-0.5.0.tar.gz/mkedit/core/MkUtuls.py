#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mistune import Markdown, Renderer, escape


class MkRenderer(Renderer):
    def __init__(self, **kwargs):
        Renderer.__init__(self, **kwargs)
        self.hasMermaid = False

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.

        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')
        mermaid = False
        if lang and lang == "mermaid":
            mermaid = True
        else:
            code1 = str(code).lstrip()
            if code1.startswith('graph TD;') or code1.startswith('sequenceDiagram') or code1.startswith(
                    'gantt') or code1.startswith('gitGraph:'):
                mermaid = True

        if mermaid:
            code = escape(code, smart_amp=False)
            self.hasMermaid = True
            return '<div class="mermaid">%s\n</div>\n' % code

        return Renderer.block_code(self, code, lang)


class MkUtuls:
    def __init__(self):
        self.renderer = MkRenderer(escape=True, hard_wrap=True)
        self.markdown = Markdown(renderer=self.renderer)

    def parse(self, txt):
        return self.markdown.parse(txt)

    def hasMermaidCode(self, txt):
        self.markdown.parse(txt)
        return self.renderer.hasMermaid
