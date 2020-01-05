import os
import sys
from subprocess import Popen
from pervane import serve


def main(as_module=False):
    print('sys.argv', sys.argv)
    # Popen('python3 serve.py')
    serve.cli_main()


# if __name__ == "__main__":
#     main(as_module=True)
