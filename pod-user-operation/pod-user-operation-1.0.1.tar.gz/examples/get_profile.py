# coding=utf-8
from pod_base import APIException, PodException

from user_operation import PodUserOperation
from examples.config import *


try:
    access_token = ACCESS_TOKEN
    user_operation = PodUserOperation(API_TOKEN, server_type=SERVER_MODE)
    profile = user_operation.get_user_profile(access_token=access_token, client_id=CLIENT_ID,
                                              client_secret=CLIENT_SECRET)

    print("Profile :\n", profile)

    # OUTPUT
    # Profile :
    #  {'version': 17, 'firstName': 'رضا', 'lastName': 'زارع', 'name': 'reza1607', ...}
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)


