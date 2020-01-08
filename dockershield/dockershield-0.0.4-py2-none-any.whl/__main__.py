"""
    This is the entry point when you run python on this module as a directory
"""

import sys
import os

if __name__ == "__main__":
    # Need to patch the sys.path variable in order to deal with Python relative imports properly
    sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
    from dockershield.main import main
    sys.exit(main(sys.argv))
