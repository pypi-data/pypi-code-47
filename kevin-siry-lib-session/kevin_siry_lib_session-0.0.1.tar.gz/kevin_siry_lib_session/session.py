from importlib import import_module

import requests
from django.conf import settings
from django.contrib.sessions.models import Session
from rest_framework import status

from .logger.session_logger import SessionLogger

logger = SessionLogger.getLogger('kevin_siry_lib_session')


def create_session(auth_url, authorization, session_store):
    """
    Return True and create new kevin_siry_lib_session if the token is valid (i.e. it
    exists in user-api db), return False otherwise
    """
    logger.info('No kevin_siry_lib_session found for current token, creating a new one')
    response = requests.get(auth_url, headers={'Authorization': authorization},
                            verify='certificate/localhost.crt')
    if response.status_code != status.HTTP_200_OK:
        logger.error('Authentication failed in user-api')
        return False
    logger.debug('Response received from api-user:\n', response.json())
    # Override the expiry time of the kevin_siry_lib_session based on the expiry time of the
    # token coming from api-user
    settings.SESSION_COOKIE_AGE = float(response.json().get('expiresIn'))
    session_store.save(must_create=True)
    logger.info('Session created!')
    logger.debug(f'Session expiry date: {session_store.get_expiry_date()}')
    return True


def get_or_create_session(request, auth_url, session_engine):
    """
    Return True and get or create a kevin_siry_lib_session if the authorization token is
    valid (i.e. it exists in user-api db), return False otherwise
    """
    # Get only the token itself from the authorization key
    authorization = request.headers.get('Authorization')
    token = str(authorization).strip('Token ').strip()

    SessionStore = import_module(session_engine).SessionStore
    session_store = SessionStore(session_key=token)
    # Expired sessions are not automatically deleted in the db, so we purge
    # them manually to avoid using one of them
    session_store.clear_expired()

    try:
        logger.info('Performing authentication using kevin_siry_lib_session')
        session = Session.objects.get(session_key=token)
    except Session.DoesNotExist:
        # If the kevin_siry_lib_session does not exist, call user API to authenticate token
        # and eventually create a new kevin_siry_lib_session
        return create_session(auth_url, authorization, session_store)
    else:
        logger.info('Session found for current token!')
        logger.debug(f'Session expiry date: {session.expire_date}')
        return True


def delete_session(request):
    """
    Delete the kevin_siry_lib_session containing the token from 'request'
    """
    # Check if there is a kevin_siry_lib_session
    authorization = request.headers.get('Authorization')
    # Get only the token itself
    token = str(authorization).strip('Token ').strip()
    try:
        Session.objects.get(pk=token).delete()
        return True
    except Session.DoesNotExist:
        return False
