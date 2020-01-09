import os
import re
import sys

from .parsing import SourceFileInfo
from . import templates


def write(subpkg_doc_files, submod_doc_files):
    for subpkg_doc_file in subpkg_doc_files:
        if os.path.isfile(subpkg_doc_file):
            continue

        name = subpkg_doc_file.split(os.sep)[-1].replace(".rst", "")
        contents = templates.load.make_subpkg_overview(name)

        with open(subpkg_doc_file, "w+") as f:
            f.write(_format_writable(contents))

    for sfi, doc_file in submod_doc_files.items():
        _manipulate_doc_file(doc_file, sfi)


def _format_writable(contents: str):
    contents = contents.strip()
    return re.sub(r"\n\s*\n", "\n\n", contents) + "\n"


def _manipulate_doc_file(doc_file, sfi: SourceFileInfo):
    # recursively make all directories up to doc_file if they don't exist already
    os.makedirs(os.path.dirname(doc_file), exist_ok=True)

    public_classes = sfi.public("classes")
    if len(public_classes) > 1:
        _multiclass_handler(doc_file, sfi, public_classes)
    else:
        if os.path.isfile(doc_file):
            # TODO complicated stuff
            return

        _, fname = os.path.split(doc_file)
        name = fname.replace(".rst", "")
        if not public_classes:
            cls_name = None
            cls_props = []
            cls_meths = []
            cls_init = None
        else:
            cls_name = list(public_classes.keys())[0]
            class_data = sfi.get_class_data(cls_name)

            cls_init = (
                None if class_data.constructor is None else class_data.constructor[0]
            )
            cls_props = list(class_data.properties.keys())
            cls_meths = list(class_data.methods.keys())

        contents = templates.load.make_simplemod_header(
            name,
            name,
            cls_name,
            cls_props,
            cls_meths,
            cls_init,
            list(sfi.functions.keys()),
        )

        with open(doc_file, "w+") as f:
            f.write(_format_writable(contents))


def _multiclass_handler(doc_file, sfi, classes):
    leading_dir, fname = os.path.split(doc_file)
    new_dirname = fname.split(".")[-2]

    full_new_dirname = os.path.join(leading_dir, new_dirname)
    if not os.path.isdir(full_new_dirname):
        os.mkdir(full_new_dirname)

    for pclass in classes:
        class_data = sfi.get_class_data(pclass)

        new_fname = ".".join(fname.split(".")[:-1]) + (".%s.rst" % pclass)
        fpath = os.path.join(leading_dir, os.path.join(new_dirname, new_fname))

        if os.path.isfile(fpath):
            # TODO complicated stuff
            continue

        with open(fpath, "w+") as f:
            name = new_fname.replace(".rst", "")
            mod_name = fname.replace(".rst", "")
            # FIXME: some issues here with properties / methods duplication
            cd_constructor = (
                None if class_data.constructor is None else class_data.constructor[0]
            )
            contents = templates.load.make_singleclass_header(
                name,
                mod_name,
                class_data.name,
                list(class_data.properties.keys()),
                list(class_data.methods.keys()),
                cd_constructor,
            )

            f.write(_format_writable(contents))

    if os.path.isfile(doc_file):
        # TODO complicated stuff
        return

    with open(doc_file, "w+") as f:
        name = fname.replace(".rst", "")
        contents = templates.load.make_multiclass_header(
            name, name, new_dirname, list(classes.keys()), list(sfi.functions.keys())
        )

        f.write(_format_writable(contents))
