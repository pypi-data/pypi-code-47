import os

def main(as_module=False):
    # TODO omit sys.argv once https://github.com/pallets/click/issues/536 is fixed
    exec('python3 serve.py')


if __name__ == "__main__":
    main(as_module=True)