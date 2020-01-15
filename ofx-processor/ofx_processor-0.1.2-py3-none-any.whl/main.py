import os
import re
from xml.etree import ElementTree

import click
from ofxtools.Parser import OFXTree
from ofxtools.header import make_header


@click.command()
@click.argument("ofx_file")
def cli(ofx_file):
    parser = OFXTree()
    try:
        parser.parse(ofx_file)
    except FileNotFoundError:
        print("Couldn't open ofx file")
        return

    ofx = parser.convert()

    if ofx is None:
        print("Couldn't open ofx file")
        return
    for transaction in ofx.statements[0].transactions:
        if "CB****" in transaction.name:
            print("Found following transaction:")
            print("Name")
            print(transaction.name)
            print("Memo")
            print(transaction.memo)

            name = transaction.name
            memo = transaction.memo
            conversion = re.compile(r"\d+,\d{2}[a-zA-Z]{3}")
            match = conversion.search(memo)
            if match:
                transaction.name = memo[: match.start() - 1]
                transaction.memo = name + memo[match.start() - 1 :]
            else:
                transaction.name = memo
                transaction.memo = name

            print("\nMapping to:")
            print("Name (should not contain CB****)")
            print(transaction.name)
            print("Memo")
            print(transaction.memo)
            print()

    header = str(make_header(version=102))
    root = ofx.to_etree()
    data = ElementTree.tostring(root).decode()

    with open(os.path.join(os.path.dirname(ofx_file), "processed.ofx"), "w") as f:
        f.write(header + data)


if __name__ == "__main__":
    cli()
