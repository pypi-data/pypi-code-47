import logging

import graphene as g
import yaml
from celery import Celery

from flask import Flask, Response
from flask_graphql import GraphQLView
from redis import StrictRedis

from .service import forms_service, FormsQuery, FormCreatedEvent

app = Flask(__name__)
app.secret_key = app.config['SECRET_KEY'] = 'foobar'
app.config['broker_url'] = 'redis://localhost:6379/0'
app.config['result_backend'] = 'redis://localhost:6379/0'

app.celery = celery = Celery(app.name, broker=app.config['broker_url'], backend=app.config['result_backend'])
celery.conf.update(app.config)
celery.set_current()
celery.set_default()

logging.basicConfig(level=logging.DEBUG)
forms_service.init_app(app)
forms_service.logger.info("Forms Service initted. Adding mutations and queries")


@app.route('/consumer_config')
def consumer_config():
    return Response(yaml.dump(forms_service.default_consumer_config()), mimetype='text/yaml')


class FormServiceMutations(forms_service.Mutations):
    pass


class FormServiceQueries(FormsQuery):
    service_web_backend = StrictRedis(db=10)


schema = g.Schema(query=FormServiceQueries, mutation=FormServiceMutations, types=forms_service.types)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))