"""A scanner generator that uses Jinja2 templates."""
import argparse
import sys
import jinja2
import scangen.internals as regexp

def from_class(cls):
    """Does not include token names that start with _."""
    keys = [k for k in cls.__dict__.keys() if k[0] != '_']
    return {k:cls.__dict__[k] for k in keys}

def convert(tokens):
    scanner = []
    for k, v in tokens.items():
        dfa = regexp.DFA(v)
        dfa.token = k
        scanner.append(dfa)
    return scanner

def generate(tokens, entrypoint="", directory=""):
    """Generate code from templates."""
    def get_args(args):
        description = "Generate scanner using jinja2 templates."
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("entrypoint", help="filename of template entrypoint")
        parser.add_argument("-d", default="", dest="directory",
                            help="path to templates directory")
        return parser.parse_args(args)

    def generate_code():
        loader = jinja2.FileSystemLoader(directory)
        env = jinja2.Environment(loader=loader)
        template = env.get_template(entrypoint)
        return template.render(scanners=convert(tokens))

    args = sys.argv[1:]
    if entrypoint:
        args.append(entrypoint)
    if directory:
        args.extend(["-d", directory])
    args = get_args(args)
    if args.entrypoint:
        entrypoint = args.entrypoint
    if args.directory:
        directory = args.directory

    try:
        output = generate_code()
        print(output)
    except jinja2.exceptions.TemplateNotFound:
        print("scangen: Template not found:", entrypoint)

name = "scangen"
