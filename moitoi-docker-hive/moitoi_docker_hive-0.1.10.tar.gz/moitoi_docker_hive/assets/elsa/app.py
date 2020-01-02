"""
MDH REST Api module
"""
import os
import re

from flask import Flask
from flask_restful import Api

from rest.controller import ServiceAPI, StateAPI, Root

app = Flask(__name__)
app.config['DEBUG'] = re.match("(1|TRUE|Y|True)", os.environ.get('DEBUG', "false"))
api = Api(app)

api.add_resource(ServiceAPI, '/Service')
api.add_resource(StateAPI, '/State')
api.add_resource(Root, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
