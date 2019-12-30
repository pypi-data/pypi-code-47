# encoding: utf-8
import requests
import os
import json
from nose.tools import set_trace
from botfriend.bot import BasicBot
from botfriend.model import (
    Post,
)
from .yearbooks import Yearbook


class YearbookBot(BasicBot):
    
    def new_post(self):
        title, year, reader_url, image_url = Yearbook().post()
        if not image_url:
            return None
        response = requests.get(image_url)
        media_type = response.headers['Content-Type']
        text = "%s (%s)\n\n%s" % (title, year, reader_url)
        post, is_new = Post.from_content(self.model, text, reuse_existing=False)
        post.attach(media_type, content=response.content)
        return post
        
Bot = YearbookBot


