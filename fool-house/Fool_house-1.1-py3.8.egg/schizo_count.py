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


def from_int_to_schizo_str(num):
    base = len(schizo_count)  # 10 digits
    res = []
    for ch in str(num):
        res.append(schizo_count[int(ch, base)])
    return "-".join(res)
