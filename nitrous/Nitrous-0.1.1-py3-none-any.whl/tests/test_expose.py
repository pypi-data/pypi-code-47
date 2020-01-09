from json import dumps, loads

from turbogears import controllers, expose, view
from turbogears.testutil import make_app, start_server, stop_server

import pytest


class RandomResource:
    @expose('json')
    def index(self):
        return {'result': 4}  # chosen by fair dice roll; guaranteed random


class ResuorceWithDefault:
    @expose('json')
    def default(self):
        return {'message': 'brought to you by the default view'}


class ResuorceWithIndex:
    @expose('genshi:turbogears.tests.simple')
    def index(self):
        return {'someval': 'SUCCESS!'}


class EmptyResource:
    pass


class Root(controllers.RootController):
    nodefault = EmptyResource()
    noindex = EmptyResource()
    random = RandomResource()
    withdefault = ResuorceWithDefault()
    withindex = ResuorceWithIndex()

    @expose('json')
    def some_json(self):
        return {
            'title': 'Foo',
            'abool': False,
            'someval': 'foo',
        }

    @expose('json')
    def custom_json(self, **kw):
        request = controllers.request
        json = request.rfile.input.getvalue()

        return loads(json)

    @expose('genshi:turbogears.tests.simple')
    def html(self, someval=None, **kw):
        """Basic HTML page, rendered by Genshi.

        Includes the phrase `Paging all ${someval}`.

        """

        return {
            'someval': someval
        }

    @expose('json')
    def a_b_but_not_c(self, a, b=2):
        return {
            'a': a,
            'b': b,
        }


@pytest.fixture(autouse=True, scope='session')
def load_engines():
    view.load_engines()


@pytest.fixture
def app():
    return make_app(Root)


def test_html_endpoint_should_return_html(app):
    response = app.get('/html')

    assert response.headers['content-type'].startswith('text/html')


def test_html_endpoint_should_not_return_json(app):
    response = app.get('/html')

    with pytest.raises(AttributeError):  # webtest for “response not JSON”
        response.json


def test_html_endpoint_should_include_rendered_value(app):
    response = app.get('/html?someval=☺')

    assert 'Paging all ☺' in response


def test_index_endpoint_should_be_exposed(app):
    response = app.get('/withindex/')

    assert 'Paging all SUCCESS!' in response


def test_default_endpoint_should_be_exposed(app):
    response = app.get('/withdefault/nonexistent')

    assert 'default view' in response.json['message']


# TODO: in TG 1, this is configurable via the allow_json option
# Options:
#   a always allow
#   b require expose(json) or expose(allow_json=True)
#   c TG 1 behavior: a or b selected by config
def test_html_endpoint_should_return_json_if_requested(app):
    response = app.get('/html?tg_format=json')

    assert response.json


def test_json_endpoint_should_return_json(app):
    response = app.get('/some_json')

    assert response.json


def test_json_response_should_include_value(app):
    response = app.get('/some_json')

    assert 'Foo' == response.json['title']


def test_json_endpoint_should_return_json_content_type(app):
    response = app.get('/some_json')

    assert 'application/json' == response.headers['content-type']


# FIXME: support non-dict json
@pytest.mark.parametrize('value', [
    {'a_key': None},
    {'a_key': True},
    {'a_key': 123},
    {'a_key': 'a neato string'},
    {'a_key': '♥'},
])
def test_json_value_should_encode_correctly(app, value):
    response = app.post('/custom_json', params=dumps(value))

    assert value == response.json


def test_extra_path_component_should_be_first_positional_argument(app):
    response = app.get('/a_b_but_not_c/smurf')

    assert 'smurf' == response.json['a']


def test_positional_argument_can_be_specified_by_name(app):
    response = app.get('/a_b_but_not_c?a=yay+semantics!')

    assert 'yay semantics!' == response.json['a']


def test_passing_unexpected_argument_should_succeed(app):
    response = app.get('/a_b_but_not_c?a=1&c=BOOM BABY!')


def test_subview_index_should_be_exposed(app):
    response = app.get('/random/')

    assert 4 == response.json['result']


def test_subview_without_index_should_not_expose_index(app):
    response = app.get('/noindex/', status=404)


def test_subview_without_default_should_404_for_nonexistent_view(app):
    response = app.get('/nodefault/nonexistent', status=404)
