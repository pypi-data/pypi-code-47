import argparse
from typing import Iterable, Optional, Tuple

from multicoder.encoders import encoders

__author__ = "flanker"

__all__ = ["main", "decode_text", "encode_text"]


def decode_text(
        message, encoding: str = "utf-8", normalization: Optional[str] = None
) -> Iterable[Tuple[str, str]]:
    for encoder in encoders.values():
        if encoder.decoder is None:
            continue
        try:
            decoded_message = encoder.decode(
                message, encoding, normalization=normalization
            )
        except Exception as e:
            decoded_message = "(invalid: %s )" % e
        yield encoder.decode_name, decoded_message


def encode_text(
        message: str, encoding: str = "utf-8", normalization: Optional[str] = None
) -> Iterable[Tuple[str, str]]:
    for encoder in encoders.values():
        try:
            encoded_message = encoder.encode(
                message, encoding=encoding, normalization=normalization
            )
        except Exception as e:
            encoded_message = "(invalid: %s )" % e
        yield encoder.encode_name, encoded_message


def main(args=None):
    parser = argparse.ArgumentParser(description="Test classical encodings")
    parser.add_argument("-o",
        "--output", help="only display encodings that return this text", default=None
    )
    parser.add_argument(
        "-r",
        "--reverse",
        help="decode the provided text instead encoding it",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--new-line",
        help="also try with an ending new line",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-N",
        "--normalization",
        default=None,
        choices=("NFC", "NFKC", "NFD", "NFKD"),
        help="normalize the Unicode representation before encoding",
    )
    parser.add_argument(
        "-e",
        "--encoding",
        default="utf-8",
        help="encoding to use for binary representations",
    )
    parser.add_argument("text", help="text to encode")
    args = parser.parse_args(args)

    src_texts = [args.text]
    if args.new_line:
        src_texts.append(args.text + "\n")
    for src_text in src_texts:
        dst_text = args.output
        fn = decode_text if args.reverse else encode_text
        for name, msg in fn(src_text, encoding=args.encoding, normalization=args.normalization):
            if dst_text is None or msg == dst_text:
                print("%s : %s" % (name, msg))


if __name__ == "__main__":
    main()
