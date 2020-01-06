#  Copyright (C) 2016-2020  Kyle.Hwang <upday7[at]163.com>
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version, with the additions
#  listed at the end of the accompanied license file.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  #
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  #
#  NOTE: This program is subject to certain additional terms pursuant to
#  Section 7 of the GNU Affero General Public License.  You should have
#  received a copy of these additional terms immediately following the
#  terms and conditions of the GNU Affero General Public License which
#  accompanied this program.
import re
from abc import abstractmethod
from typing import Type

from .exception import NoTranslationSegmentError
from .prviders.base_provider import BaseProvider
from .prviders.cn_bing import CNBing
from .prviders.cn_bing_s import CNBingSuggestion
from .prviders.collinsdictionary import CollinsWeb
from .prviders.lexico import Lexico
from .prviders.spanishdict import SpanishDict
from .prviders.urbandictionary import define
from .prviders.vocabulary_s import VocabularySuggestion
from .prviders.vocaublary import Vocabulary
from .prviders.youdao_ec import YoudaoEC


class DictionaryFactory:
    def __init__(self, dict_cls: Type[BaseProvider], word: str = ""):
        self.dict_cls = dict_cls
        self.word = word
        self._in_lang = None
        self._target_lang = None

    def __enter__(self, ):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    @property
    @abstractmethod
    def segment(self) -> str:
        ...

    @property
    @abstractmethod
    def lang_codes(self) -> dict:
        """
        {
            'es': 'spanish',
            'zh': 'chinese',
            'de': 'german',
            'fr': 'french',
            'en': 'english',
        }
        :return:
        """

    @property
    def provider(self) -> BaseProvider:
        return self.dict_cls(self.word, self.segment)

    def search(self, word: str, in_lang: str, target_lang: str) -> dict:
        self.word = word if word else self.word
        self._in_lang = in_lang
        self._target_lang = target_lang
        return self.provider.to_dict()


class OrphanDictionaryFactory(DictionaryFactory):
    @property
    def segment(self) -> str:
        return ""

    @property
    def lang_codes(self) -> dict:
        return {}

    def __init__(self, provider_cls, *, word: str = ""):
        self._provider_cls = provider_cls
        super(OrphanDictionaryFactory, self).__init__(self._provider_cls, word=word)

    def do_search(self, word: str = ""):
        return super(OrphanDictionaryFactory, self).search(word, "", "")


class CollinsDictionary(DictionaryFactory):
    lang_codes = {
        "es": "spanish",
        "zh": "chinese",
        "de": "german",
        "fr": "french",
        "en": "english",
    }

    @property
    def segment(self) -> str:
        if (
                self._in_lang not in self.lang_codes
                or self._target_lang not in self.lang_codes
        ):
            raise NoTranslationSegmentError(
                str(self._provider_cls), self._in_lang, self._target_lang
            )
        if self._in_lang != "en" and self._target_lang != "en":
            raise NoTranslationSegmentError(
                str(self._provider_cls), self._in_lang, self._target_lang
            )
        if self._in_lang == self._target_lang == "en":
            return "english"
        return f"{self.lang_codes[self._in_lang]}-{self.lang_codes[self._target_lang]}"

    def __init__(self, *, word: str = ""):
        self._provider_cls = CollinsWeb
        super(CollinsDictionary, self).__init__(self._provider_cls, word=word)

    def en2fr(self, word: str = ""):
        return self.search(word, "en", "fr")

    def en2es(self, word: str = ""):
        return self.search(word, "en", "es")

    def en2de(self, word: str = ""):
        return self.search(word, "en", "de")

    def en2zh(self, word: str = ""):
        return self.search(word, "en", "zh")

    def es2en(self, word: str = ""):
        return self.search(word, "es", "en")

    def fr2en(self, word: str = ""):
        return self.search(word, "fr", "en")

    def de2en(self, word: str = ""):
        return self.search(word, "de", "en")

    def zh2en(self, word: str = ""):
        return self.search(word, "zh", "en")

    def en(self, word: str = ""):
        return self.search(word, "en", "en")


class OxfordDictionary(DictionaryFactory):
    lang_codes = {
        "es": "spanish",
        "en": "english",
    }

    @property
    def segment(self) -> str:
        if (
                self._in_lang not in self.lang_codes
                or self._target_lang not in self.lang_codes
        ):
            raise NoTranslationSegmentError(
                str(self._provider_cls), self._in_lang, self._target_lang
            )
        if self._in_lang == self._target_lang:
            return self._in_lang

        return f"{self._in_lang}-{self._target_lang}"

    def __init__(self, *, word: str = ""):
        self._provider_cls = Lexico
        super(OxfordDictionary, self).__init__(self._provider_cls, word=word)

    def en2es(self, word: str = ""):
        return self.search(word, "en", "es")

    def es2en(self, word: str = ""):
        return self.search(word, "es", "en")

    def en(self, word: str = ""):
        return self.search(word, "en", "en")

    def es(self, word: str = ""):
        return self.search(word, "es", "es")


class VocabularyDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(VocabularyDictionary, self).__init__(Vocabulary, word=word)


class VocabularySuggestionDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(VocabularySuggestionDictionary, self).__init__(
            VocabularySuggestion, word=word
        )


class SpanishDictDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(SpanishDictDictionary, self).__init__(SpanishDict, word=word)


class CNBingDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(CNBingDictionary, self).__init__(CNBing, word=word)


class CNBingSuggestionDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(CNBingSuggestionDictionary, self).__init__(CNBingSuggestion, word=word)


class YoudaoDictionary(OrphanDictionaryFactory):
    def __init__(self, *, word: str = ""):
        super(YoudaoDictionary, self).__init__(YoudaoEC, word=word)


class UrbanDictionary:
    def __init__(self, word: str = ""):
        self.word = word

    def do_search(self, word: str = ""):
        if word:
            self.word = word
        ub = define(self.word)
        return {
            "definitions": [
                re.sub(
                    r"\s+", " ", d.definition.strip().replace("]", "").replace("[", "")
                )
                for d in ub
            ]
        }
