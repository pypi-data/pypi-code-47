# dependency: sqlalchemy, mysql-connector
from typing import Any, Iterator
from urllib.parse import quote
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session


class GlobalData:
    db_session_maker: Any
    db_engine: Any
    autocommit: bool


global_data = GlobalData()


def init(*, protocol='mysql+mysqlconnector', username=None, password=None, host=None, port:int=None, database=None,
         echo:bool=True, autoflush=True, autocommit=False):
    engine = create_engine(
        '{protocol}://{username}:{password}@{host}:{port}/{database}'.format(
            protocol=protocol, username=quote(username), password=quote(password),
            host=host, port=port, database=database
        ),
        pool_recycle=3600
    )
    engine.echo = echo
    global_data.db_session_maker = scoped_session(sessionmaker(
        autoflush=autoflush, autocommit=autocommit, bind=engine))
    global_data.db_engine = engine
    global_data.autocommit = autocommit



@contextmanager
def make_session() -> Iterator[Session]:
    session: Session = global_data.db_session_maker()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()