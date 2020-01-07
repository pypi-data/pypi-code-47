from aneki.parsers import Bash, AnekdotRu, Nekdo, ShytokNet
import random


class Aneki():
    def __init__(self):
        self.sources = [Bash(), AnekdotRu(), Nekdo(), ShytokNet()]

    def print_anek(self):
        anek = -1
        max_tries = 5
        while anek == -1 and max_tries > 0:
            parser_index = random.randint(0, len(self.sources) - 1)
            parser = self.sources[parser_index]
            anek = parser.get_anek()
            max_tries -= 1
        if anek == -1:
            print('Сегодня Анеки в отпуске :(')
            print('Зайдите на https://github.com/VolkovAK/aneki, вдруг там что-то есть.')
            return 1
        else:
            print(anek)
        return 0

    def test(self):
        print('Test sources availability:')
        for source in self.sources:
            print(source.get_name() + ':', end=' ')
            res = source.ping()
            if res:
                print('OK')
            else:
                print('ERROR')
        print('\nTest unicode:')
        try:
            print('Если вы это видите, то русские анекдоты тоже прочтете.')
            print('∃⛄: ∀❄: ∑❄ ≡ ☺')
        except UnicodeEncodeError as err:
            print('Oh no, unicode error:', err)
