# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException

from user_operation import PodUserOperation
from examples.config import *
from platform import python_version

print("Python", python_version())
try:
    access_token = ACCESS_TOKEN
    CODE = "2004360"
    MOBILE = "0937*****41"

    user_operation = PodUserOperation(API_TOKEN, server_type=SERVER_MODE)

    confirm = user_operation.edit_confirm_profile(access_token=access_token, code=CODE, cell_phone_number=MOBILE)
    print("Confirm :\n", confirm)
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
