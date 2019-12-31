import datetime
import git
import os
import patoolib
import re
import string
import shutil
import urllib
import black
from colorama import Fore
from portmod.repo.download import (
    clobber_spaces,
    download,
    get_hash,
    get_filename,
    parse_arrow,
)
from portmod.repo.atom import Atom
from portmod.repo.loader import load_file, load_mod
from portmod.repo.metadata import get_categories
from portmod.repo.manifest import (
    create_manifest,
    get_manifest,
    Manifest,
    FileType,
    Hash,
    SHA512,
)
from portmod.log import err, warn
from portmod.prompt import prompt_bool
from portmod.colour import colour
from portmod.masters import get_masters
from portmod.repos import Repo
from portmod.globals import env
from portmod.main import configure_mods
from .util import clean_plugin, tr_patcher
from .sources.nexus import APILimitExceeded, get_nexus_info, validate_file
from .atom import parse_atom
from .datadir import find_esp_bsa, find_data_dirs, get_dominant_texture_size
from .deps import DependencyException, get_esp_deps


API_LIMIT_EXCEEDED = False

USER_REPO = Repo(
    "user-repo",
    os.path.join(env.PORTMOD_LOCAL_DIR, "user-repo"),
    False,
    None,
    None,
    ["openmw"],
    50,
)


def generate_build_files(mod, noreplace=False, allow_failures=False, validate=False):
    """
    Generates pybuilds from a mod decription dictionary.

    Valid Fields: atom, name, desc, homepage, category, url, file,
      author, needs_cleaning
    Other fields are ignored
    """
    clobber_spaces()

    todostr = "TODO: FILLME"
    if "atom" in mod:
        atom = Atom(mod["atom"])
    elif "category" in mod and "name" in mod:
        atom = parse_atom(mod["category"] + "/" + mod["name"])
    else:
        atom = None

    url = mod.get("url")
    if "file" in mod:
        file = os.path.expanduser(mod.get("file").replace(" ", "_"))
    else:
        file = None
    name = mod.get("name", None)
    desc = mod.get("desc", None) or mod.get("description", None)
    homepage = mod.get("homepage", None)
    author = mod.get("author")
    needs_cleaning = mod.get("needs_cleaning")

    sources = []
    source_string = url

    parsed = urllib.parse.urlparse(url)
    downloaded = False
    nexus_data = None
    REQUIRED_USE = []
    CLASS = ""
    OTHER_IMPORTS = ""
    OTHER_FIELDS = ""

    if parsed.hostname == "www.nexusmods.com":
        parsed = urllib.parse.urlparse(url)
        game = parsed.path.split("/")[1]
        mod_id = int(parsed.path.split("/")[3])

        # Get Nexus API data, but if we've exceeded out limit,
        # just print an error and return
        global API_LIMIT_EXCEEDED
        if API_LIMIT_EXCEEDED:
            return
        else:
            try:
                nexus_data = get_nexus_info(game, mod_id)
            except APILimitExceeded:
                err("Nexus API limit has been exceeded. Try again tomorrow")
                API_LIMIT_EXCEEDED = True
                return

        if nexus_data is not None:
            homepage = homepage or nexus_data.homepage
            name = name or nexus_data.name
            if not atom:
                atom = Atom(mod["category"] + "/" + nexus_data.atom)
            elif not atom.MV:
                atom = Atom(atom + "-" + nexus_data.atom.MV)
            desc = desc or nexus_data.desc

            if noreplace and len(load_mod(atom)) > 0:
                return

            if not all(
                [os.path.exists(get_filename(file)) for file in nexus_data.files]
            ):
                print("Please download the following files from the url at the bottom")
                print("before continuing and move them to the download directory:")
                print("  {}".format(env.DOWNLOAD_DIR))
                print()
                for source in nexus_data.files:
                    if not os.path.exists(get_filename(source)):
                        print("  {}".format(source))
                print()
                print("  {}?tab=files".format(nexus_data.homepage))
                if not prompt_bool("Continue?"):
                    return

                clobber_spaces()

            for file in nexus_data.files:
                if validate and not validate_file(game, mod_id, get_filename(file)):
                    raise Exception(f"File {file} has invalid hash!")

            url = None
            file = None
            downloaded = True
            sources = nexus_data.files
            source_string = " ".join(sources)
            if nexus_data.nudity:
                REQUIRED_USE.append("nudity")
            author = author or nexus_data.author
            OTHER_FIELDS += f'    NEXUS_URL = "{nexus_data.homepage}"\n'

    elif parsed.hostname == "mw.modhistory.com":
        homepage = url
        num = re.search(r"\d+$", url)[0]
        source_string = (
            f"http://mw.modhistory.com/file.php?id={num} -> {atom.C}_{atom.M}"
        )
        url = source_string
    elif parsed.hostname == "github.com" or parsed.hostname == "gitlab.com":
        source_string = ""
        CLASS += "Git,"
        OTHER_IMPORTS += "from pyclass.git import Git\n"
        OTHER_FIELDS += f'    GIT_SRC_URI = "{url}"\n'

        name, _ = os.path.splitext(os.path.basename(url))
        outdir = os.path.join(env.TMP_DIR, name)
        gitrepo = git.Repo.clone_from(url, outdir)
        date = datetime.date.fromtimestamp(gitrepo.head.commit.committed_date)
        print(date)
        atom = Atom(
            "{}-0_p{}{}{}".format(
                atom.CMN,
                str(date.year),
                str(date.month).zfill(2),
                str(date.day).zfill(2),
            )
        )
        OTHER_FIELDS += f'    GIT_COMMIT_DATE = "{date}"\n'
        shutil.rmtree(outdir)
        url = None
        downloaded = True
    elif (
        str(os.path.basename(parsed.path)).endswith(".php") and "->" not in url.split()
    ):
        source_string = url = f"{url} -> {atom.C}_{atom.M}"

    if noreplace and len(load_mod(atom)) > 0:
        return

    print("Importing {}...".format(atom))
    if url is not None:
        # We permit arrow notation in the url field
        for source in parse_arrow(url.split()):
            if not os.path.exists(get_filename(source.name)):
                download(source.url, source.name)
            sources.append(source.name)

    elif file is not None:
        download_name = os.path.basename(file).replace(" ", "_")
        shutil.copy(file, get_filename(download_name))
        sources.append(download_name)
        source_string = os.path.basename(file)
    elif not downloaded:
        raise Exception(
            "Please provide a download name or file name in the import configuration"
        )

    INSTALL_DIRS = []
    C = atom.C or mod.get("category")
    M = atom.M
    MN = atom.MN

    dir_data = {}
    dep_atoms = set()
    dep_uses = set()

    prepare = ""
    includes = ""

    cleanr = re.compile("<.*?>")
    if desc is not None:
        desc = re.sub(cleanr, "", desc)
        desc = desc.replace("\n", " ").replace("\r", " ").replace('"', '\\"')
    if author is not None:
        author = re.sub(cleanr, "", author)

    data_dirs = []

    for source in sources:
        # Extract file into tmp
        outdir = os.path.join(env.TMP_DIR, source)
        os.makedirs(outdir, exist_ok=True)
        patoolib.extract_archive(get_filename(source), outdir=outdir, interactive=False)

    for source in sources:
        # Search for data directories
        outdir = os.path.join(env.TMP_DIR, source)
        dirs = find_data_dirs(outdir)
        data_dirs.append((source, dirs))
        print(
            "Detected the following data directories for {}: {}".format(
                source, [dir.PATH for dir in dirs]
            )
        )

        for directory in dirs:
            (esps, bsas) = find_esp_bsa(os.path.join(outdir, directory.PATH))
            if bsas:
                bsa_string = ",ARCHIVES=[{}]".format(
                    ",".join(['File("{}")'.format(bsa) for bsa in bsas])
                )
            else:
                bsa_string = ""

            d_esps = []
            # Get dependencies for the ESP.
            # List dependencies common to all ESPs as deps for the mod
            for esp in esps:
                esp_path = os.path.join(outdir, directory.PATH, esp)
                print("Masters of esp {} are {}".format(esp, get_masters(esp_path)))
                if "TR_Data.esm" in get_masters(esp_path):
                    if not prepare:
                        prepare += "\n    def src_prepare(self):\n"
                    prepare += '        tr_patcher("{}")\n'.format(
                        os.path.normpath(os.path.join(source, directory.PATH, esp))
                    )
                    if "TRPatcher" not in OTHER_IMPORTS.split():
                        OTHER_IMPORTS += "from pyclass import TRPatcher\n"
                    if "TRPatcher" not in CLASS.split():
                        CLASS = "TRPatcher, " + CLASS
                    print("TR Patching file {}".format(esp))
                    tr_patcher(esp_path)

                try:
                    (dep_atom, dep_use) = get_esp_deps(
                        esp_path,
                        [
                            os.path.join(env.TMP_DIR, source, data_dir.PATH)
                            for (source, dirs) in data_dirs
                            for data_dir in dirs
                        ],
                        atom,
                    )
                    print(
                        'Found esp "{}" with deps of: {}'.format(
                            esp, dep_atom.union(dep_use)
                        )
                    )
                    d_esps.append(
                        {"esp": esp, "dep_atom": dep_atom, "dep_use": dep_use}
                    )
                    dep_atoms |= dep_atom
                    dep_uses |= dep_use
                except DependencyException as e:
                    warn("{}. Continuing anyway at user's request".format(e))

            dir_data[(source, directory.PATH)] = {
                "bsas": bsa_string,
                "esps": d_esps,
                "source": source,
            }

    if "base/morrowind" in dep_atoms and dep_uses:
        dep_atoms.remove("base/morrowind")
        dep_atoms.add("base/morrowind[" + ",".join(sorted(dep_uses)) + "]")

    deps = " ".join(sorted(dep_atoms))
    build_deps = set()

    # Install deps if the mods needs cleaning
    if needs_cleaning:
        configure_mods(dep_atoms, False, False, True, True, False, True, True, True)

    TEXTURE_SIZES = set()

    for (source, directories) in data_dirs:
        for directory in directories:
            d = dir_data[(source, directory.PATH)]
            bsa_string = d["bsas"]
            esps = d["esps"]
            source = d["source"]
            source_name, _ = os.path.splitext(source)
            if source_name.endswith(".tar"):
                source_name, _ = os.path.splitext(source_name)

            texture_size = get_dominant_texture_size(
                os.path.join(env.TMP_DIR, source, directory.PATH)
            )
            if texture_size:
                TEXTURE_SIZES.add(texture_size)

            if esps:
                esp_string = ",PLUGINS=["
                for esp in esps:
                    esp_string += '\n# Deps: {}\nFile("{}"),'.format(
                        " ".join(sorted(esp["dep_atom"] | esp["dep_use"])), esp["esp"]
                    )

                esp_string += "]"
            else:
                esp_string = ""

            for esp in esps:
                path = os.path.join(env.TMP_DIR, source, directory.PATH, esp["esp"])
                if needs_cleaning and clean_plugin(path):
                    sourcepath, _ = os.path.splitext(source)
                    if sourcepath.endswith(".tar"):
                        sourcepath, _ = os.path.splitext(source)
                    if "CleanPlugin" not in CLASS.split():
                        CLASS = "CleanPlugin, " + CLASS
                    if "CleanPlugin" not in OTHER_IMPORTS.split():
                        OTHER_IMPORTS += "from pyclass import CleanPlugin\n"
                    if not prepare:
                        prepare += "\n    def src_prepare(self):\n"
                    prepare += '        self.clean_plugin(f"{}/{}")\n'.format(
                        "{self.WORKDIR}",
                        os.path.normpath(
                            os.path.join(sourcepath, directory.PATH, esp["esp"])
                        ),
                    )
                    build_deps |= esp["dep_atom"]

            if directory.RENAME:
                RENAME_STR = ',RENAME="{}"'.format(directory.RENAME)
            else:
                RENAME_STR = ""
            DIR_NAME = directory.PATH
            if texture_size:
                texture_comment = f"\n# Texture Size: {texture_size}"
            else:
                texture_comment = ""
            if len(sources) > 1:
                INSTALL_DIRS.append(
                    string.Template(
                        """${texture_comment}
                        InstallDir("${DIR_NAME}"${bsa_string}${esp_string},
                            S="${source}"${RENAME_STR})
                        """
                    ).substitute(locals())
                )
            else:
                INSTALL_DIRS.append(
                    string.Template(
                        """${texture_comment}
                        InstallDir("${DIR_NAME}"${bsa_string}${esp_string}
                        ${RENAME_STR})
                        """
                    ).substitute(locals())
                )

    for source in sources:
        # Clean up files
        path = os.path.join(env.TMP_DIR, source)
        print(f"Cleaning up {path}")
        shutil.rmtree(path)

    install_dir_string = ",".join(INSTALL_DIRS)

    if nexus_data is not None:
        CLASS += "NexusMod,"
        OTHER_IMPORTS += "from pyclass import NexusMod\n"

    OTHER_IMPORTS += "\n"
    if REQUIRED_USE:
        REQUIRED_USE_STRING = 'REQUIRED_USE="' + " ".join(REQUIRED_USE) + '"\n'
    else:
        REQUIRED_USE_STRING = ""

    if build_deps:
        DEPEND = '\n    DEPEND="{}"'.format(" ".join(sorted(build_deps)))
    else:
        DEPEND = ""

    if TEXTURE_SIZES:
        OTHER_FIELDS += '    TEXTURE_SIZES = "{}"'.format(
            " ".join(map(str, sorted(TEXTURE_SIZES)))
        )

    build_file_str = string.Template(
        """# Copyright 2019 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

from portmod.pybuild import Pybuild1, InstallDir, File$includes
${OTHER_IMPORTS}

class Mod(${CLASS}Pybuild1):
    NAME="${name}"
    DESC="${desc}"
    HOMEPAGE="${homepage}"
    LICENSE="TODO: FILLME"
    RDEPEND="${deps}"${DEPEND}
    KEYWORDS="TODO: FILLME or Delete"
    SRC_URI="${source_string}"
${OTHER_FIELDS}
    INSTALL_DIRS=[${install_dir_string}]
    ${REQUIRED_USE_STRING}${prepare}
    """
    )

    build_file = build_file_str.substitute(locals())

    print("Formatting code...")
    build_file = black.format_str(build_file, mode=black.FileMode())

    # User import repo may not exist. If not, create it
    if not os.path.exists(USER_REPO.location):
        os.makedirs(os.path.join(USER_REPO.location, "profiles"), exist_ok=True)
        metadata_file = os.path.join(USER_REPO.location, "profiles", "repo_name")
        with open(metadata_file, "w") as file:
            print("user-repo", file=file)
        # Add user repo to REPOS so that it can be used in further dependency resolution
        env.REPOS.append(USER_REPO)
        # Write user import repo to repos.cfg
        with open(env.REPOS_FILE, "a") as file:
            userstring = """
[user]
location = {}
auto_sync = False
masters = openmw
priority = 50
"""
            print(userstring.format(USER_REPO.location), file=file)

    if C not in get_categories(USER_REPO.location):
        with open(
            os.path.join(USER_REPO.location, "profiles", "categories"), "a"
        ) as categories:
            print(C, file=categories)

    outdir = os.path.join(USER_REPO.location, C, MN)
    filename = os.path.join(outdir, M + ".pybuild")
    os.makedirs(outdir, exist_ok=True)

    build_files = [filename]

    print("Exporting pybuild to {}".format(filename))
    with open(filename, "w") as file:
        print(build_file, file=file)

    if parsed.hostname == "github.com" or parsed.hostname == "gitlab.com":
        # Create Live Pybuild
        OTHER_FIELDS = re.sub("GIT_COMMIT_DATE.*?\n", "", OTHER_FIELDS)
        live_file = build_file_str.substitute(locals())

        M = atom.MN + "-9999"
        filename = os.path.join(outdir, M + ".pybuild")
        build_files.append(filename)
        print("Exporting pybuild to {}".format(filename))
        with open(filename, "w") as file:
            print(live_file, file=file)

    # Add author to metadata.yaml if provided
    if author:
        create_metadata(os.path.join(outdir, "metadata.yaml"), author)

    # Create manifest file
    for filename in build_files:
        shasum = get_hash(filename)
        size = os.path.getsize(filename)
        # Start by storing the pybuild in the manifest so that we can load it
        manifest = get_manifest(filename)
        manifest.add_entry(
            Manifest(
                os.path.basename(filename),
                FileType.PYBUILD,
                size,
                [Hash(SHA512, shasum)],
            )
        )
        manifest.write()
        create_manifest(load_file(filename))

    print(colour(Fore.GREEN, "Finished Importing {}".format(atom)))


def create_metadata(file, author):
    with open(file, "w") as metadata:
        print("upstream:", file=metadata)
        print(f"    maintainer: !person {author}", file=metadata)
