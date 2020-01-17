import os
import socketserver
import threading
import json
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from solution_efe_config import configConstants

def createMicroservice(swaggerName,swaggerPath,swaggerUrl,controller):

    app = Flask(__name__)
    app.config['DEBUG'] = configConstants.DEBUG
    app.config['HOST'] = configConstants.HTTP['host']
    app.config['PORT'] = configConstants.HTTP['port']
    swaggerBaseUrl = configConstants.SWAGGER['host']+swaggerUrl

    SWAGGER_URL = swaggerPath
    API_URL = swaggerBaseUrl
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': swaggerName
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.register_blueprint(controller, url_prefix='/api/')
    return app

def launchServer(serverTcp):
    HOST, PORT = configConstants.TCP['host'], configConstants.TCP['port']
    print('Server TCP '+str(HOST)+':'+str(PORT))
    with socketserver.TCPServer((HOST, PORT), serverTcp) as server:
        server.serve_forever()

def createServerTcp(decode):
    class serverTcp(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(1024).strip()
            petition=json.loads(self.data.decode("utf-8"))
            respose=decode(petition['event'],petition['data'])
            sendData=json.dumps(respose) 
            self.request.sendall(bytes(sendData,"utf-8"))
    return serverTcp
