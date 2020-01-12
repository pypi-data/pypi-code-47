# License: MIT (expat)
#
# Copyright (c) 2020 Julien Lepiller <julien@lepiller.eu>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#####

# A dictionnary associating each language to a pair of lists: the first
# element is a list of quantities that correspond to English "one" and the
# second is a list of quantities that correspond to English "other".
#
# See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html
# for plural quantities.

zero = 'zero'
one = 'one'
two = 'two'
few = 'few'
many = 'many'
other = 'other'

# very common pattern
oo = [one, other]

# Some languages are not supported by Android yet, and others (commented out)
# are supported by Android, but not present on the above page. Help welcome
# if you speak these languages :)
language_map = {
  'af': oo,
  #'agq': [],
  'ak': oo,
  'am': oo,
  'an': oo,
  'ar': [zero, one, two, few, many, other],
  'ars': [zero, one, two, few, many, other],
  'as': oo,
  'asa': oo,
  'ast': oo,
  'az': oo,
  #'bas': [],
  'be': [one, few, many, other],
  'bem': oo,
  'bez': oo,
  'bg': oo,
  'bho': oo,
  'bm': [other],
  'bn': oo,
  'bo': [other],
  'br': [one, two, few, many, other],
  'brx': oo,
  'bs': [one, few, other],
  'ca': oo,
  'ce': oo,
  'ceb': oo,
  'cgg': oo,
  'chr': oo,
  'ckb': oo,
  'cs': [one, few, many, other],
  'cy': [zero, one, two, few, many, other],
  'da': oo,
  #'dav': [],
  'de': oo,
  #'dje': [],
  'dsb': [one, two, few, other],
  #'dua': [],
  'dv': oo,
  #'dyo': [],
  'dz': [other],
  #'ebu': [],
  'ee': oo,
  'el': oo,
  'en': oo,
  'eo': oo,
  'es': oo,
  'et': oo,
  'eu': oo,
  #'ewo': [],
  'fa': oo,
  'ff': oo,
  'fi': oo,
  'fil': oo,
  'fo': oo,
  'fr': oo,
  'fur': oo,
  'fy': oo,
  'ga': [one, two, few, many, other],
  'gd': [one, two, few, other],
  'gl': oo,
  'gsw': oo,
  'gu': [one, two, few, many, other],
  'guw': oo,
  #'guz': [],
  'gv': [one, two, few, many, other],
  'ha': oo,
  'haw': oo,
  'hi': [one, two, few, many, other],
  'hr': [one, few, other],
  'hsb': [one, two, few, other],
  'hu': oo,
  'hy': oo,
  'ia': oo,
  'iw': [one, two, many, other],
  'in': [other],
  'ig': [other],
  'ii': [other],
  'io': oo,
  'is': oo,
  'it': oo,
  'iu': [one, two, other],
  'ja': [other],
  'jbo': [other],
  'jgo': oo,
  'jmc': oo,
  'jv': [other],
  'ka': oo,
  'kab': oo,
  'kaj': oo,
  #'kam': [],
  'kcg': oo,
  'kde': [other],
  'kea': [other],
  #'khq': [],
  #'ki': [],
  'kk': oo,
  'kkj': oo,
  'kl': oo,
  #'kln': [],
  'km': [other],
  'kn': oo,
  'ko': [other],
  #'kok': [],
  'ks': oo,
  'ksb': oo,
  #'ksf': [],
  'ksh': [zero, one, other],
  'ku': oo,
  'kw': [zero, one, two, few, many, other],
  'ky': oo,
  'lag': [zero, one, other],
  'lb': oo,
  'lg': oo,
  'lkt': [other],
  'ln': oo,
  'lo': [other],
  'lt': [one, few, many, other],
  #'lu': [],
  #'luo': [],
  #'luy': [],
  'lv': [zero, one, other],
  'mas': oo,
  #'mer': [],
  #'mfe': [],
  'mg': oo,
  #'mgh': [],
  'mgo': oo,
  'mk': oo,
  'ml': oo,
  'mn': oo,
  'mr': [one, two, few, other],
  'ms': [other],
  'mt': [one, few, many, other],
  #'mua': [],
  'my': [other],
  'nah': oo,
  'naq': [one, two, other],
  'nb': oo,
  'nd': oo,
  'ne': oo,
  'nl': oo,
  #'nmg': [],
  'nn': oo,
  'nnh': oo,
  'nqo': oo,
  'nr': oo,
  'nso': oo,
  #'nus': [],
  'ny': oo,
  'nyn': oo,
  'om': oo,
  'or': oo,
  'os': oo,
  'osa': [other],
  'pa': oo,
  'pap': oo,
  'pl': [one, few, many, other],
  'pr': [zero, one, other],
  'ps': oo,
  'pt': oo,
  'rm': oo,
  #'rn': [],
  'ro': [one, few, other],
  'rof': oo,
  'ru': [one, few, many, other],
  #'rw': [],
  'rwk': oo,
  'sah': [other],
  'saq': oo,
  #'sbp': [],
  'sc': oo,
  'scn': oo,
  'sd': oo,
  'sdh': oo,
  'se': [one, two, other],
  'seh': [one, other],
  'ses': [other],
  'sg': [other],
  'shi': [one, few, other],
  'si': oo,
  'sk': [one, few, many, other],
  'sl': [one, two, few, other],
  'sma': [one, two, other],
  'smi': [one, two, other],
  'smj': [one, two, other],
  'smn': [other],
  'sms': [one, two, other],
  'sn': oo,
  'so': oo,
  'sq': oo,
  'sr': [one, few, other],
  'ss': oo,
  'ssy': oo,
  'st': oo,
  'su': [other],
  'sv': oo,
  'sw': oo,
  #'swc': [],
  'syr': oo,
  'ta': oo,
  'te': oo,
  'teo': oo,
  'th': [other],
  'ti': oo,
  'tig': oo,
  'tk': oo,
  'tn': oo,
  'to': [other],
  'tr': oo,
  'ts': oo,
  #'twq': [],
  'tzm': oo,
  'ug': oo,
  'uk': [one, few, many, other],
  'ur': oo,
  'uz': oo,
  #'vai': [],
  've': oo,
  'vi': oo,
  'vo': oo,
  'vun': oo,
  'wa': oo,
  'wae': oo,
  'wo': [other],
  'xog': oo,
  'xh': oo,
  #'yav': [],
  'yi': oo,
  'yo': [other],
  'yue': [other],
  #'zgh': [],
  'zh': [other],
  'zu': oo
}


def base_language(lang):
    return lang.split("-")[0]

def default_plural_from_english(eng, lang):
    try:
        qtt = language_map[lang]
    except:
        raise Exception('Unknown language {}'.format(lang))
    value = {}
    for quantity in qtt:
        if qtt == 'one':
            value[quantity] = eng['one']
        else:
            value[quantity] = eng['other']
    return value

def quantities_for_language(lang):
    try:
        return language_map[lang]
    except:
        raise Exception('Unknown language {}'.format(lang))
