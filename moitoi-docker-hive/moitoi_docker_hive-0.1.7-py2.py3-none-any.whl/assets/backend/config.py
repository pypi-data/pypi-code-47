import os


class BaseConfig(object):
    """
     This is a great place to pass configuration parameters from the
     Environment into your application
    """
    # DB_NAME = os.environ['DB_NAME']
    SECRET_KEY = os.environ.get('SECRET_KEY', '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE')
    pass
