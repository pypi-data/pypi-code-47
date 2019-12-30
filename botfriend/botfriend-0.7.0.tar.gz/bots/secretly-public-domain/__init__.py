# encoding: utf-8
import json
from pdb import set_trace
from botfriend.bot import BasicBot
from botfriend.model import Post

class SecretlyPublicDomainBot(BasicBot):

    @classmethod
    def render(self, data):
        data = json.loads(data)
        hathi_id = data.get('hathi_id')
        if hathi_id:
            hathi_url = "https://catalog.hathitrust.org/Record/%s" % hathi_id
        else:
            hathi_url = None
        title = data.get('title')
        author = data.get('author')
        claimants = data.get('claimants') or []
        claimants = ", ".join(claimants)
        regnum = data.get('regnum')
        regdate = data.get('reg_date')
        lines = []
        key = (data['regnum'], data.get('reg_date', 'n/a'))
        lines.append("Registration #%s - %s" % key)
        lines.append("Title: %s" % title)
        title_index = len(lines)+1
        if author:
            lines.append("Author: %s" % author)
        if claimants:
            lines.append("Claimants: %s" % claimants)
            claimants_index = len(lines)+1
        lines.append("No renewal record found.")
        if hathi_url:
            lines.append(hathi_url)
        out = "\n".join(lines)
        if len(out) > 500:
            missing = len(out) - 500
            if len(title) > len(claimants):
                title = title[:len(title)-(missing+1)] + "…"
                lines[title_index] = "Title: %s" % title
            else:
                claimants = claimants[:len(claimants)-(missing+1)] + "…"
                lines[claimants_index] = "Claimants: %s" % claimants
        content = "\n".join(lines)
        return content, json.dumps(key)

    def prepare_input(self, line):
        return [line]
    
    def object_to_post(self, obj):
        """The input is a JSON list. We turn it into a post by calling render().
        """
        if isinstance(obj, str):
            obj = json.loads(obj)
        text, external_key = self.render(*obj)
        post, is_new = Post.from_content(self.model, text)
        post.external_key = external_key
        return [post]

Bot = SecretlyPublicDomainBot
