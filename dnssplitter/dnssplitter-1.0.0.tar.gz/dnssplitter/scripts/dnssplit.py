import argparse
import sys
import dnssplitter

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("dns_names", type=str, nargs='+',
                        help="Domain name(s) to break down into parts")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    splitter = dnssplitter.DNSSplitter()
    splitter.init_tree(0)
    for name in args.dns_names:
        results = splitter.search_tree(name)
        print(name + ":")
        if results:
            print("  Prefix:    " + results[0])
            print("  Domain:    " + results[1])
            print("  Reg Point: " + results[2])
        else:
            print("  Error: failed to break the domain down (not a real name?)")
