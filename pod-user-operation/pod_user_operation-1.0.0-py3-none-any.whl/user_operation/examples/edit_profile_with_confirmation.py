# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException

from user_operation import PodUserOperation
from examples.config import *
from platform import python_version

print("Python", python_version())
try:
    access_token = ACCESS_TOKEN
    user_operation = PodUserOperation(API_TOKEN, server_type=SERVER_MODE)

    profile = user_operation.get_user_profile(access_token=access_token)
    print("Profile :\n", profile)

    # OUTPUT
    # Profile :
    #  {'version': 17, 'firstName': 'رضا', 'lastName': 'زارع', 'name': 'reza1607', ...}

    data = {
        "firstName": "رضا ویرایش می شود",
        "lastName": profile["lastName"],
        "nickName": profile["nickName"],
    }

    edited = user_operation.edit_profile_with_confirmation(access_token=access_token, params=data)
    print("Edited :\n", edited)

    # OUTPUT
    # Edited :
    #  {'version': 17, 'firstName': 'رضا', 'lastName': 'زارع', 'name': 'reza1607', ...}

    r"""
    Note:
    تغییرات بعد از تایید پیامکی توسط کاربر اعمال می شود
    به همین دلیل از خروجی این متد همان مقادیر قبلی را دریافت می کنید 
    """
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
