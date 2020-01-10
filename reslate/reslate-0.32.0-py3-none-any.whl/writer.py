import os
import re
import sys

from .loader import is_matching_file, is_matching_dir
from .parsing import SourceFileInfo
from . import templates
from . import CONFIG


def write(subpkg_doc_files: dict, submod_doc_files: dict):
    exit_val = 0
    for subpkg_dir, subpkg_doc_file in subpkg_doc_files.items():
        if os.path.isfile(subpkg_doc_file):
            # TODO complicated stuff
            continue

        name = subpkg_doc_file.split(os.sep)[-1].replace(".rst", "")
        all_items = os.listdir(subpkg_dir)
        submodules = _filter_submodules(all_items, subpkg_dir)

        contents = templates.load.make_subpkg_overview(name, submodules)

        with open(subpkg_doc_file, "w+") as f:
            f.write(_format_writable(contents))

        exit_val = 1

    for sfi, doc_file in submod_doc_files.items():
        exit_val = _manipulate_doc_file(doc_file, sfi)

    return exit_val


def _filter_submodules(items, subpkg_dir):
    submods = []

    for item in items:
        if item == "__pycache__":
            continue

        path = os.path.join(subpkg_dir, item)
        dd = os.path.normpath(path).split(os.sep)
        pkg_idx = dd.index(CONFIG.package_name)
        if CONFIG.package_name in dd[pkg_idx:]:
            pkg_idx += 1 + dd[pkg_idx:].index(CONFIG.package_name)
        subpkg_unfolded = dd[pkg_idx:]

        if os.path.isdir(path) and is_matching_dir(item):
            sub_items = os.listdir(path)
            if "__init__.py" in sub_items:
                submods.append(".".join(subpkg_unfolded))
        else:
            if is_matching_file(item):
                if subpkg_unfolded[-1].endswith(".py"):
                    subpkg_unfolded[-1] = subpkg_unfolded[-1].replace(".py", "")
                elif subpkg_unfolded[-1].endswith(".pyx"):
                    subpkg_unfolded[-1] = subpkg_unfolded[-1].replace(".pyx", "")

                submods.append(".".join(subpkg_unfolded))

    submods.sort()
    return submods


def _format_writable(contents: str):
    contents = contents.strip()
    return re.sub(r"\n\s*\n", "\n\n", contents) + "\n"


def _manipulate_doc_file(doc_file, sfi: SourceFileInfo):
    # recursively make all directories up to doc_file if they don't exist already
    os.makedirs(os.path.dirname(doc_file), exist_ok=True)

    public_objs = sfi.public()
    if not public_objs and not sfi.public("functions"):
        # TODO write doc file with contents as just title and .. automodule:: {modname}
        return 0

    return _multiobj_handler(doc_file, sfi, public_objs)


def _multiobj_handler(doc_file: str, sfi: SourceFileInfo, objs: dict):
    exit_val = 0

    leading_dir, fname = os.path.split(doc_file)
    new_dirname = fname.split(".")[-2]

    # Write the module level doc file first
    if os.path.isfile(doc_file):
        # TODO complicated stuff
        pass
    else:
        name = fname.replace(".rst", "")
        classes = list(objs.get("classes", {}).keys())
        dataclasses = list(objs.get("dataclasses", {}).keys())
        enums = list(objs.get("enums", {}).keys())
        functions = list(sfi.public("functions").keys())

        contents = templates.load.make_multiclass_header(
            name, name, new_dirname, classes, dataclasses, enums, functions,
        )
        with open(doc_file, "w+") as f:
            f.write(_format_writable(contents))

        exit_val = 1

    # Now write all the sub doc files from all the objects
    # that exist within this module - creating a directory
    # with module name if it doesn't already exist
    full_new_dirname = os.path.join(leading_dir, new_dirname)
    if not os.path.isdir(full_new_dirname):
        os.mkdir(full_new_dirname)

    for obj_type, objects in objs.items():
        for obj in objects:  # NOTE: obj is the object name
            new_fname = ".".join(fname.split(".")[:-1]) + (".%s.rst" % obj)
            fpath = os.path.join(leading_dir, os.path.join(new_dirname, new_fname))

            if os.path.isfile(fpath):
                # TODO complicated stuff
                continue

            name = new_fname.replace(".rst", "")
            mod_name = fname.replace(".rst", "")

            if obj_type == "classes":
                cd = sfi.get_class_data(obj)

                constructor = None if cd.constructor is None else cd.constructor[0]
                properties = list(cd.properties.keys())
                methods = list(cd.methods.keys())
            else:
                constructor = None
                properties = []
                methods = []

            contents = templates.load.make_singleobj_header(
                name, mod_name, obj, properties, methods, constructor,
            )

            with open(fpath, "w+") as f:
                f.write(_format_writable(contents))

            exit_val = 1

    return exit_val
