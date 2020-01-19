import os
import errno
import getpass
from pathlib import Path
import colorful as col


def get_auth_token():
    AUTH_FILE = Path(f"/home/{getpass.getuser()}/.briar/auth_token")
    if not AUTH_FILE.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), AUTH_FILE)
    with open(AUTH_FILE) as txt:
        token = txt.read().strip()
        return {'Authorization': f'Bearer {token}'}, token


AUTH, TOKEN = get_auth_token()
HOST = "127.0.0.1"
PORT = 7000
API_VERSION = "v1"
URL_BASE = f'http://{HOST}:{PORT}/{API_VERSION}/'
APP_NAME = "briar_repl"
print(f"\nwelcome to {col.bold_chartreuse(APP_NAME)}!")
print("to list all functionality enter 'help'.\n")

URLS = {
    "BASE"             : URL_BASE,
    "CONTACTS"         : f"{URL_BASE}contacts",
    "CONTACTS_PENDING" : f"{URL_BASE}contacts/add/pending",
    "ADD_LINK"         : f"{URL_BASE}contacts/add/link",
    "MSGS"             : f"{URL_BASE}messages/",
    "BLOGS"            : f"{URL_BASE}blogs/posts",
    "WS"               : f'ws://{HOST}:{PORT}/{API_VERSION}/ws',
}
