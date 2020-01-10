from aneki.core import Aneki
import sys
import codecs
import argparse


def main():
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

    parser = argparse.ArgumentParser(description='Let\'s get some jokes from the Internet')
    parser.add_argument('-t', '--test', help='test installation', action='store_true')
    args = parser.parse_args()

    aneki = Aneki()
    if args.test:
        aneki.test()
    else:
        aneki.print_anek()


if __name__ == '__main__':
    main()
