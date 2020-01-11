from typing import Dict

__all__ = (
    'PACKAGE_STATUS_MAP',
    'HTTP_STATUS_CODE_MAP',
    'ERROR_STATUS_CODE_MAP'
)

PACKAGE_STATUS_MAP: Dict[int, str] = {
    0: "Not Found",
    10: "In Transit",
    20: "Alert",
    30: "Pick up",
    35: "Undelivered",
    40: "Delivered",
    50: "Expired",
}

HTTP_STATUS_CODE_MAP: Dict[int, str] = {
    200: "The request is processed normally, and the returned data needs "
         "to be checked for the specific processing result.",
    401: "Request unauthorized, wrong key, access IP not in whitelist or account disabled.",
    404: "The requested URL address is incorrect.",
    429: "Access frequency exceeds limit.",
    500: "Server Error.",
    503: "Service temporarily unavailable.",
}

ERROR_STATUS_CODE_MAP: Dict[int, str] = {
    0: "Success",
    -18010001: "IP address is not in whitelist.",
    -18010002: "Access token is invalid.",
    -18010003: "Internal service error, please retry later.",
    -18010004: "Account is disabled.",
    -18010005: "Unauthorized access.",
    -18010010: "The field of {0} is required.",
    -18010011: "The value of {0} is invalid.",
    -18010012: "The format of {0} is invalid.",
    -18010013: "Submitted data is invalid.",
    -18010014: "Request limit exceeded.",
    -18019901: "The tracking number {0} has been registered, don't need to repeat registration",
    -18019902: "The tracking number {0} does not register, please register first",
    -18019903: "Carrier cannot be detected.",
    -18019904: "Retrack is not allowed. You can only retrack stopped number.",
    -18019905: "Retrack is not allowed. You can only retrack each number once.",
    -18019906: "Stop tracking is not allowed. You can only stop numbers that are being tracked.",
    -18019907: "Exceeded daily request limit.",
    -18019908: "Quota is not enough for use.",
    -18019909: "No tracking information at this time.",
    -18019910: "The carrier is value {0} is not correct.",
}
