from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:force1@localhost/sspo2_ontology"
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
#engine = create_engine('sqlite:///sspo.db', echo=True)
session = sessionmaker(bind=engine)
session = session()
Base = declarative_base()

class Config():

    def create_database(self):
        Base.metadata.create_all(engine)

