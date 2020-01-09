#!/usr/bin/python
# -*- coding: utf-8 -*-

from cryptos import *
from wicc.language import Language


def random_words(language: Language=Language.English):
    return entropy_to_words(os.urandom(16), language_words_list(language=language))


def language_words_list(language: Language):
    if language.name == Language.French.name:
        from wicc.cryptos.words_fr import words_list
        return words_list
    elif language.name == Language.Spanish.name:
        from wicc.cryptos.words_es import words_list
        return words_list
    elif language.name == Language.Italian.name:
        from wicc.cryptos.words_it import words_list
        return words_list
    elif language.name == Language.Korean.name:
        from wicc.cryptos.words_ko import words_list
        return words_list
    elif language.name == Language.Japanese.name:
        from wicc.cryptos.words_jp import words_list
        return words_list
    elif language.name == Language.Simplified_Chinese.name:
        from wicc.cryptos.words_zh_hans import words_list
        return words_list
    else:
        from wicc.cryptos.words_en import words_list
        return words_list


def to_en_mnemonic_string(language: Language, mnemonic):
    if language == Language.English:
        return mnemonic
    target_words = []
    en_words_list = language_words_list(language=Language.English)
    words_list = language_words_list(language=language)
    for word in mnemonic.split(" "):
        for (index, word_in) in enumerate(words_list):
            if word == word_in:
                target_words.append(en_words_list[index])
    print(target_words)
    return " ".join(target_words)

