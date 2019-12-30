from typing import Dict, NewType, Generic, TypeVar, Type, ItemsView, Tuple, Generator

Key = NewType('Key', str)
Lang = NewType('Lang', str)
Translation = NewType('Translation', str)
PLIndex = NewType('PLIndex', int)

KT = TypeVar('KT')
VT = TypeVar('VT')


class GenStorage(Generic[KT, VT]):
    def __init__(self, value_class: Type[VT]):
        self.dct: Dict[KT, VT] = {}
        self.value_class = value_class

    def __getitem__(self, item: KT) -> VT:
        if item not in self.dct:
            self.dct[item] = self.value_class()
        return self.dct[item]

    def __setitem__(self, key: KT, value: VT) -> None:
        self.dct[key] = value

    def __len__(self) -> int:
        return len(self.dct)

    def __contains__(self, item: KT) -> bool:
        return item in self.dct

    def items(self) -> ItemsView[KT, VT]:
        return self.dct.items()

    def key_sorted(self) -> Generator[Tuple[KT, VT], None, None]:
        for key in sorted(self.dct.keys()):
            yield key, self[key]


class Forms(GenStorage[PLIndex, Translation]):
    def __init__(self: 'Forms', value_class=Translation):
        super().__init__(value_class)


class Translations(GenStorage[Lang, Forms]):
    def __init__(self: 'Translations', value_class=Forms):
        super().__init__(value_class)

    def key_sorted(self) -> Generator[Tuple[Lang, Forms], None, None]:
        first_langs = [Lang(x) for x in ['en', 'en-GB', 'ru']]
        for key in first_langs:
            if key in self.dct:
                yield key, self[key]
        for k, v in self.dct.items():
            if k in first_langs:
                continue
            yield k, v


class Terms(GenStorage[Key, Translations]):
    def __init__(self, value_class=Translations):
        super().__init__(value_class)
