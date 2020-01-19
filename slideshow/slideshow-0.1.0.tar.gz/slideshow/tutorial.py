from slideshow import slideshow
from textwrap import dedent

slide, run = slideshow()


@slide
def introduction():
    return dedent(
        """\
    Slideshow
    =========

    Simple slides mixed with python REPL.
    Press Enter to go to next slide.
    """
    )


@slide
def examples():
    return dedent(
        """\
            Take a look at the source code to see how things work.
            After each command, press Enter to execute.

            b       : Go back
            g <num> : Go to slide `num`
            l       : List slides
            r       : Break out to REPL.
            """
    )


@slide
def writing():
    return dedent(
        """\
            from slideshow import slideshow

            slide, run = slideshow()

            @slide
            def introduction():
                return 'This is the introduction'

            @slide
            def thankyou():
                return 'Thank you.'

            ss = run()


            # This command is also used to resume a slideshow if you have
            # jumped out to REPL
            next(ss)
            """
    )


@slide
def repl():
    return dedent(
        """\
            You can jump out to the Python REPL by pressing `r Enter`

            To come back to the slideshow type in `next(ss)`
            """
    )
