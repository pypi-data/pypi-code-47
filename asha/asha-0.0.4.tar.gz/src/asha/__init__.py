#! /usr/bin/env python3

import rangeen
import sys
from .lib import Asha

def main():
    usage = rangeen.colorify(f'''
Usage:
-----
asha init - creates a new static site with default settings
asha install URL - fetch plugin or theme from URL and installs it
asha build - builds the static website
asha serve - serves the static site
    ''', fg=rangeen.colors.GREEN)
    if len(sys.argv) < 2 or sys.argv[1] not in ("init", "build", "install", "serve", "clean"):
        error_message = f'''
        Error! - Invalid usage see correct usage below
        {usage}
        '''
        print(rangeen.danger(error_message))
    else:
        command = sys.argv[1].lower()
        if command == "init":
            Asha._setup()
        elif command == "build":
            asha = Asha()
            asha._build()
        else:
            pass #implement later

if __name__ == '__main__':
    main()
