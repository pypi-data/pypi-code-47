from ..tokens import Tokens
import requests
import time

tokens = Tokens()
baseurl = "https://drone-1.prima.it"


def get_last_build_url(repo):
    # necessario per far comparire la build che abbiamo appena pushato
    time.sleep(2)
    try:
        resp = requests.get("{}/api/repos/primait/{}/builds".format(baseurl, repo),
                            headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()

        return '{}/primait/{}/{}'.format(baseurl, repo, resp[0]['number'])
    except (Exception) as e:
        return ""


def get_pr_build_url(repo, commit_sha):
    try:
        resp = requests.get("{}/api/repos/primait/{}/builds".format(baseurl, repo),
                            headers={'Authorization': 'Bearer {}'.format(tokens.drone)}).json()
        build_number = list(filter(lambda build: build.after == commit_sha, resp))[
            0]['number']
        return '{}/primait/{}/{}'.format(baseurl, repo, build_number)
    except (Exception) as e:
        return ""
