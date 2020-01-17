from . import pluralization_ranges

# Language code to rule number mapping
PLURALIZATION_BY_LANGUAGE = {
    "zh": 0,
    "ja": 0,
    "ko": 0,
    "fa": 0,
    "tr": 0,
    "th": 0,
    "lo": 0,
    "da": 1,
    "nl": 1,
    "en": 1,
    "fo": 1,
    "fy": 1,
    "stq": 1,
    "frr": 1,
    "de": 1,
    "no": 1,
    "sv": 1,
    "et": 1,
    "fi": 1,
    "hu": 1,
    "eu": 1,
    "el": 1,
    "he": 1,
    "it": 1,
    "pt": 1,
    "pt-pt": 1,
    "es": 1,
    "ca": 1,
    "vi": 1,
    "fr": 2,
    "pt-br": 2,
    "ln": 2,
    "lv": 3,
    "ltg": 3,
    "gd": 4,
    "ro": 5,
    "lt": 6,
    "be": 7,
    "ru": 7,
    "uk": 7,
    "sk": 8,
    "cs": 8,
    "pl": 9,
    "sl": 10,
    "dsb": 10,
    "hsb": 10,
    "ga": 11,
    "ar": 12,
    "mt": 13,
    "is": 15,
    "mk": 15,
    "br": 16,
    "jiv": 17,
    "cy": 18,
    "bs": 19,
    "hr": 19,
    "sr": 19,
}

# See the TestPluralizationFormNumbers class in tests/test_pluralization.py
# for descriptions of these rules and the returned forms.
FORMS_BY_RULE = {
    0: lambda c: 0,
    1: lambda c: 0 if c == 1 else 1,
    2: lambda c: 0 if c in [0, 1] else 1,
    3: lambda c: 0 if c == 0 else (1 if c == 1 else 2),
    4: lambda c: 0
    if c in [1, 11]
    else (
        1 if c in [2, 12] else (2 if c in pluralization_ranges.rule_4_range_2 else 3)
    ),
    5: lambda c: 0
    if c == 1
    else (1 if (c == 0 or (c % 100 in pluralization_ranges.rule_5_range_1)) else 2),
    6: lambda c: 1
    if ((c % 10 == 0) or (c % 100 in pluralization_ranges.rule_6_range_1))
    else (0 if c % 10 == 1 else 2),
    7: lambda c: 0
    if (c % 10 == 1 and c % 100 != 11)
    else (1 if c % 10 in [2, 3, 4] and c % 100 not in [12, 13, 14] else 2),
    8: lambda c: 0 if c == 1 else (1 if c in [2, 3, 4] else 2),
    9: lambda c: 0
    if c == 1
    else (1 if c % 10 in [2, 3, 4] and c % 100 not in [12, 13, 14] else 2),
    10: lambda c: 0
    if c % 100 == 1
    else (1 if c % 100 == 2 else (2 if c % 100 in [3, 4] else 3)),
    11: lambda c: 0
    if c == 1
    else (
        1
        if c == 2
        else (
            2
            if c in pluralization_ranges.rule_11_range_2
            else (3 if c in pluralization_ranges.rule_11_range_3 else 4)
        )
    ),
    12: lambda c: 5
    if c == 0
    else (
        0
        if c == 1
        else (
            1
            if c == 2
            else (
                2
                if c % 100 in pluralization_ranges.rule_12_range_2
                else (3 if c % 100 in [0, 1, 2] else 4)
            )
        )
    ),
    13: lambda c: 0
    if c == 1
    else (
        1
        if c == 0 or c % 100 in pluralization_ranges.rule_13_range_1
        else (2 if c % 100 in pluralization_ranges.rule_13_range_2 else 3)
    ),
    15: lambda c: 0 if (c % 10 == 1 and c % 100 != 11) else 1,
    16: lambda c: 0
    if (c % 10 == 1 and c % 100 not in [11, 71, 91])
    else (
        1
        if (c % 10 == 2 and c % 100 not in [12, 72, 92])
        else (
            2
            if (
                c % 10 in [3, 4, 9]
                and c % 100 not in pluralization_ranges.rule_16_exclude_range_2
            )
            else (3 if (c != 0 and c % 1_000_000 == 0) else 4)
        )
    ),
    17: lambda c: 0 if c == 0 else 1,
    18: lambda c: 0
    if c == 0
    else (1 if c == 1 else (2 if c == 2 else (3 if c == 3 else (4 if c == 6 else 5)))),
    19: lambda c: 0
    if (c % 10 == 1 and c % 100 != 11)
    else (1 if (c % 10 in [2, 3, 4] and c % 100 not in [12, 13, 14]) else 2),
}
