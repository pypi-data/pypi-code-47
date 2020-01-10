from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

import datetime

DEFAULT_DB_NAME = 'tritise.sqlite'

class NotConnectedError(Exception):
    pass

def require_cursor(f):
    def wrapper(*args):
        s = args[0]
        if not s.cursor:
            raise NotConnectedError()
        return f(*args)
    return wrapper

Base = declarative_base()

class TritiseEntry(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key = True)
    timestamp = Column(DateTime, server_default=func.now())
    value = Column(Float, nullable=False)
    tag = Column(String)

    def __repr__(self):
        return '{}: {:>8.2f} {}'.format(self.timestamp, self.value, '[%s]' % self.tag if self.tag else '')

class Tritise(object):
    def __init__(self, filename = DEFAULT_DB_NAME, engine = None):
        """Without an engine and a filename a sqlite connection is assumed"""
        self._filename = filename
        self._engine = engine
        if self._engine is None:
            self._engine = create_engine('sqlite:///%s' % filename)
        Base.metadata.create_all(self._engine)
        self._sessionmaker = sessionmaker(bind=self._engine)
        self._session = self._sessionmaker()

    def add(self, value, tag = None, timestamp = None):
        """
        Add a data point with an optional tag to the time series.
        The entry is returned on success, None otherwise
        """
        t = TritiseEntry(value = value, tag = tag)
        if (timestamp):
            t.timestamp = timestamp
        self._session.add(t)
        self._session.commit()
        return t if t.id else None

    def add_many(self, data, tag = None):
        """
        Allows to add many existing data points with an optional tag.
        data must be an array of dicts with `value` and `timestamp` fields
        or behave like one
        """
        for point in data:
            point_tag = tag
            if 'tag' in point:
                point_tag = point['tag']
            t = TritiseEntry(value=point['value'], tag=point_tag, timestamp=point['timestamp'])
            self._session.add(t)
        return self._session.commit()

    def all(self, tag = None):
        return self._session.query(TritiseEntry)\
                   .order_by(TritiseEntry.timestamp.desc(), TritiseEntry.id.desc())\
                   .filter(TritiseEntry.tag == tag)\
                   .all()

    def last(self, tag = None):
        """Retrieve the newest data point for a tag"""
        return self._session.query(TritiseEntry)\
            .filter(TritiseEntry.tag == tag)\
            .order_by(TritiseEntry.timestamp.desc(), TritiseEntry.id.desc())\
            .first()

    def count(self, tag = None):
        """Count all entries with a common tag"""
        return self._session.query(func.count(TritiseEntry.id)).filter(TritiseEntry.tag == tag).scalar()

    def range(self, start_date = None, end_date = None, tag = None):
        """
        Retrieves all entries for a tag in a time range
        """
        query = self._session.query(TritiseEntry)\
                    .order_by(TritiseEntry.timestamp.desc(), TritiseEntry.id.desc())\
                    .filter(TritiseEntry.tag == tag)
        if start_date:
            query = query.filter(TritiseEntry.timestamp >= start_date)
        if end_date:
            query = query.filter(TritiseEntry.timestamp <= end_date)
        return query.all()