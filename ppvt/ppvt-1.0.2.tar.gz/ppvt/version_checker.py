import requests
import json

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse


class Pypi:
    """
    Helps to find the latest version of pip modules
    """

    @staticmethod
    def url():
        """
        Pypi python org API to get package versions
        """
        url = "https://pypi.python.org/pypi/{package}/json"

        return url

    @staticmethod
    def _get_python_version(info):
        rec1 = dict()
        rec2 = dict()
        if len(info) >= 1:
            rec1 = info[0]
        if len(info) >= 2:
            rec2 = info[1]

        rec1.update(rec2)
        version = rec1.get("requires_python")
        if version:
            version = str(version)

        return version

    @staticmethod
    def get(package):
        """
        Get list of versions for a given package with
        all the info.
        Args:
            package = Package name. Ex: Django.
        Output:
            List of versions and their details.
        """
        url = Pypi.url()
        url = url.format(package=package)

        # Request Pypi
        resp = requests.get(url)
        if resp.status_code != requests.codes.ok:
            return dict(status="failure", message="Invalid Package")

        data = dict()
        resp = resp.json()
        releases = resp.get("releases", [])
        data["releases"] = releases
        data["status"] = "success"

        return data

    @staticmethod
    def all(data):
        """
        Give pypi pesponse to this method.
        It will return list of versions with minimal info.
        Args:
            data = Pypi response.
        Output:
            List of versions.
        """
        result = list()
        for release, info in data.items():
            version = release
            python_version = Pypi._get_python_version(info)
            d = dict(version=version, python_version=python_version)
            result.append(d)

        return result

    @staticmethod
    def latest(data):
        """
        Give pypi pesponse to this method.
        It will return latest version of the module.
        Args:
            data = Pypi response.
        Output:
            List of versions.
        """
        result = dict()
        version = parse("0")
        for release, info in data.items():
            python_version = Pypi._get_python_version(info)
            ver = parse(release)
            if not ver.is_prerelease:
                version = max(version, ver)
                python_version = python_version

        result = dict(version=str(version), python_version=python_version)

        return [result]

    @staticmethod
    def greater(data, version):
        """
        Give pypi pesponse to this method.
        It will return grater version of the given version.
        Args:
            data = Pypi response.
        Output:
            List of versions.
        """
        result = list()
        given_version = parse(version)
        for release, info in data.items():
            python_version = Pypi._get_python_version(info)
            ver = parse(release)
            if not ver.is_prerelease and ver > given_version:
                result.append(dict(version=str(ver), python_version=python_version))

        return result
