from sanic import Sanic
from sanic.exceptions import SanicException
from sanic_cors import CORS
from sanic.response import HTTPResponse

app = Sanic()
CORS(app, automatic_options=True)


@app.middleware('request')
async def handle_options_middleware(req):
    if req.method == 'OPTIONS':
        return HTTPResponse()

@app.route('/')
async def t1(req):
    raise SanicException("hello", 401)

app.run(host="localhost", port=5001, debug=True, auto_reload=False)