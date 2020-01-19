import pyrebase
import os


config = {
  "apiKey": os.environ.get('API_KEY_FIREBASE'),
  "authDomain": os.environ.get('AUTH_DOMAIN_FIREBASE'),
  "databaseURL": os.environ.get('DATA_BASE_URL_FIREBASE'),
  "storageBucket": os.environ.get('STORAGE_BUCKET_FIREBASE')
}


def connect_firebase():
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    return db