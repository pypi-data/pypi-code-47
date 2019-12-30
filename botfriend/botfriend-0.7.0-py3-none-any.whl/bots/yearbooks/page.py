from pdb import set_trace
import urllib.request, urllib.parse, urllib.error
import random
import requests
import json
import sys
from urllib.parse import urlparse

class Selection(object):
    image_template = "https://%(server)s/BookReader/BookReaderImages.php?zip=%(zip_path)s&file=%(image_path)s&scale=8&rotate=0"

    def __init__(self, path):
        self.items = []
        for x in open(path):
            try:
                item = json.loads(x.strip())
                self.items.append(item)
            except ValueError:
                continue

    def image_url(self, title, item, server_name, directory_number, page, jp2_filename):
        tests = [item['identifier']]
        for identifier in tests:
            url = self._image_url(identifier, item, server_name, directory_number, jp2_filename, page)
            if url:
                break
        return url
            
    def _image_url(self, identifier, item, server_name, directory_number, jp2_filename, page):
        #with_format_identifier = identifier + "_jp2"
        #zip_file_identifier = with_format_identifier + ".zip"
        with_format_identifier = jp2_filename[:-4]
        filename_base = with_format_identifier[:-4]
        
        zip_path = "/%(directory_number)s/items/%(identifier)s/%(archive_filename)s" % dict(
            identifier=identifier,
            directory_number=directory_number,
            archive_filename=jp2_filename,
        )

        image_filename = filename_base + "_%.4d.jp2" % page
        path_within_file = "/".join([with_format_identifier, image_filename])
        
        image_url = self.image_template % dict(
            server=server_name,
            zip_path=zip_path,
            image_path=path_within_file,
        )
        check = requests.head(image_url)
        if check.status_code == 500:
            print("%s didn't work." % image_url)
            return None
        return image_url
        
    def post(self):
        choice = random.choice(self.items)
        title = choice['title']
    
        description = choice.get('description')
        identifier = choice['identifier']
        pages = int(choice.get('imagecount', 50))
        page = random.randint(0,pages-1)
        jp2 = [
            x for x in choice['files']
            if x['format'] == 'Single Page Processed JP2 ZIP'
            and x['exists']
        ]
        if not jp2:
            return None
        [jp2] = jp2
        url = jp2['url']

       
        # Make a HEAD request to the jp2 URL to see which server the
        # file is on and which directory it's in.
        response = requests.head(url)
        if response.status_code != 302 or not 'location' in response.headers:
            return None, None, None
        location = response.headers['location']
        parsed = urlparse(location)
        server = parsed.netloc
        path = parsed.path.split("/")
        filename = path[-1]
        directory_number = path[1]
    
        reader_template = "https://archive.org/details/%(identifier)s/page/n%(page)d" 
        reader_url = reader_template % dict(
            identifier=choice['identifier'],
            page=page
        )
        
        image_url = self.image_url(title, choice, server, directory_number, page, filename)
        return title, reader_url, image_url
