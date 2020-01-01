#!/usr/bin/env python
# encoding: utf-8

"""
Parsing latex error to bubble up import ones
"""

from functools import wraps

def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def generic_sink(func):
    """ Generic sink

    :param function: function that define the end of the sink

    >>> print_sink = generic_sink(print)
    >>> print_sink.send("coucou")
    coucou
    """
    while True:
        c = (yield)
        if c:
            func(c)

@coroutine
def filter_errors(target):
    """ Filter pdflatex log to bubble up error

    https://en.wikibooks.org/wiki/LaTeX/Errors_and_Warnings
    
    >>> s = generic_sink(print)
    >>> tex_filter = filter_errors(s)
    >>> tex_filter.send("! Undefined control sequence.")
    ! Undefined control sequence.
    >>> tex_filter.send("l.43     \\includegraphics")
    l.43     \\includegraphics
    >>> tex_filter.send("l.43     \\includegraphics")
    >>> 
    """
    while True:
        line = (yield)
        if line.startswith("!"):
            target.send(line)
            line = (yield)
            while not line.startswith('See'):
                target.send(line)
                line = (yield)

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
