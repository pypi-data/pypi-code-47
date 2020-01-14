import ssl
import os
import logging

LOGGER = logging.getLogger(__name__)


def get_ssl_context():
    """
    Constructs SSL context based on environment variables

    If environment variables are missing,
    then no ssl context is returned so the app can run in local mode
    :returns: Properly formatted SSL context or None
    """

    if os.environ['USE_SSL'] == 'False':
        print('No SSL context: Running in Plaintext mode')
        return None

    else:
        ca_file = os.environ['SSL_CA_LOCATION']
        cert_file = os.environ["SSL_CERTIFICATE_LOCATION"]
        key_file = os.environ["SSL_KEY_LOCATION"]
        ssl_context = ssl.create_default_context(
            purpose=ssl.Purpose.SERVER_AUTH,
            cafile=ca_file
        )
        ssl_context.load_cert_chain(
            certfile=cert_file,
            keyfile=key_file
        )
        return ssl_context


def get_config():
    """
    Maps environment variables to Faust app config dictionary

    :return: Faust configs
    :rtype: dict
    """
    config = {
        'id': os.environ['APP_NAME'],
        'broker': os.environ['KAFKA_CLUSTER'],
        'topic_partitions': int(os.environ['TOPIC_PARTITIONS']),
        'topic_replication_factor': int(os.environ['TOPIC_REPLICATION_FACTOR']),
        'processing_guarantee': os.environ['PROCESSING_GUARANTEE'],
        'datadir': f"{os.environ['FAUST_DATADIR_BASE']}/{os.environ['HOSTNAME']}/"
    }

    try:
        config['store'] = os.environ['STORE']
    except KeyError:
        if os.environ['USE_ROCKSDB'] == 'TRUE':
            config['store'] = 'rocksdb://'
        else:
            config['store'] = 'memory://'

    if os.environ['USE_SSL'] == 'True':
        LOGGER.debug('Using SSL Encryption...')
        config.update({'broker_credentials': get_ssl_context()})

    return config
