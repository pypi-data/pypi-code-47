# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pycubelut']
install_requires = \
['colour-science>=0.3.14,<0.4.0',
 'numpy==1.17.3',
 'pillow>=6.2.1,<7.0.0',
 'scipy>=1.4.1,<2.0.0']

entry_points = \
{'console_scripts': ['cubelut = pycubelut:main']}

setup_kwargs = {
    'name': 'pycubelut',
    'version': '0.2.2',
    'description': 'Tool for Applying Adobe Cube LUTs to Images',
    'long_description': '# pycubelut\n[![GitHub license](https://img.shields.io/github/license/yoonsikp/pycubelut.svg)](https://github.com/yoonsikp/pycubelut/blob/master/LICENSE)\n\nStop wasting time with sloppy \'gram filters, and use `pycubelut` to easily add that *pro* feel to your images!\n\n## Quick Start\nDownload one of many free `.cube` LUTs online \\[[1](https://luts.iwltbap.com/#freeware), [2](https://www.freepresets.com/product/free-luts-cali-vibes/)\\]. Then, run the following with your downloaded LUT and image.\n\n```\n$ sudo pip3 install pycubelut\n$ cubelut F-8700-V2-STD.cube P1040326.jpg -v\nINFO: Processing image: P1040326.jpg\nINFO: Completed in  6.71s\n```\n\n## Sample Image\n<p align="center">\n  <img src=https://github.com/yoonsikp/pycubelut/blob/master/sample.jpg?raw=true width=100%>\n</p>\n\n## Overview\nMany professionals apply 3D LUTs to obtain a certain look and feel to their images and videos, which is usually done with proprietary software such as Adobe Photoshop or Final Cut Pro. `pycubelut` was created to be the first easy to use, open-source, command-line tool to apply Adobe Cube LUTs to images.\n\nIn the context of images, a Lookup Table (LUT) is a table describing a transformation of RGB values. There are multiple types of LUTs used in image processing, most common being 1D LUTs and 3D LUTs. A 1D LUT contains an independent transformation for each colour channel, meaning there would be three 1D LUTs defined (for Red, Green, and Blue). However, a 3D LUT has every colour in RGB space directly mapped to another specified colour (\xe2\x84\x9d\xc2\xb3 -> \xe2\x84\x9d\xc2\xb3), allowing for powerful and arbitrary transformations, such as greyscale, false colour, and hue shifts. All colour effects, such as gamma, contrast, brightness, etc. can be encoded as a 3D LUT.\n\n3D LUTs are essentially grids in the shape of cubes (hence Adobe used `.cube` for their LUT file extension). In order to encode a lossless transformation of the complete 8 bit RGB space, 256x256x256 mappings are needed. However, the Cube format allows for interpolation of values from a LUT defined with fewer points, commonly 33x33x33 mappings.\n\n## Usage\nWarning: If your input image is in a Log colorspace, make sure to choose a Log LUT!\n```\n$ cubelut --help\nusage: cubelut [-h] [-o OUT] [-g] [-v] [-t [THUMB]] [-j JOBS] LUT INPUT\n\nTool for applying Adobe Cube LUTs to images\n\npositional arguments:\n  LUT                   Cube LUT filename/folder\n  INPUT                 input image filename/folder\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -o OUT, --out OUT     output image folder\n  -g, --log             convert to Log before LUT\n  -v, --verbose         control verbosity and info messages\n  -t [THUMB], --thumb [THUMB]\n                        resizes to <= 500px, optionally specify max size\n  -j JOBS, --jobs JOBS  number of processes to spawn, defaults to number of\n                        logical CPUs\n```\n\n### Multiple LUTs\nApplies all `.cube` files in the folder to the image(s)\n```\n$ cubelut ./my_luts/ P1040326.jpg -v\n```\n\n### Batch Image Processing\nProcesses all images in the input folder, and outputs to a specified folder\n```\n$ cubelut ./my_luts/ ./my_images/ -o ./new_images/ -v\n```\n\n### Thumbnail Mode\nResizes images for a huge speedup, useful for multiple LUTs\n```\n$ cubelut ./my_luts/ P1040326.jpg -v -t\n```\n',
    'author': 'Yoonsik Park',
    'author_email': 'park.yoonsik@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yoonsikp/pycubelut',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
