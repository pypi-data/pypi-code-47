import asyncio
import json
import requests
import websockets
import colorful as col
from .start_up import URLS, AUTH, TOKEN
from . import messages as msgs


async def check_response(resp, topic=None):
    status = resp.status_code
    if status != 200:
        print(f"{topic or ''}request not successful: {status} - {resp.reason}")
    return resp


async def probe_headless():
    if await check_response(requests.get(URLS["CONTACTS"], headers=AUTH),
                      topic="probe headless if headless is running"):
        print(col.bold_chartreuse("connection to headless successful!"))
    else:
        print(col.bold_coral("could not connect to headless!"))


async def connect_websocket():
    async with websockets.connect(URLS["WS"]) as ws:
        await ws.send(TOKEN)
        await get_message_websocket(ws)


async def get_message_websocket(ws):
    while not ws.closed and not asyncio.get_event_loop().is_closed():
        message = await ws.recv()
        m = json.loads(message)
        if m['name'] == 'ConversationMessageReceivedEvent':
            print()  # line-break
            await msgs.print_message(m['data'])
            print("", end='', flush=True)
    if not asyncio.get_event_loop().is_closed():
        asyncio.get_event_loop().create_task(get_message_websocket(ws))

