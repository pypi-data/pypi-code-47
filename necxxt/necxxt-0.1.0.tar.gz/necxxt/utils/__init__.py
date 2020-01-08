import json
import os


def listCompilers():
    compilers = []

    for path in os.environ["PATH"].split(os.pathsep):
        compilers.extend(
            listFiles(path, filters=["clang++", "g++"], shorten=False))

    return compilers


def listFiles(d, filters=[], shorten=True):
    fs = []

    for path, subdirs, files in os.walk(d):
        for name in files:
            add = False
            if len(filters) == 0:
                add = True
            else:
                for f in filters:
                    if name.endswith(f):
                        add = True

            if add:
                p = os.path.join(path, name)
                if shorten:
                    fs.append(os.path.relpath(p, d))
                else:
                    fs.append(p)

    return fs


def readModule(dependency=None):
    if dependency:
        module_file = os.path.join(
            os.getcwd(), "necxxt_modules", dependency, "necxxt.json")
    else:
        module_file = os.path.join(os.getcwd(), "necxxt.json")

    if not os.path.isfile(module_file):
        print("ENOENT: no such file or directory, open '{}'".format(module_file))
        exit(1)

    module = {}
    with open(module_file, "r") as f:
        module = json.load(f)

    return module
