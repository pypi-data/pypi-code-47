from __future__ import absolute_import

import sys

from simple_python_profiler import Profiler

if __name__ == '__main__':
    with Profiler():
        exec(open(sys.argv[1]).read(), globals())
