import datetime
import json
from nose.tools import set_trace
import os

from bot import Bot as BasicBot
from model import Post

class TimeBot(BasicBot):

    dir = os.path.split(__file__)[0]

    def local_path(self, filename):
        return os.path.join(self.dir, filename)

    def new_post(self):
        return None

    def schedule_posts(self):
        script = self.local_path("script.txt")
        for i in open(script):
            data = json.loads(i.strip())
            in_format = '%Y-%m-%d'
            content = datetime.datetime.strptime(data['date'], in_format).strftime("%B %d, %Y")
            publish_at_str = data['post_date']
            publish_at = datetime.datetime.strptime(publish_at_str, in_format).replace(
                hour=17
            )
            expect = self.local_path(data['path'])
            if not os.path.exists(expect):
                self.log.warn(
                    "Not creating post for %s: %s does not exist.",
                    publish_at_str, expect
                )
                continue
                
            post, is_new = Post.for_external_key(self.model, publish_at_str)
            if is_new:
                post.content = content
                post.publish_at = publish_at
                post.attach('image/png', data['path'])
                self.log.info("Created post for %s", publish_at_str)
            else:
                self.log.info("Post for %s already exists.", publish_at_str)
Bot = TimeBot
