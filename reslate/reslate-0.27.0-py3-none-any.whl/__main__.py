import argparse
import difflib
import logging
import os
import sys
import yaml

from . import CONFIG

from .loader import file_mappings
from .parsing import Parser
from .writer import write


LOGGER = logging.getLogger(__name__)

_REPO_URL = "https://gitlab.com/sjrowlinson/reslate"
_PCC_RESLATE = {"repo": _REPO_URL, "rev": "1.0.0", "hooks": [{"id": "reslate"}]}


def write_config_file():
    cwd = os.getcwd()

    conf = os.path.join(cwd, ".reslate-config.yaml")
    if os.path.isfile(conf):
        os.remove(conf)

    root_name = os.path.normpath(cwd).split(os.sep)[-1].split("_")[0]
    dirs_in_cwd = list(filter(lambda x: os.path.isdir(x), os.listdir(cwd)))

    closest_to_rootname = difflib.get_close_matches(root_name, dirs_in_cwd, n=1)
    if not closest_to_rootname:
        LOGGER.warn(
            "Unable to determine package_source_path. Please set this "
            "field manually in .reslate-config.yaml"
        )
        relative_source_path = ""
    else:
        relative_source_path = closest_to_rootname[0]

    closest_to_docs = difflib.get_close_matches("docs", dirs_in_cwd, n=1)
    if not closest_to_rootname:
        LOGGER.warn(
            "Unable to determine docs_source_path. Please set this "
            "field manually in .reslate-config.yaml"
        )
        relative_docs_src_path = ""
    else:
        relative_docs_path = closest_to_docs[0]

        docs_path = os.path.join(cwd, relative_docs_path)

        dirs_in_docs = list(
            filter(
                lambda x: os.path.isdir(os.path.abspath(os.path.join(docs_path, x))),
                os.listdir(docs_path),
            )
        )
        if "source" in dirs_in_docs:
            relative_docs_src_path = os.path.join(relative_docs_path, "source")
        elif "src" in dirs_in_docs:
            relative_docs_src_path = os.path.join(relative_docs_path, "src")
        else:
            relative_docs_src_path = relative_docs_path

    contents = r"""
# path to package source code relative to package root
package_source_path: %s

# path to package documentation source relative to package root
docs_source_path: %s

# files and patterns to exclude from documenting
exclude:
    files: ['^_', '^\.', 'version', 'test']
    subpkgs: ['^_', '^\.', version', 'test']

    classes: []
    enums: []
    dataclasses: []
    methods: []
    functions: []
    """ % (
        relative_source_path,
        relative_docs_src_path,
    )

    with open(conf, "w") as f:
        f.write(contents.strip() + "\n")


def load_config_file():
    cwd = os.getcwd()

    conf = os.path.join(cwd, ".reslate-config.yaml")
    if not os.path.isfile(conf):
        LOGGER.error("Could not find .reslate-config.yaml file!")
        return None

    with open(conf, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as ex:
            LOGGER.error(
                "Unable to load .reslate-config.yaml file, the "
                "following error occurred:\n\t%s" % str(ex)
            )
            return None


def _check_pre_commit_config_file(pcc):
    with open(pcc, "r") as f:
        try:
            pcc_load = yaml.safe_load(f)
        except yaml.YAMLError as ex:
            LOGGER.error(
                "Unable to load .pre-commit-config.yaml file, the "
                "following error occurred:\n\t%s" % str(ex)
            )
            return False, False, None

        repos = pcc_load.get("repos", [])
        reslate_repo_entry = list(
            filter(lambda x: "repo" in x and x["repo"] == _REPO_URL, repos)
        )
        if reslate_repo_entry:
            reslate_in_repos = True
            reslate_repo = reslate_repo_entry[0]
            rev_correct = reslate_repo["rev"] == _PCC_RESLATE["rev"]
            hooks_correct = reslate_repo["hooks"] == _PCC_RESLATE["hooks"]

            if not rev_correct or not hooks_correct:
                pcc_load["repos"].remove(reslate_repo)
                reslate_in_repos = False
        else:
            reslate_in_repos = False

    return "repos" not in pcc_load, not reslate_in_repos, pcc_load


def write_pre_commit_config_file():
    cwd = os.getcwd()

    pcc = os.path.join(cwd, ".pre-commit-config.yaml")

    if os.path.isfile(pcc):
        make_repos, make_reslate, pcc_load = _check_pre_commit_config_file(pcc)
        if pcc_load is None:
            return -1

        if make_repos:
            pcc_load["repos"] = []

        if make_reslate:
            pcc_load["repos"].append(_PCC_RESLATE)
        else:
            return 0
    else:
        pcc_load = {"repos": [_PCC_RESLATE]}

    with open(pcc, "w+") as f:
        yaml.dump(pcc_load, f)

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Generate and update API documentation."
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        return 0

    parser.add_argument(
        "sources",
        nargs="*",
        help="Source files of package to generate / update API "
        "documentation pages from.",
    )

    parser.add_argument(
        "--init",
        dest="initialise",
        action="store_true",
        help="Initialise reslate for the current working directory. Note that "
        "the current working directory should be the root directory of your "
        "local copy of your package repository.",
        default=False,
    )

    # parse the args provided into a Namespace
    args = parser.parse_args()

    if args.initialise:
        err = write_pre_commit_config_file()
        if err:
            return err

        write_config_file()

    config = load_config_file()
    if config is None:
        return -1

    CONFIG.source = config["package_source_path"]
    CONFIG.docs = config["docs_source_path"]

    exclude = config.get("exclude", {})
    CONFIG.exclude_files = exclude.get("files", [])
    CONFIG.exclude_pkgs = exclude.get("subpkgs", [])
    CONFIG.exclude_classes = exclude.get("classes", [])
    CONFIG.exclude_enums = exclude.get("enums", [])
    CONFIG.exclude_dataclasses = exclude.get("dataclasses", [])
    CONFIG.exclude_methods = exclude.get("methods", [])
    CONFIG.exclude_functions = exclude.get("functions", [])

    if not args.sources:
        return 0

    sources = []
    for src in args.sources:
        src = os.path.abspath(src)
        if os.path.isfile(src) and (src.endswith(".py") or src.endswith(".pyx")):
            sources.append(src)
        elif os.path.isdir(src):
            for root, _, files in os.walk(src):
                for f in files:
                    if f.endswith(".py") or f.endswith(".pyx"):
                        af = os.path.abspath(os.path.join(root, f))
                        sources.append(af)
        else:
            LOGGER.warn(
                "Ignoring file / directory: %s passed to sources as "
                "it does not exist." % src
            )

    subpkg_doc_files, submod_doc_files = file_mappings(sources)

    map_sfi_to_docfile = {}
    for src, docfile in submod_doc_files.items():
        p = Parser(src)
        map_sfi_to_docfile[p.parse()] = docfile

    write(subpkg_doc_files, map_sfi_to_docfile)


if __name__ == "__main__":
    exit(main())
