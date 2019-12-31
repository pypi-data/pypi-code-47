# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auditorium']

package_data = \
{'': ['*'],
 'auditorium': ['static/css/*',
                'static/css/print/*',
                'static/css/theme/*',
                'static/js/*',
                'static/lib/font/league-gothic/*',
                'static/lib/font/source-sans-pro/*',
                'static/lib/js/*',
                'static/md/*',
                'static/plugin/highlight/*',
                'static/plugin/math/*',
                'static/plugin/multiplex/*',
                'static/plugin/notes-server/*',
                'static/plugin/notes/*',
                'static/plugin/print-pdf/*',
                'static/plugin/search/*',
                'static/plugin/zoom-js/*',
                'templates/*']}

install_requires = \
['fire>=0.2.1,<0.3.0',
 'jinja2>=2.10.3,<3.0.0',
 'markdown>=3.1.1,<4.0.0',
 'pygments>=2.5.2,<3.0.0',
 'sanic>=19.9.0,<20.0.0']

entry_points = \
{'console_scripts': ['auditorium = auditorium.__main__:main']}

setup_kwargs = {
    'name': 'auditorium',
    'version': '0.6.5',
    'description': 'A Python-powered slideshow maker with steroids.',
    'long_description': '# Auditorium\n\n[<img alt="PyPI - License" src="https://img.shields.io/pypi/l/auditorium.svg">](https://github.com/apiad/auditorium/blob/master/LICENSE)\n[<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/auditorium.svg">](https://pypi.org/project/auditorium/)\n[<img alt="PyPI" src="https://img.shields.io/pypi/v/auditorium.svg">](https://pypi.org/project/auditorium/)\n[<img alt="Travis (.org)" src="https://img.shields.io/travis/apiad/auditorium/master.svg">](https://travis-ci.org/apiad/auditorium)\n[<img alt="Codecov" src="https://img.shields.io/codecov/c/github/apiad/auditorium.svg">](https://codecov.io/gh/apiad/auditorium)\n[<img alt="Gitter" src="https://img.shields.io/gitter/room/apiad/auditorium">](https://gitter.im/auditorium-slides/community)\n[<img alt="Demo" src="https://img.shields.io/badge/demo-browse-blueviolet"></img>](https://auditorium-demo.now.sh)\n\n> A Python-powered slideshow creator with steroids.\n\nSee the demo at [auditorium-demo.now.sh](https://auditorium-demo.now.sh).\n\n## What\'s this about\n\nAuditorium is a Python-powered slideshow generator.\nYou write pure Python code, and obtain an HTML+JavaScript slideshow (using the amazing [reveal.js](https://revealjs.com) library).\nThe awesomeness comes from the fact that your Python backend is connected to the slideshow frontend, which allows your slideshow to dynamically change according to user input or automatically.\n\nThis opens the door to a few interesting use cases:\n\n*  The slides content itself can be generated by code. For example, long and repetitive sets of slides can be automatically generated, or tables and graphs embedded in slides can be generated on-the-fly with `matplotlib`, `bokeh`, `altair`, `plotly`, or any visualization package that produces HTML output.\n*  You can insert components in the slides that respond to user input, and execute a Python code in response. For example, you can generate an interactive graph that can be modified by moving sliders in a slideshow.\n*  You can create beautiful animations with simple Python code, that automatically play on a slide, using visualization libraries or simple HTML markup.\n\n> **And all of this without writing a single line of HTML or JavaScript.**\n\nAlternatively, if you need little to no Python code, you can author your slideshow in pure Markdown and add some Python sprinkless here and there when necessary.\n\n## Installation\n\nSimply run:\n\n    pip install auditorium\n\nTo see a quick demo run:\n\n    auditorium demo\n\nAnd point your browser at [localhost:6789](http://localhost:6789).\n\n## Quick Start - Python First\n\nIn `auditorium` you create a presentation via the `Show` class:\n\n```python\n# Content of <file.py>\n\nfrom auditorium import Show\nshow = Show("My Show")\n```\n\nEvery slide in your show is a Python method that renders the content and powers the backend logic.\nSlides are decorated with the `@show.slide` decorator.\nEvery slide receives a `ctx` parameter, of type `Context`, which provides the functionalities\nthat add content, both static and reactive.\n\n```python\n@show.slide\ndef one_slide(ctx):\n    # content\n```\n\nThen run the show:\n\n```bash\nauditorium run <file.py>\n```\n\n> **Slides are ordered in the same order in which methods are defined in your script.**\n\nOptionally, you can specify `--host` and `--port` as well as `--debug` which activates hot-reload and outputs debug info (powered by Sanic).\n\nAlternatively, you can also directly call `show.run`, although the recommended way is the previous one.\n\n```python\nshow.run(\'localhost\', 6789)\n```\n\nThe simplest possible form of content is static Markdown.\nYou can add it directly as the docstring of the corresponding slide function,\nor calling `ctx.markdown`.\n\n```python\n@show.slide\ndef static_content(ctx):\n    """\n    ## Static content\n\n    Can be added very simply with:\n\n    * Method _docstrings_\n    * Calling `show.markdown`\n    """\n\n    ctx.markdown("> Like this")\n```\n\nThere are several components in `auditorium` to style and layout your presentation, including reactive components that respond to user input.\n\n```python\n@show.slide\ndef interactive(ctx):\n    ctx.markdown("Enter your name")\n    name = ctx.text_input(default="World")\n    ctx.markdown(f"> Hello {name}")\n```\n\nThe slide code is considered stateless, and will be executed every time the input changes.\nYou should design your slides with this in mind to, for example, provide sensible default values that will work when your presentation first opens.\n\nSimple stateless animations can be created with `ctx.animation`, which execute the backend code for every frame.\nCombining this with drawing logic from, for example, `matplotlib` allows for very simple animated graphs and visualizations:\n\n```python\n@show.slide\ndef pyplot(ctx):\n    with ctx.animation(steps=50, time=0.33, loop=True) as anim:\n        # Every 0.33 seconds the graph will move\n        step = anim.current * 2 * math.pi / 50\n        x = np.linspace(0, 2 * math.pi, 100)\n        y = np.sin(x + step) + np.cos(x + step)\n        plt.plot(x, y)\n        plt.ylim(-2,2)\n        ctx.pyplot(plt, fmt=\'png\', height=350)\n```\n\n## Quick Start - Markdown First\n\nAlternatively, if you need little to no Python, you can author your slideshow in pure Markdown. Every level-2 header (`##`) becomes a slide.\n\n```markdown\n## Static content\n\nStatic content can be added with pure markdown.\n\n*  Some _markdown_ content.\n*  More **markdown** content.\n```\n\nPure Markdown can be used as long as all you need is static content. If you need more advanced features, you can add a Python code section anywhere in your slideshow and it will be executed.\n\n~~~markdown\n## Dynamic content\n\nIf you need interaction or advanced `auditorium` features,\nsimply add a code section.\n\n```python :run\nwith ctx.columns(2) as cl:\n    text = ctx.text_input("World")\n\n    cl.tab()\n\n    with ctx.success("Message"):\n        ctx.markdown(f"Hello {text}")\n```\n~~~\n\nAn instance named `ctx` will be magically available in every Python code section. Beware that **local variables are not persisted** between different code sections. This is a by-design decision to save you a bunch of headaches, believe me.\nIf you want variables to persist accross code sections, add `:persist` in the code declaration section. This also let\'s you interpolate Python variables directly inside the Markdown content.\n\n~~~markdown\n```python  :run :persist\ntext = ctx.text_input("World")\n```\n\nHello {text}. This is pure Markdown.\n~~~\n\nYou need to add `:run` to the code section declaration for it to be executed, otherwise `auditorium` will consider it just Markdown code and simply print it. If you want **both** to run and print the code, then add `:run` and `:echo` to the code declaration part.\n\nOnce you finished authoring you slideshow, simply run it just like before:\n\n```bash\nauditorium run <file.md>\n```\n\nIf you want to see an example, check [auditorium/static/md/demo.md](auditorium/static/md/demo.md)\n\n### Going full static\n\nIf you only need `auditorium` to generate the HTML, but have no interactive code whatsoever, you can also run:\n\n```bash\nauditorium render <file.[py|md]> > <output.html>\n```\n\nThis will render the slideshow in an HTML file with all CSS and JavaScript embedded. Just copy this single HTML file and open it on any browser. You won\'t need to have `auditorium` installed. However, do keep in mind that all of the backend code will execute only once for the initial rendering, so your animations will be frozen at the starting frame and none of the interaction will work.\n\n## What\'s the catch\n\nAuditorium covers a fairly simple use case that I haven\'t seen solved for a long time.\nI came up with this idea while trying to make better slideshows for my lectures at the University of Havana.\nI usually need to display complex math stuff and graphs, ideally animated, and sometimes make modifications on the fly according to the interaction with students.\nThey could ask how a function would look if some parameters where changed, etc.\n\nAlong that path I grew up from Power Point to JavaScript-based slides (like [reveal.sj](https://revealjs.com)) and sometimes even coded some simple behavior in JS, like changing a chart\'s parameters.\nHowever, for the most complex stuff I wanted to use Python, because otherwise I would need to redo a lot of coding in JS.\nFor example, I\'m teaching compilers now, and I want to show interactively how a parse tree is built for a regular expression.\nI simply cannot rewrite my regex engine in JS just for a slideshow.\n\nThen I discovered [streamlit](https://streamlit.io) and for a while tried to move my slides to streamlit format.\nStreamlit is awesome, but is aimed at a completely different use case.\nIt\'s quite cumbersome to force it to behave like a slideshow, the flow is not natural, and the styling options are very restrictive.\nOn the other hand, they handle a lot of complex scenarios which I simply don\'t need in a slideshow, like caching and a lot of magic with Pandas and Numpy.\nContrary to streamlit, I do want custom CSS and HTML to be easy to inject, because styling is very important in slides.\n\nSo I decided to write my own slideshow generator, just for my simple use cases.\nThat being said, there are some known deficiencies that I might fix, and some others which I probably will not, even in the long run.\n\n### Slides need to be fast\n\nA slide\'s code is executed completely every time that slide needs to be rendered.\nThat is, once during loading and then when inputs change or animations tick.\nHence, you slide logic should be fairly fast.\nThis is particularly true for animations, so don\'t expect to be able to train a neural network in real time.\nThe slide logic is meant to be simple, the kind of one-liners you can run every keystroke, like less than 1 second fast.\nIf you need to interactively draw the loss value of a neural network, either is gonna take a while or you will have to fake it, i.e., compute it offline and then simply animate it.\n\n### All slides are executed on load\n\nFor now, on the first load all slides are going to be run, which might increase significantly your loading time if you have complex logic in each slide.\nAt some point, if I run into the problem, I may add a "lazy" loading option so that only the first few slides are executed.\nIf this is an issue for a lot of people it might become a priority.\n\n### Slides have to be stateless\n\nThe code that runs inside a slide should not depend on anything outside of `ctx`, since you have no guarantee when will it be executed.\nRight now, slide\'s code is executed once before any rendering in order to discover vertical slides, then again during the\ninitial rendering to layout and then everytime an interaction or animation forces the slide to render again.\nHowever, this might be changed at any time, so make no assumptions as to when is that code executed.\nThe easiest way to do this, is making sure that every slide function is a pure function and all state is handled through\n`ctx` interactive items, such as `ctx.text_input`.\n\n### Watch out for code injection!\n\nIt is very tempting to do things like getting a text from an input box and passing it through `eval` in Python, so that you can render different functions interactively.\nAs long as you serve your presentations on `localhost` and show them yourself, feel free.\nHowever, beware when hosting presentations online.\nSince the backend code runs in your computer, a viewer could inject nasty stuff such as importing `os` and deleting your home folder! In the future I might add a `--safe` option that only allows for animations and other interactive behaviors that don\'t use input directly from the user.\nStaying away from `eval` and `exec` should keep you safe in most scenarios, but the basic suggestion is don\'t do anything you wouldn\'t do in a regular web application, since all security issues are the same.\n\n## History\n\n### v0.6.5\n\n* Improved compatibility for [Now](https://now.sh) static deployments.\n* The demo has now been moved to [auditorium-demo.now.sh](https://auditorium-demo.now.sh).\n\n### v0.6.4\n\n* New development environment completely based on Docker.\n* Added compatibility with Python 3.7 and 3.8.\n\n### v0.6.3\n\n* Added `Show.append` to append existing `show` instances or direct paths.\n* Fixed error with absolute path for the Markdown demo.\n* Append Markdown demo to the Python demo.\n\n### v0.6.2\n\n* Added `mypy` for some static type checking. Will slowly add as many type hints as possible.\n* Fixed dependency bugs when porting to `poetry`.\n\n### v0.6.1\n\n* Changed package manager to `poetry`.\n\n### v0.6.0\n\n* Completely redesigned API. Now slide functions receive a `ctx: Context` instance on which to call all the layout options. This detaches the `Show` instance from the slides code, which makes `Show` a stateless object and all slide functions side-effects are contained for each client.\n\n### v0.5.1\n\n* Added `pygments` for code highlighting, removing `highlight.js` and fixing the error with static rendering.\n\n### v0.5.0\n\n* Added command `auditorium render` to generate a static HTML that can be displayed without `auditorium`.\n\n### v0.4.5\n\n*  Fixed random order of vertical slides.\n\n### v0.4.4\n\n*  Changed the syntax for vertical slides, thanks to suggestions by [@tialpoy](https://www.reddit.com/user/tialpoy/).\n*  Added automatically launching browser on `auditorium run` and `... demo`. Override with `--launch=0`.\n*  Improved performance, now rendering only occurs at `show.run` or when changing the theme.\n\n### v0.4.3\n\n*  Improved test coverage a lot.\n\n### v0.4.2\n\n*  Added support for interpolating Python variables in Markdown mode.\n\n### v0.4.0\n\n*  Ported to Sanic 🤓!\n\n### v0.3.1\n\n*  Improved support for running Markdown.\n\n### v0.3.0\n\n*  Added support for running directly from Markdown files with `auditorium run <file.md>`.\n\n### v0.2.0\n\n*  Added command `auditorium run <file.py>` for running a specific slideshow. This is now the preferred method.\n*  Added command `auditorium demo` for running the demo.\n\n### v0.1.5\n\n*  Added support for `reveal.js` themes via `show.theme` and query-string argument `?theme=...`.\n*  Improved testing coverage.\n*  Fixed error with missing static files in the distribution package.\n\n### v0.1.3\n\n*  Added support for fragments.\n*  Added support for vertical slides.\n*  Added custom layout options with `show.columns`.\n*  Added styled block with `show.block`.\n*  Added parameter `language` for `show.code`, defaulting to `"python"`.\n*  Improved layout for columns, with horizontal centering.\n*  Improved layout for input texts.\n*  Improved example for the `pyplot` support in the demo.\n*  Fixed some style issues.\n*  Fixed error reloading on a slide with an animation.\n*  Updated Readme with some examples.\n\n### v0.1.2\n\n*  Refactor custom CSS and JavaScript into `auditorium.css` and `auditorium.js` respectively.\n\n### v0.1.1\n\n*  Added basic binding for variables.\n*  Added support for simple animations with `show.animation`.\n*  Added support for `pyplot` rendering.\n\n### v0.1.0\n\n*  Initial version with basic functionality.\n\n## Collaboration\n\nThis project uses a novel methodology for development, in which you only need [Docker installed](https://docs.docker.com/install/).\nFork the project, clone, and you\'ll find a `dockerfile` and `docker-compose.yml` files in the project root.\nWe provided [packaged testing environments](https://github.com/apiad/auditorium/packages) (in the form of Docker images) for all the Python versions we target.\nThere is also a `makefile` with all the necessary commands.\n\nThe workflow is something like this:\n* Fork, clone, and make some changes.\n* Run `make` to run the local, fast tests. The first time this will download the corresponding image.\n* Fix errors (if any) and watch the testing coverage. Make sure to at least cover the newly added features.\n* Run `make test-full` to run the local but long tests. This will download all the remaining images for each Python environment.\n* If all worked, push and pull-request.\n\nIf you need to tinker with the dev environment, `make shell` will open a shell inside the latest Python environment where you can run and test commands.\n\nThis project uses [poetry](https://python-poetry.org/) for package management. If you need to install new dependencies, run `make shell` and then `poetry add ...` inside the dockerized environment. Finally, don\'t forget to `poetry lock` and commit the changes to `pyproject.toml` and `poetry.lock` files.\n\n## License\n\nLicense is MIT, so you know the drill: fork, develop, add tests, pull request, rinse and repeat.\n\n> MIT License\n>\n> Copyright (c) 2019 Alejandro Piad, <https://apiad.net> and contributors.\n>\n> Permission is hereby granted, free of charge, to any person obtaining a copy\n> of this software and associated documentation files (the "Software"), to deal\n> in the Software without restriction, including without limitation the rights\n> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n> copies of the Software, and to permit persons to whom the Software is\n> furnished to do so, subject to the following conditions:\n>\n> The above copyright notice and this permission notice shall be included in all\n> copies or substantial portions of the Software.\n>\n> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n> SOFTWARE.\n\n### License for Reveal-js\n\n`auditorium` includes a copy a [reveal-js](https://revealjs.com) which is\nitself licensed under MIT.\n\n> Copyright (C) 2019 Hakim El Hattab, <http://hakim.se>, and reveal.js contributors.\n>\n> Permission is hereby granted, free of charge, to any person obtaining a copy\n> of this software and associated documentation files (the "Software"), to deal\n> in the Software without restriction, including without limitation the rights\n> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n> copies of the Software, and to permit persons to whom the Software is\n> furnished to do so, subject to the following conditions:\n>\n> The above copyright notice and this permission notice shall be included in\n> all copies or substantial portions of the Software.\n>\n> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n> THE SOFTWARE.\n',
    'author': 'Alejandro Piad',
    'author_email': 'alepiad@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
