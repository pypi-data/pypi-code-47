from aneki.parsers import Bash, AnekdotRu, Nekdo, ShytokNet
import random
import sys
import codecs


def print_anek():
    sources = [Bash(), AnekdotRu(), Nekdo(), ShytokNet()]
    text = -1
    max_tries = 5
    while text == -1 and max_tries > 0:
        parser_index = random.randint(0, len(sources) - 1)
        parser = sources[parser_index]
        text = parser.get_anek()
        max_tries -= 1
    if max_tries == 0:
        print('Сегодня Анеки в отпуске :(')
        print('Зайдите на https://github.com/VolkovAK/aneki, вдруг там что-то есть.')
        return 1
    else:
        print(text)
    return 0


def main(args=None):
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    if args is None:
        print_anek()
    else:
        print('ANEK TEST')


if __name__ == '__main__':
    main()
