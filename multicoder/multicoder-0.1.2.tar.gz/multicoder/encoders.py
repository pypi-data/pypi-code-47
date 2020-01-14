import base64
import email.encoders
import email.header
import functools
import hashlib
import html
import quopri
import shlex
import unicodedata
import urllib.parse
from typing import Callable, Optional, Iterable, Union

encoders = {}


class Encoder:
    def __init__(
            self,
            encode_name: str,
            encoder: Callable,
            help_text: Optional[str] = None,
            class_: str = None,
            binary_input: bool = False,
            binary_output: bool = False,
            decode_name: str = None,
            decoder: Optional[Callable] = None
    ):
        self.encode_name = encode_name
        self.decode_name = decode_name or encode_name
        self.encoder = encoder
        self.decoder = decoder
        self.help_text = help_text
        self.class_ = class_
        self.binary_input = binary_input
        self.binary_output = binary_output
        encoders[self.encode_name] = self

    def encode(self, message: str, encoding: str = "utf-8", normalization: Optional[str] = None) -> str:
        if normalization:
            message = unicodedata.normalize(normalization, message)
        if self.binary_input:
            message = message.encode(encoding)
        return self.encoder(message, encoding)

    def decode(self, message: str, encoding: str = "utf-8", normalization: Optional[str] = None) -> str:
        if normalization:
            message = unicodedata.normalize(normalization, message)
        if self.binary_output:
            message = message.encode(encoding)
        r = self.decoder(message, encoding)
        if self.binary_input:
            r = r.decode(encoding)
        return r


Encoder("email.header.Header",
        lambda message, enc: email.header.Header(message, charset=enc).encode(),
        decode_name="email.header.decode_header",
        decoder=lambda header, enc: "".join([x[0].decode(x[1]) if isinstance(x[0], bytes) else x[0] for x in email.header.decode_header(header)])
        )
Encoder(
    "quopri.encodestring",
    lambda message, enc: quopri.encodestring(message).decode("ascii"),
    binary_input=True,
    decode_name="quopri.decodestring",
    decoder=lambda message, enc: quopri.decodestring(message.encode("ascii"))
)
Encoder("urllib.parse.quote", lambda message, enc: urllib.parse.quote(message),
        decode_name="urllib.parse.unquote",
        decoder=lambda message, enc: urllib.parse.unquote(message),
        )
Encoder("urllib.parse.quote_plus", lambda message, enc: urllib.parse.quote_plus(message),
        decode_name="urllib.parse.unquote_plus",
        decoder=lambda message, enc: urllib.parse.unquote_plus(message),
        )
Encoder("html.escape", lambda message, enc: html.escape(message),
        decode_name="html.unescape",
        decoder=lambda message, enc: html.unescape(message)
        )
Encoder("shlex.quote", lambda message, enc: shlex.quote(message),
        )
Encoder(
    "base64.b64encode",
    lambda message, enc: base64.b64encode(message).decode("ascii"),
    decoder=lambda message, enc: base64.b64decode(message.encode("ascii")),
    binary_input=True,
)
Encoder(
    "base64.urlsafe_b64encode",
    lambda message, enc: base64.urlsafe_b64encode(message).decode("ascii"),
    decoder=lambda message, enc: base64.urlsafe_b64decode(message.encode("ascii")),
    binary_input=True,
)
Encoder(
    "base64.b32encode",
    lambda message, enc: base64.b32encode(message).decode(),
    binary_input=True,
)
Encoder(
    "base64.b16encode",
    lambda message, enc: base64.b16encode(message).decode(),
    binary_input=True,
)
Encoder(
    "base64.a85encode",
    lambda message, enc: base64.a85encode(message).decode(),
    binary_input=True,
)
Encoder(
    "base64.b85encode",
    lambda message, enc: base64.b85encode(message).decode(),
    binary_input=True,
)


def get_hashed_value(message: bytes, enc:str,  method: str = "md5") -> str:
    return getattr(hashlib, method)(message).hexdigest()


for m in sorted(hashlib.algorithms_guaranteed):
    if m not in {"shake_128", "shake_256"}:
        Encoder(
            "hashlib.%s" % m, functools.partial(get_hashed_value, method=m), binary_input=True
        )
# idna	 	Implements RFC 3490, see also encodings.idna
# mbcs	dbcs	Windows only: Encode operand according to the ANSI codepage (CP_ACP)
# palmos	 	Encoding of PalmOS 3.5
# punycode	 	Implements RFC 3492
# raw_unicode_escape	 	Produce a string that is suitable as raw Unicode literal in Python source code
# rot_13	rot13	Returns the Caesar-cypher encryption of the operand
# undefined	 	Raise an exception for all conversions. Can be used as the system encoding if no automatic coercion between byte and Unicode strings is desired.
# unicode_escape	 	Produce a string that is suitable as Unicode literal in Python source code
# unicode_internal
# hex_codec	hex	Convert operand to hexadecimal representation, with two digits per byte	binascii.b2a_hex(), binascii.a2b_hex()
# quopri_codec	quopri, quoted-printable, quotedprintable	Convert operand to MIME quoted printable	quopri.encode() with quotetabs=True, quopri.decode()
# string_escape	 	Produce a string that is suitable as string literal in Python source code
# uu_codec	uu	Convert the operand using uuencode	uu.encode(), uu.decode()
# zlib_codec	zip, zlib	Compress the operand using gzip	zlib.compress(), zlib.decompress()
# [1]	str object