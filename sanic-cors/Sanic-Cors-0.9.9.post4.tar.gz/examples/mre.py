from sanic import Sanic
from sanic.response import text
try:
    #Sanic 19.9.0 and above
    from sanic.compat import CIMultiDict
except ImportError:
    #Sanic 18.12.0-19.6.3
    from sanic.server import CIMultiDict

app = Sanic()

@app.route("/")
def index(request):
    my_headers = CIMultiDict({"Vary": "Origin"})
    my_headers.extend({"Vary": "'Accept-Encoding'"})
    return text("OK", headers=my_headers)

req, resp = app.test_client.get("/")
vary = resp.headers.get('Vary')
print(vary)