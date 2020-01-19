from functools import partial
from textwrap import dedent
import os


def slideshow(*, fail_silent=True):
    slides = {}
    rows, columns = list(map(int, os.popen("stty size", "r").read().split()))

    def prompt(i):
        total_slides = len(slides)
        slide_fn = slides[i]
        return f"{i:>3}/{total_slides:<3} | {slide_fn.__name__}"

    def list_slides():
        total_slides = len(slides)
        for i, slide_fn in slides.items():
            print(prompt(i))

    def slide(fn=None, n=None):
        if fn is None:
            return partial(slide, n=n)
        n = len(slides) if n is None else n
        slides[n] = fn
        return fn

    def show(string):
        lines = string.split("\n")
        n_lines = len(lines)
        pre, post = rows // 2, rows // 2
        pre -= n_lines // 2
        post -= n_lines // 2
        left, right = columns // 2, columns // 2
        max_len = max(len(line) for line in lines)
        left -= max_len // 2
        right -= max_len // 2
        lines = [" " * max(0, left) + line + " " * max(0, right) for line in lines]
        print("\n" * pre)
        print("\n".join(lines))
        print("\n" * post)

    def run():
        current_slide = 0
        cmd = None
        while True:
            try:
                show(slides[current_slide]())
                cmd = (
                    input(f"{prompt(current_slide)} :>").strip() if cmd is None else cmd
                )
                if cmd == "":  # Forward
                    current_slide += 1
                    cmd = None
                elif cmd == "b":  # Back
                    current_slide -= 1
                    cmd = None
                elif cmd.startswith("g"):  # Go to slide number
                    current_slide = int(cmd.split()[1])
                    cmd = None
                elif cmd.startswith("l"):  # List all slides
                    list_slides()
                    cmd = input(f"{prompt(current_slide)} :>").strip()
                elif cmd == "r":  # Break out to normal python repl
                    yield
                    cmd = None
                else:
                    cmd = None
                if current_slide not in slides:
                    current_slide = 0
                    show("END")
                    yield None
            except Exception as e:
                if not fail_silent:
                    raise

    return slide, run


if __name__ == "__main__":
    s = run()
    next(s)
