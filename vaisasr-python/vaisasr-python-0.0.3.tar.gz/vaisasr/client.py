"""
Module to use the websocket API with an appliance.
"""
import asyncio
import copy
import inspect
import json
import logging
import sys
import string
import traceback

import websockets
import requests
import os
import random

LOGGER = logging.getLogger(__name__)

# If the logging level is set to DEBUG then websockets logs very verbosely,
# including a hex dump of every message being sent. Setting the websockets
# logger at INFO level specifically prevents this spam.
logging.getLogger("websockets.protocol").setLevel(logging.INFO)
AUTHEN_URL = "https://sohoa-api.vais.vn/authen"
ANALYTIC_URL = "https://sohoa-api.vais.vn/analytic"

def get_authen_file():
    homedir = os.path.expanduser('~/')
    vaisasr_dir = os.path.join(homedir, ".vaisasr")
    if not os.path.exists(vaisasr_dir):
        os.makedirs(vaisasr_dir)
    return os.path.join(vaisasr_dir, "credentials.json")


def login(email, password):
    r = requests.post(AUTHEN_URL + "/api/v1/auth/login", json={"email": email, "password": password})
    credential_file = get_authen_file()
    open(credential_file, "w").write(json.dumps(r.json()))

def get_header():
    credential_file = get_authen_file()
    assert os.path.exists(credential_file), "User unauthorized. Run `vais login` command to login"
    credential = json.loads(open(credential_file, "r").read())
    assert "access_token" in credential, "Access token not found. Run `vais login` command to login"
    return {"token": credential["access_token"]}

def get_upload_url(file_name, audiosource_id):
    r = requests.post(ANALYTIC_URL + "/v1/digitalization/upload-audio",
            json={
                "file_name": file_name,
                "audiosource_id": audiosource_id
                },
            headers=get_header())
    return r.json()

def create_audio(name, audiosource_id, bucket, key):
    r = requests.post(ANALYTIC_URL + "/v1/audios",
            json={
                "name": name,
                "audiosource_id": audiosource_id,
                "bucket": bucket,
                "key": key
                },
            headers=get_header())
    return r.json()


def upload_file(file_path, audiosource_id=None):
    if not audiosource_id:
        source = list_source()
        assert len(source) > 0, "You don't have any audio source configured, please access the web page and setup one."
        LOGGER.debug("Source id is not specified, use the default one")
        audiosource_id = source[0]["id"]
    LOGGER.debug("Uploading file to source " + audiosource_id)

    file_name, ext = os.path.splitext(os.path.basename(file_path))
    file_name += "_".join(random.choices(string.digits, k=4)) + ext

    upload_info = get_upload_url(file_name, audiosource_id)
    host = upload_info["postEndpoint"]
    signature = upload_info["signature"]

    audio_fd = open(file_path, "rb")
    files =  {'file': audio_fd}
    LOGGER.info("Uploading file")
    r = requests.post(host, data=signature, files=files, timeout=600)
    LOGGER.info("Upload complete")

    audio = create_audio(file_name, audiosource_id, signature["bucket"], signature["key"])
    r = requests.post(ANALYTIC_URL + "/v1/audios/execute-plan",
            json={
                "audio_id": audio["id"]
                },
            headers=get_header())
    LOGGER.info("Queued audio with id: " + audio["id"])
    return r.json()

async def monitor_status(audio_id):
    WS_ANALYTIC_URL = ANALYTIC_URL.replace("https", "wss").replace("http", "ws")
    URL = WS_ANALYTIC_URL + "/v1/monitor/ws/audio-status?audio_id=" + audio_id
    async with websockets.connect(URL) as websocket:
        while True:
            info = await websocket.recv()
            info = json.loads(info)
            if info["status"] == 4:
                return info["message"]
            LOGGER.info(info)

def list_source():
    r = requests.get(ANALYTIC_URL + "/v1/audio-sources",
            headers=get_header())
    return r.json()["data"]
