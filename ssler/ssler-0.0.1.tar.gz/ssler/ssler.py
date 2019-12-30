import os
import sys
from flask import Flask, request, Response
import requests


os.environ['WERKZEUG_RUN_MAIN'] = 'true'
redirect_addr = 'localhost:8080'
run_port = 8800


def help():
    print('''ssler
Easily redirect your localhost server though an a server with self signed certificate

usage: ssler '<domain>' '<ssler_port(optional)>'
examples:
    - ssler 'localhost:8080'
    - ssler 'http://33.22.22.88'
    - ssler 'localhost:8080' 8888''')


if len(sys.argv) < 2:
    print("Please provide redirect address")
    help()
    exit(1)
elif len(sys.argv) < 3:
    if sys.argv[1] in ['--help', '-h']:
        help()
        exit(0)
    print('Will use port 8800 for https')
    redirect_addr = sys.argv[1]
elif len(sys.argv) > 4:
    print('Not sure why there are so many parametes')
    help()
    exit(1)
else:
    redirect_addr = sys.argv[1]
    run_port = int(sys.argv[2])


app = Flask(__name__)
SITE_NAME = redirect_addr


@app.route("/")
def index():
    return proxy("")


@app.route("/<path:path>", methods=["GET", "POST", "DELETE"])
def proxy(path):
    global SITE_NAME
    if request.method == "GET":
        resp = requests.get(f"{SITE_NAME}/{path}", headers=request.headers)
        excluded_headers = [
            "content-encoding",
            "content-length",
            "transfer-encoding",
            "connection",
        ]
        headers = [
            (name.upper(), value)
            for (name, value) in resp.raw.headers.items()
            if name.lower() not in excluded_headers
        ]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == "POST":
        resp = requests.post(f"{SITE_NAME}/{path}", json=request.get_json(), headers=request.headers)
        excluded_headers = [
            "content-encoding",
            "content-length",
            "transfer-encoding",
            "connection",
        ]
        headers = [
            (name, value)
            for (name, value) in resp.raw.headers.items()
            if name.lower() not in excluded_headers
        ]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == "DELETE":
        resp = requests.delete(f"{SITE_NAME}/{path}", headers=request.headers).content
        response = Response(resp.content, resp.status_code, headers)
        return response


def main():
    app.run(ssl_context="adhoc", port=run_port)


if __name__ == "__main__":
    main()
