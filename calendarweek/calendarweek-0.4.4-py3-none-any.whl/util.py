from locale import getpreferredencoding, locale_alias, locale_encoding_alias
from typing import Optional


def normalise_locale(loc: str, enc: Optional[str] = None) -> str:
    loc = locale_alias.get(loc, loc) or ""
    if loc:
        if enc:
            enc = locale_encoding_alias.get(enc.replace("-", ""), enc)
        else:
            enc = getpreferredencoding()
        loc = loc.split(".")[0] + "." + enc
    return loc
