from sanic import Sanic
from sanic.response import json, HTTPResponse, text
from sanic_cors import cross_origin
from sanic_cors.extension import cors
from spf import SanicPluginsFramework
import time

app = Sanic(__name__)
app.config['CORS_AUTOMATIC_OPTIONS'] = True
spf = SanicPluginsFramework(app)
spf.register_plugin(cors, automatic_options=True)
##CORS(app, automatic_options=True)


@app.route('/timeline', methods=["GET", "OPTIONS"])
@cross_origin(app)
async def get_timeline(request):
    if request.method == "OPTIONS":
        return HTTPResponse()
    time.sleep(61)
    user = None
    #twitter_api.assign_user(user.token, user.secret)

    #raw_timeline_tweets = twitter_api.get_home_timeline()
    #timeline_tweets = [Tweet(raw_timeline_tweet) for raw_timeline_tweet in raw_timeline_tweets]

    return json({"timeline": "test"})


#app.blueprint(auth_route, url_prefix="/auth")
#app.blueprint(user_route, url_prefix="/user")
#app.blueprint(tweet_route, url_prefix='/tweet')

app.run(host="localhost", port=5001, debug=False, workers=2)
