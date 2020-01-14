schizo_count = [
    "ноль",
    "целковый",
    "чекушка",
    "порнушка",
    "пердушка",
    "засерушка",
    "жучок",
    "мудачок",
    "хуй на воротничок",
    "дурачок"
]


class SchizoInt(int):
    def __init__(self):
        super().__init__()
        self.base = len(schizo_count)

    def __repr__(self):
        num = self.conjugate()
        res = []
        while True:
            r = num % self.base
            res.append(schizo_count[r])
            num //= self.base
            if num == 0:
                break
        return "-".join(res[::-1])
