import requests

BUILD_ALIASES = {
    "hg19": "GRCh37"
}


def fetch_rsid(rs_id: str, species: str = "human") -> dict:
    """
    Fetch rsid from Ensembl
    :param rs_id: the rs id to look up
    :param species: the species to look up (human default)
    :raises: ValueError when rsid can't be found
    :return: dict of returned response
    """
    url = "https://rest.ensembl.org/variation/{0}/{1}".format(
        species,
        rs_id
    )

    r = requests.get(url, headers={"Content-Type": "application/json"})
    if r.status_code == 400:
        raise ValueError("Could not find rsid {0}".format(rs_id))
    return r.json()


def fetch_sequence(reference: str, chromosome: str, start: int,
                   end: int, species: str = "human") -> str:
    """
    Fetch sequence for a region from Ensembl
    :param reference: name of reference build
    :param chromosome: chromosome
    :param start: start position
    :param end: end position
    :param species: species
    :return:
    """
    ref = BUILD_ALIASES.get(reference, reference)
    url = "https://rest.ensembl.org/sequence/region/{0}/{1}:{2}-{3}".format(
        species,
        chromosome,
        start,
        end
    )

    r = requests.get(url, params={"coord_system_version": ref},
                     headers={"Content-Type": "application/json"})
    if r.status_code == 400:
        raise ValueError("Could not find region")
    return r.json().get("seq")


def position_converter(build: str, variant: str) -> requests.Response:
    url = "https://mutalyzer.nl/json/numberConversion"
    r = requests.get(url, params={"build": build, "variant": variant})
    return r


def name_checker(variant: str) -> requests.Response:
    url = "https://mutalyzer.nl/json/runMutalyzer"
    r = requests.get(url, params={"variant": variant})
    return r
