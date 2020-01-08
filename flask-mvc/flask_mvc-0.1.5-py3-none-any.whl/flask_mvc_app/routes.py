from flask_mvc_app import app, db, models
from flask import render_template, escape, redirect
from flask_mvc_app.controller import Controller
from werkzeug.http import http_date
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return redirect('app/admin/')

@app.route('/app', methods=['GET'])
def app_index():
    return f'General Overview'

@app.route('/app/<namespace>', methods=['GET'])
def namespace_index(namespace):
    context = {'nav_models': models.registry}
    return render_template('namespace_list.html', **context) # f'Overview {escape(namespace)}'

@app.route('/app/<namespace>/<model>', methods=['GET'])
def list_view(namespace, model):
    return Controller(escape(namespace), escape(model)).index()

@app.route('/app/<namespace>/<model>/view/<int:id>', methods=['GET'])
def item_view(namespace, model, id):
    return Controller(escape(namespace), escape(model)).view(id)

@app.route('/app/<namespace>/<model>/add', methods=['POST', 'GET'])
def create_view(namespace, model):
    return Controller(escape(namespace), escape(model)).create()

@app.route('/app/<namespace>/<model>/edit/<int:id>', methods=['POST', 'GET'])
def update_view(namespace, model, id):
    return Controller(escape(namespace), escape(model)).update(id)

@app.route('/app/<namespace>/<model>/delete/<int:id>', methods=['POST', 'GET'])
def delete_view(namespace, model, id):
    return Controller(escape(namespace), escape(model)).delete(id)

@app.errorhandler(404)
def page_not_found(e):
    context = {'nav_models': models.registry}
    return render_template('errors/404.html', **context), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    context = {'nav_models': models.registry}
    return render_template('errors/500.html', **context), 500

@app.after_request
def set_response_headers(response):
    response.headers['Last-Modified'] = http_date(datetime.now())
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response