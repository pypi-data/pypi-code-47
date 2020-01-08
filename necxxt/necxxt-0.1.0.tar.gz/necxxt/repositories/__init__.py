import io
import json
import os
import pathlib
import shutil
import urllib.request
import zipfile


class Repository:
    def __init__(self, name, version):
        self._name = name
        self._version = version

    def readLocalModule(self):
        module_file = os.path.join("necxxt_modules", self._name, "necxxt.json")
        with open(module_file, "r") as f:
            return json.load(f)

    def readModule(self):
        pass

    def install(self):
        pass

    def __repr__(self):
        return None

    def __str__(self):
        return self.__repr__()


class RepositoryDirectory(Repository):
    def readModule(self):
        module_file = os.path.join(self._version, "necxxt.json")
        with open(module_file, "r") as f:
            return json.load(f)

    def install(self):
        pathlib.Path("necxxt_modules").mkdir(parents=True, exist_ok=True)

        if os.path.isdir(os.path.join("necxxt_modules", self._name)):
            shutil.rmtree(os.path.join("necxxt_modules", self._name))

        shutil.copytree(self._version, os.path.join(
            "necxxt_modules", self._name))

    def __repr__(self):
        return self._version


class RepositoryGitHub(Repository):
    def readModule(self):
        url = "https://raw.githubusercontent.com/necxxt/{}/master/necxxt.json".format(
            self._name)
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            data = response.read()
            encoding = response.info().get_content_charset("utf-8")
            return json.loads(data.decode(encoding))

    def install(self):
        url = str(self)
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            data = response.read()
            z = zipfile.ZipFile(io.BytesIO(data))

            if os.path.isdir(os.path.join("necxxt_modules", self._name)):
                shutil.rmtree(os.path.join("necxxt_modules", self._name))

            if os.path.isdir(os.path.join("necxxt_modules", "{}-master".format(self._name))):
                shutil.rmtree(os.path.join("necxxt_modules",
                                           "{}-master".format(self._name)))

            z.extractall("necxxt_modules")

            shutil.move(os.path.join("necxxt_modules", "{}-master".format(self._name)),
                        os.path.join("necxxt_modules", self._name))

    def __repr__(self):
        return "https://github.com/necxxt/{}/archive/master.zip".format(self._name)


def resolveRepository(name, version):
    if os.path.isdir(version):
        return RepositoryDirectory(name, version)
    elif isHostedOnGitHub(name):
        return RepositoryGitHub(name, version)

    return None


def isHostedOnGitHub(name):
    url = "https://github.com/necxxt/{}".format(name)
    response = urllib.request.urlopen(url)

    return response.getcode() == 200
