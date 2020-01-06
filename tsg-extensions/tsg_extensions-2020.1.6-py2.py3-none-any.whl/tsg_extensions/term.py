# -*- coding: UTF-8 -*-
"""
An extension to the Markdown syntax to format output like a computer console/terminal.

The syntax is very similar to a literal code block, but instead of three backticks
(```) before an after, you use three carets (^^^).

You also have to define the CSS class "terminal". Here's a simple example of the
Markdown for this extension:

# Some heading

^^^
some output that looks like a terminal
^^^

Here's what the resulting HTML looks like:
<h1>Some heading</h1>
<div class="terminal">
<pre><code>some output that looks like a terminal
</code></pre>
</div>

The use of a <div> is so we get a solid block, instead of the background color
simply wrapping the text.
"""
import sys
import re

import markdown
from markdown.blockprocessors import CodeBlockProcessor, util, BlockParser


class FakeMD:
    """Exist to fake the API for __init__ on BlockProcessors"""
    def __init__(self):
        self.tab_length = 4


class FakeParser:
    """Exist to fake the API for __init__ on BlockProcessors"""
    def __init__(self):
        self.md = FakeMD()


class TerminalProcessor(CodeBlockProcessor, markdown.extensions.Extension):
    """Defines how to process a text block for mimicking terminal output

    The mixin of markdown.extensions.Extension was the only way I could get the
    Markdown lib to build this extension. Following the patterns in
    https://github.com/Python-Markdown/markdown/tree/master/markdown/extensions
    didn't work...
    """
    def __init__(self):
        """This needs to be defined to avoid API breakage. Seems like not a lot
        of people write BlockProcessors for Markdown, because if they did, they'd
        realized that the API for building BlockProcessors is different than every
        other processor.
        """
        super().__init__(FakeParser())

    def test(self, parent, block):
        return block.startswith('^^^') and block.endswith('^^^')

    def run(self, parent, blocks):
        block = blocks.pop(0)
        lines = block.split('\n')
        literal_code = lines[1:-1]
        div = util.etree.SubElement(parent, 'div')
        div.attrib['class'] = 'terminal'
        pre = util.etree.SubElement(div, 'pre')
        code = util.etree.SubElement(pre, 'code')
        code.text = util.AtomicString('%s\n' % util.code_escape('\n'.join(literal_code).rstrip()))

    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(TerminalProcessor(), 'terminal', 15)


def makeExtension(**kwargs):
    return TerminalProcessor(**kwargs)
