from .json_data import tarot_skins, tarot_data, tarot_spreads


class Card:
    def __init__(self, data, set, card):
        self._data = data
        self._set = set
        self._card = card

    @property
    def name(self):
        return self._data.get("name") or "UNKNOWN NAME"

    @property
    def fields(self):
        all_fields = self._data.get("fields")
        all_fields = all_fields.copy() if all_fields is not None else {}
        return all_fields

    @property
    def formatted_fields(self):
        return "\n".join(["\"{}\"".format(f.capitalize()) for f in self.fields.keys()])

    @property
    def core_values(self):
        return [k for k in self.fields.keys()]

    def skin(self, name=None):
        return get_skin(self._set, self._card, name)


all_cards = {}

for k, v in tarot_data.items():
    for k2, c in v.items():
        C = Card(c, k, k2)
        all_cards[C.name.lower()] = C


def gen_deck():
    return list(all_cards.values())


def get_skin(set, card, name=None):
    try:
        s = tarot_skins[name][set][card]
        if not s:
            raise ValueError()
        else:
            return s
    except (KeyError, ValueError):
        return tarot_skins["default"][set][card]
