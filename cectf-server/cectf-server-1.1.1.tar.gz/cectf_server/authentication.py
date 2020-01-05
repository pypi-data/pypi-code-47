from flask import Blueprint, jsonify, request
from flask_login import current_user
from flask_security.registerable import register_user
from flask_security.utils import logout_user, login_user, verify_and_update_password, hash_password
from flask_wtf.csrf import generate_csrf
import re
from .models import User, Role, Challenge, Solve
from .passwords import password_dictionary

blueprint = Blueprint('authentication', __name__, url_prefix='/api/auth')


@blueprint.route('/csrf', methods=['GET'])
def csrf():
    return jsonify({'csrf_token': generate_csrf()})


@blueprint.route('/login', methods=['POST'])
def login():
    if request.get_json() == None:
        return (jsonify({'error': 'Request JSON is required'}), 400)
    if 'username' not in request.get_json():
        return (jsonify({'error': 'Username is required'}), 400)
    if 'password' not in request.get_json():
        return (jsonify({'error': 'Password is required'}), 400)
    username = request.get_json()['username']
    password = request.get_json()['password']

    user = User.query.filter_by(username=username).first()
    if user == None:
        # maybe they logged in with their email instead of their username
        user = User.query.filter_by(email=username).first()
    if user == None:
        # username/password not found
        hash_password(password) # hash the password anyway to prevent timing attacks
        return (jsonify({'error': 'Username/password not found'}), 400)
    if not verify_and_update_password(password, user):
        # password is wrong
        return (jsonify({'error': 'Username/password not found'}), 400)
    login_user(user)

    return (jsonify({'authentication_token': user.get_auth_token()}), 200)


@blueprint.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
    return ('', 204)

def _error(message):
    return (jsonify({'error': message}), 400)

def _validate_email(request_json):
    print(dir(User.email))
    if 'email' not in request_json:
        return _error('Email is required')
    email = request_json['email']
    match = re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email)
    if match == None:
        return _error('Email is formatted incorectly')
    if len(email) > User.email.property.columns[0].type.length:
        return _error('Email is too long')
    if User.query.filter_by(email=email).first() != None:
        return _error('Email is already registered')
    return None

def _validate_username(request_json):
    if 'username' not in request_json:
        return _error('Username is required')
    username = request_json['username']
    if len(username) < 3:
        return _error('Username must have 3 or more characters')
    if len(username) > User.username.property.columns[0].type.length:
        return _error('Username is too long')
    if User.query.filter_by(username=username).first() != None:
        return _error('Username is already registered')
    return None

def _validate_password(request_json):
    if 'password' not in request_json:
        return _error('Password is required')
    password = request_json['password']
    if password in password_dictionary:
        return _error('good god why would you choose that password')
    if len(password) < 6:
        return _error('Password must have 6 or more characters')
    return None

def _validate_register_request_json(request_json):
    if request_json == None:
        return _error('Request JSON is required')
    error = _validate_email(request_json)
    if error != None:
        return error
    error = _validate_username(request_json)
    if error != None:
        return error
    error = _validate_password(request_json)
    if error != None:
        return error
    return None
    

@blueprint.route('/register', methods=['POST'])
def register():
    error = _validate_register_request_json(request.get_json())
    if error != None:
        return error
    
    email = request.get_json()['email']
    password = request.get_json()['password']
    username = request.get_json()['username']
    roles = [Role.query.filter_by(name='contestant').first()]
    solves = [Solve(
        solved=False,
        challenge=challenge)
        for challenge in Challenge.query.all()]

    new_user = register_user(email=email,
                             password=password,
                             username=username,
                             roles=roles,
                             solves=solves)

    login_user(new_user)
    return (jsonify({'authentication_token': new_user.get_auth_token()}), 200)


def init_app(app):
    app.register_blueprint(blueprint)
