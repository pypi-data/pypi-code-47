from flask import Flask
from flask import request
from flask import send_file
from flask import abort
from flask import render_template_string
from flask import make_response
from flask import Response
import os
import shutil
import sys
import webbrowser
import datetime
import logging

app = Flask('tiddlypy')

# Template used to list content of directory
templatelistdir="""
<!doctype html>
<title>tiddlypy -- {{ path }}</title>
<h1>Path : {{ path }}</h1>
<ul>
{%- for item in lst %}
    <li><a href="{{ item }}">{{ item }}</a></li>
{%- endfor %}
</ul>
"""

# handling OPTIONS must be declared before
# GET otherwise this doesnt work
# dont know why
@app.route('/<path>', methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def serveOPT(path='.'):
    logging.debug("OPTIONS request on path={}".format(path))
    if os.path.isfile(path):
        resp = make_response()
        # This is needed to be add to the header to inform TiddlyWiki that we support DAV.
        # Otherwise it will not try to save the Tiddly with DAV
        resp.headers['DAV'] = "1.2"
        return resp
    else:
        abort(404)

@app.route('/', methods=['GET'])
@app.route('/<path:path>', methods=['GET']) 
def serve(path='.'):
    logging.debug("GET request on path={}".format(path))
    # if a file is requested, send it 
    if os.path.isfile(path):
        return send_file(path)
    # if it is a directory
    # send the list of files using the template templatelistdir
    elif os.path.isdir(path):
        lst = os.listdir(path)

        # add '/' to name for each directorys
        for index, entry in enumerate(lst):
            if os.path.isdir(path + '/' + entry):
                lst[index] = entry + '/'
        
        # remove hidden files
        lst = [ entry for entry in lst if not entry[0]=='.' ]

        return render_template_string(templatelistdir, path=path, lst=lst)
    # not a file, and not a directory
    # return error
    else:
        abort(404)

@app.route('/<path:path>', methods=['PUT'])
def put(path='.'):
    logging.debug("PUT request on path={}".format(path))
    logging.debug("PUT referer header : ".format(request.headers['Referer']))
    open(path,'wb').write(request.get_data())
    # We have to send something back
    return "ok"


def main_func():
    logging.basicConfig(filename='.tiddlypy.log',level=logging.DEBUG)
    webbrowser.open_new_tab("http://127.0.0.1:5000")
    app.run()

if __name__ == "__main__":
    main_func()
   
