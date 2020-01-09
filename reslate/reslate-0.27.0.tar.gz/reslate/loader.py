# pylint: disable=missing-docstring
import inspect
import os
import re
import sys

from . import CONFIG


def is_matching_file(f):
    files, patterns = CONFIG.exclude_files
    files_match = (f.endswith(".py") or f.endswith(".pyx")) and f not in files
    patterns_match = all(re.search(p, f) is None for p in patterns)
    return files_match and patterns_match


def is_matching_dir(d):
    dirs, patterns = CONFIG.exclude_pkgs
    dirs_match = d not in dirs
    patterns_match = all(re.search(p, d) is None for p in patterns)
    return dirs_match and patterns_match


def get_all_file_mappings():
    doc_api_path = os.path.join(CONFIG.docs, "api")
    if not os.path.isdir(doc_api_path):
        os.mkdir(doc_api_path)

    whole_walk = list(os.walk(CONFIG.source))
    src_walk = list(filter(lambda x: "__pycache__" not in x[0], whole_walk))

    subpkg_doc_files = []
    submod_doc_files = {}
    for root, dirs, files in src_walk:
        dd = os.path.normpath(root).split(os.sep)
        pkg_idx = dd.index(CONFIG.package_name)
        subpkg_unfolded = dd[pkg_idx:]

        try:
            dirs.remove("__pycache__")
        except ValueError:
            pass

        for d in dirs:
            if not is_matching_dir(d):
                continue

            spkg_name = ".".join(subpkg_unfolded) + (".%s" % d) + ".rst"

            doc_real_path = doc_api_path
            if len(subpkg_unfolded) > 1:
                for sub in subpkg_unfolded[1:]:
                    doc_real_path = os.path.join(doc_real_path, sub)

            subpkg_doc_files.append(
                os.path.normpath(os.path.join(doc_real_path, spkg_name))
            )

        for f in files:
            if not is_matching_file(f):
                continue

            # form the name of the corresponding doc file
            fname = f.split(".")[0]
            src_file = os.path.normpath(os.path.join(root, f))

            submod_name = ".".join(subpkg_unfolded) + (".%s" % fname) + ".rst"

            doc_real_path = doc_api_path
            if len(subpkg_unfolded) > 1:
                for sub in subpkg_unfolded[1:]:
                    doc_real_path = os.path.join(doc_real_path, sub)

            doc_file = os.path.join(doc_real_path, submod_name)

            submod_doc_files[src_file] = doc_file

    return subpkg_doc_files, submod_doc_files


def file_mappings(sources):
    subpkg_doc_files, submod_doc_files = get_all_file_mappings()
    mappings = {
        source: submod_doc_files[source]
        for source in sources
        if source in submod_doc_files
    }
    return subpkg_doc_files, mappings
