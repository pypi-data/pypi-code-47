import importlib
# firebase_admin
# from firebase_admin import credentials, firestore
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
import calendar
from datetime import datetime, date

def get_daterange(request, from_date_field = 'after_utc', to_date_field = 'before_utc'):
    from_date = getattr(request, from_date_field, None)
    to_date = getattr(request, to_date_field, None)
    now = timezone.now()

    if from_date is None:
        from_date = "{}-{}-{}".format(now.year, now.month, 1)
    if to_date is None:
        last_day = calendar.monthrange(now.year, now.month)[1]
        to_date = "{}-{}-{}".format(now.year, now.month, last_day)
    return (from_date, to_date)

def get_month(month=None, year=None):
    """
    Given optional month/year, return first and last day of the month as date
    """
    now = date.today()
    if month is None:
        month = now.month
    if year is None:
        year = now.year

    last_day_of_month = calendar.monthrange(year, month)[1]
    start_of_month = date(year, month, 1)
    end_of_month = date(year, month, last_day_of_month)
    return (start_of_month, end_of_month)

# def init_firestore():
#     try:
#         firebase_admin.get_app()
#     except ValueError:
#         path_to_credentials = getattr(settings, 'FIRESTORE_CREDENTIALS_FILE', None)
#         if path_to_credentials is None:
#             raise AssertionError('settings.FIRESTORE_CREDENTIALS_FILE is not defined')

#         cred = credentials.Certificate(path_to_credentials)
#         app = firebase_admin.initialize_app(cred)

#     return firestore.client()

# def push_tags_to_firestore_lookup(tags, practitioner_id, spaces = []):
#     if tags:
#         db = init_firestore()
#         for tag in tags:
#             tag_id = "{}:{}".format(practitioner_id, slugify(tag))
#             data = {
#                 "id": tag_id,
#                 "tag": tag,
#                 "practitioner": practitioner_id,
#                 "spaces": spaces
#             }
#             db.collection('tags').document(tag_id).set(data)
