from requests.exceptions import HTTPError

from backends import Dec2019Backend, LegacyBackend

BACKENDS = [Dec2019Backend(), LegacyBackend()]


def search_movies(search_term):
    for parser in BACKENDS:
        try:
            results = parser.search_movies(search_term)
            if results:
                return results
        except HTTPError:
            continue

    return []


def get_movie_id(search_term):
    results = search_movies(search_term)

    exact_match = next((result for result in results if result['exact']), None)
    if exact_match is not None:
        return exact_match['movie_id']

    # Otherwise, if there's exactly one match, return that.
    if len(results) == 1:
        return results[0]['movie_id']

    # In any other case, return None since there isn't an unambiguous result.
    return None


def get_box_office(movie_id):
    for parser in BACKENDS:
        try:
            result = parser.get_box_office(movie_id)
            if result['box_office']:
                return result
        except HTTPError:
            continue

    return {}
