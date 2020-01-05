import requests
import datetime
from .start_up import URLS, AUTH


async def check_response(resp, topic=None):
    status = resp.status_code
    if status != 200:
        print(f"{topic or ''}request not successful: {status} - {resp.reason}")
    return resp


async def send(contact_id, text):
    resp = requests.post(URLS["MSGS"] + str(contact_id), headers=AUTH, json={'text': text})
    await check_response(resp, topic=f"send_message to {contact_id}")
    if resp.status_code == 200:
        await print_msg(resp.json())


async def get_history(contact_id):
    resp = requests.get(URLS["MSGS"] + str(contact_id), headers=AUTH)
    if await check_response(resp, topic="get_contacts"):
        return resp.json()


async def show_history(contact_id):
    history = await get_history(contact_id)
    if history:
        for message in history:
            await print_message(message)
            # print(message)


def get_timestamp(msg_time):
    # msg_time = datetime.datetime.fromtimestamp(msg_time / 1000).strftime('%Y-%m-%dT%H:%M:%S')
    msg_time = datetime.datetime.fromtimestamp(msg_time / 1000).strftime('%Y-%m-%d %H:%M')
    return msg_time


async def print_message(message):
    prefix = '> ' if message['local'] else ' <'
    time = get_timestamp(message['timestamp'])
    if 'text' in message:
        print(f"{time} {prefix} {message['text']}")


async def get_time(msg_time):
    # msg_time = datetime.datetime.fromtimestamp(msg_time / 1000).strftime('%Y-%m-%dT%H:%M:%S')
    msg_time = datetime.datetime.fromtimestamp(msg_time / 1000).strftime('%Y-%m-%d %H:%M')
    return msg_time


async def print_msg(message):
    prefix = '> ' if message['local'] else ' <'
    time = await get_time(message['timestamp'])
    if 'text' in message:
        print(f"{time} {prefix} {message['text']}")

