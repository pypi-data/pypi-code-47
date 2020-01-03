import requests
import cloudscraper
import os


def simple_get(url: str) -> bytes:
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    resp = requests.get(url, timeout=3)
    if resp.status_code != 200:
        raise Exception(f"Wrong status code: {resp.status_code}")
    return resp.content


scraper = cloudscraper.create_scraper()


def scraper_get(url: str) -> bytes:
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    for i in range(3):
        try:
            resp = scraper.get(url)
            if i > 0:
                print("Request successful")
            break
        except RuntimeError:
            print(f"Request failed {i+1} of 3")
    else:
        raise Exception(f"Request failed")

    if resp.status_code != 200:
        raise Exception(f"Wrong status code: {resp.status_code}")
    return resp.content


def download_file(url: str, file: str, p_fun) -> bool:
    try:
        with open(file, mode="wb") as f:
            resp = requests.get(url, stream=True, allow_redirects=True)
            total_length = resp.headers.get("content-length")
            if total_length is None:
                f.write(resp.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in resp.iter_content(chunk_size=1024):
                    dl += len(data)
                    p_fun(int(dl / total_length * 100.0))
                    f.write(data)
        return True
    except requests.exceptions.RequestException:
        if os.path.isfile(file):
            os.remove(file)
        return False
