from flask import Flask
from flask import request
from flask import send_from_directory
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
import datetime
import configparser


app = Flask('tiddlypy')
config = configparser.ConfigParser()


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

# decorator for pluggable function
def pluggable(f, *args, **kargs):
    def pluginwrapper(*args, **kargs):
        global config
        plugin = None

        #look for configuration for the requested file
        if kargs.get('path','/') in config.sections():
            section = config[kargs.get('path')]

            #look if there is plugin entry
            if section.get("plugin"):
                plugin = section.get("plugin")

        #run <plugin> before <function> <path>
        if plugin:
            cmd = ' '.join([plugin, 'before', f.__name__, kargs.get('path', '/')])
            logging.debug("plugin run : {}".format(cmd))
            pluginret = os.system(cmd)
            logging.debug("plugin return value : {}".format(pluginret))
            if pluginret != 0:
                logging.warning("plugin return value : {}".format(pluginret))

        # run the pluged function
        ret = f(*args, **kargs)

        #run <plugin> after <function> <path>
        if plugin:
            cmd = ' '.join([plugin, 'after', f.__name__, kargs.get('path', '/')])
            logging.debug("plugin run : {}".format(cmd))
            pluginret = os.system(cmd)
            logging.debug("plugin return value : {}".format(pluginret))
            if pluginret != 0:
                logging.warning("plugin return value : {}".format(pluginret))


        return ret

    logging.debug("decoration of function ", f.__name__)
    pluginwrapper.__name__ = "pluginwrapper_"+f.__name__
    return pluginwrapper


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
@pluggable
def serve(path='.'):
    logging.debug("GET request on path={}".format(path))
    # if a file is requested, send it 
    if os.path.isfile(path):
        return send_from_directory(os.getcwd(), path)
    # if it is a directory
    # send the list of files using the template templatelistdir
    elif os.path.isdir(path):
        lst = os.listdir(path)

        # sort by alphabetical order
        lst = sorted(lst)

        # add '/' to name for each directorys
        lst = [os.path.join(entry, '') if os.path.isdir(entry) else entry for entry  in lst]

        # remove hidden files
        lst = [ entry for entry in lst if not entry[0]=='.' ]

        return render_template_string(templatelistdir, path=path, lst=lst)
    # not a file, and not a directory
    # return error
    else:
        abort(404)


@app.route('/<path:path>', methods=['PUT'])
@pluggable
def put(path='.'):
    logging.debug("PUT request on path={}".format(path))
    logging.debug("PUT referer header : ".format(request.headers['Referer']))
    with open(path, 'wb') as filedest:
        filedest.write(request.get_data())
        filedest.flush()

    # We have to send something back
    return "ok"

def main_func():
    config.read('tiddlypy.ini')

    logging.basicConfig(filename='.tiddlypy.log',level=logging.DEBUG)
    webbrowser.open_new_tab("http://127.0.0.1:5000")

    # force browser not to cache
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.run()

if __name__ == "__main__":
    main_func()
   
