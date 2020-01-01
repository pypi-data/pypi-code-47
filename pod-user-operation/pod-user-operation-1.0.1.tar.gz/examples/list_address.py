# coding=utf-8
from pod_base import APIException, PodException

from user_operation import PodUserOperation
from examples.config import *


try:
    access_token = ACCESS_TOKEN
    user_operation = PodUserOperation(API_TOKEN, server_type=SERVER_MODE)
    addresses = user_operation.get_list_address(access_token=access_token)

    print("Addresses :\n", addresses)

    # OUTPUT
    # Addresses :
    #  [{'id': 10838, 'address': 'دانشگاه فردوسی', 'city': 'مشهد', 'state': 'خراسان رضوی', 'country': 'ایران', ...]
except APIException as e:
    print("API Exception\nError {0}\nReference Number : {1}".format(e, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e)
