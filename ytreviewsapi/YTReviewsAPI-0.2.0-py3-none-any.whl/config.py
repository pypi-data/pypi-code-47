import os
basedir = os.path.abspath(os.path.dirname(__file__))

#'http://3.210.43.88:8000'

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ytreviewsapi:a@database-2.cvebpou5jr9i.us-east-2.rds.amazonaws.com/ytreviewsapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_URL = 'http://3.210.43.88' 