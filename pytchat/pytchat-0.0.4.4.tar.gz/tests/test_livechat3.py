import asyncio, aiohttp
import json
import pytest
import re
import requests

import sys
import time
from aioresponses import aioresponses
from concurrent.futures import CancelledError
from unittest import TestCase
from pytchat.core_multithread.livechat import LiveChat
from pytchat.core_async.livechat import LiveChatAsync
from pytchat.exceptions import (
      NoLivechatRendererException,NoYtinitialdataException,
      ResponseContextError,NoContentsException)
from pytchat.parser.live import Parser
from pytchat.processors.dummy_processor import DummyProcessor
def _open_file(path):
    with open(path,mode ='r',encoding = 'utf-8') as f:
        return f.read()
def test_multithread_replay_stream(mocker):
    # def func(chats):
    #     rawdata = chats[0]["chatdata"]
    #     assert list(rawdata[0]["addChatItemAction"]["item"].keys())[0] == "liveChatTextMessageRendere"
    #     assert list(rawdata[14]["addChatItemAction"]["item"].keys())[0] == "liveChatPaidMessageRenderer"
    class ResponseObj:
        def __init__(self,text):
            self.text=text
            self.status_code = 200
    def switch(url,headers):
        _text_live = _open_file('tests/testdata/finished_live.json')
        _text_replay = _open_file('tests/testdata/chatreplay.json')
        pattern_live = re.compile(r'^https://www.youtube.com/live_chat/get_live_chat\?continuation=.*$')
        pattern_replay =  re.compile(r'^https://www.youtube.com/live_chat_replay/get_live_chat_replay\?continuation=.*$')
        if re.match(pattern_live, url):
            print("$",url)
            return ResponseObj(_text_live)
        elif re.match(pattern_replay,url):
            print(url)
            return ResponseObj(_text_replay)
    #pattern_live = 'https://www.youtube.com/live_chat/get_live_chat?continuation=0&pbj=1'
    #pattern_replay =  'https://www.youtube.com/live_chat_replay/get_live_chat_replay?continuation=1&pbj=1'
    #empty livechat -> switch to fetch replaychat

    # responseMock_live = mocker.Mock()
    # responseMock_live.status_code = 200
    # responseMock_live.text = _text_live
    # mocker.patch(f'requests.Session.get').return_value.__enter__.return_value = responseMock_live

    _text_live = _open_file('tests/testdata/finished_live.json')
    _text_replay = _open_file('tests/testdata/chatreplay.json')
    responseMock_replay = mocker.Mock()
    responseMock_replay.side_effect=switch#[ResponseObj(_text_live),ResponseObj(_text_replay)]
    #responseMock_replay.status_code = 200
    #responseMock_replay.text = _text_replay
    #mocker.patch(f'requests.Session.get').return_value.__enter__.return_value = responseMock_replay()
    mocker.patch('requests.Session.get').return_value.__enter__.return_value = responseMock_replay
    #mocker.patch('liveparam.getparam').return_value = "0"
    #mocker.patch('arcparam.getparam').return_value = "1"
    chat = LiveChat(video_id='', processor = DummyProcessor())
    chats= chat.get()
    time.sleep(1)
    rawdata = chats[0]["chatdata"]
    print(rawdata,"#")
    #mocker.assertEqual(responseMock_replay.mock_calls[0], call('http://google.co.jp'))
    #mocker.assertEqual(responseMock_replay.mock_calls[1], call('http://google.co.jp'))
    assert list(rawdata[0]["addChatItemAction"]["item"].keys())[0] == "liveChatTextMessageRenderer"
    assert list(rawdata[14]["addChatItemAction"]["item"].keys())[0] == "liveChatPaidMessageRenderer"
        
    #time.sleep(3)
    #chat.terminate()