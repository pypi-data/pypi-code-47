# encoding: utf-8
import requests
import os
import json
from nose.tools import set_trace
from botfriend.bot import BasicBot
from botfriend.model import (
    Post,
)
from .page import Selection

class JunkMailBot(BasicBot):
    
    def new_post(self):
        d = os.path.split(__file__)[0]
        path = os.path.join(d, "data/1-details-tednelsonjunkmail.ndjson")
        choice = Selection(path)
        post = choice.post()
        if not post:
            return None
        title, reader_url, image_url = post
        if not image_url:
            return None
        response = requests.get(image_url)
        media_type = response.headers['Content-Type']
        text = "%s\n\n%s" % (title, reader_url)
        post,  is_new = Post.from_content(self.model, text, reuse_existing=False)
        post.attach(media_type, content=response.content)
        return post
        
Bot = JunkMailBot


