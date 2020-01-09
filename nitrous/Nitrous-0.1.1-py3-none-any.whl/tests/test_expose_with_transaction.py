from json import dumps, loads

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from turbogears import controllers, database, expose, view
from turbogears.testutil import make_app, start_server, stop_server

import pytest


session = database.session

engine = database.get_engine()
metadata = database.get_metadata()

Base = declarative_base(bind=engine, metadata=metadata)


class User(Base):
    __tablename__ = 'test_user'

    id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.Unicode, nullable=False)


metadata.create_all(engine)


class Root(controllers.RootController):
    @expose()
    def users(self, user_name):
        user = User(user_name=user_name)
        session.add(user)

        return {'user_name': user.user_name}

    @expose()
    def should_rollback(self):
        user = User(user_name='phantom')
        session.add(user)
        session.flush()

        1/0


@pytest.fixture
def app():
    return make_app(Root)


def test_users_endpoint_should_add_user(app):
    response = app.post('/users/newbie')

    assert session.query(User).filter_by(user_name='newbie').one()


def test_exception_endpoint_should_raise(app):
    app.get('/should_rollback', status=500)

    assert not session.query(User).filter_by(user_name='phantom').first()
