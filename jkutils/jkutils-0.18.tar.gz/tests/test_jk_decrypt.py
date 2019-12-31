import datetime

from jkutils.jk_decrypt import CoreCrypt, CryptoRsa


def test_encrypt():
    a = CoreCrypt()
    body = {"data": {'certType': '01',
                     'certNo': '522623198706237606',
                     'address': '云南省曲靖市南苑小区',
                     'custName': '李明',
                     'loanAmount': '1000000',
                     'mobile': '18623451234',
                     'creditLimit': '1000000',
                     'businessNo': '10080000353100873225489139797243',
                     'applyNo': '6b2879e627cb11eaac87787b8ae13052',
                     'register_mobile': '18623451234'
                     },
            "mchtNo": "00000000",
            "version": "1.0",
            "reqTime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
    new_body = a.run(body, "data", "./sn_test_encrypt.pem")
    print(new_body)
    assert new_body


def test_decrypt_public():
    """测试公钥解密"""
    res = {"returnCode": "0", "returnMsg": "成功", "respTime": "2019-12-31 16:56:11",
           "sign": "NDY4NjliYzRhNGY4MjhmNDJlNzBiMDJiMDc2YWRjMGNhYWFhNWRlNmI1OTI1OWMyYTY4MWQzYjg4NWMxMjMzZQ==",
           "data": "K2A1+yf0JXXjGhyT5RfeyRD+cYEjbMHXv0OcmYo9UEQJB9MKXEA8iRhobm19iEE3",
           "randomKey": "W2UhXxG9qzU12aRUbXR/q04TaFQPrs4pUzJFm1kcMvIGxnnDBQoyCfX67CcUChKmdtrb2hoKYARl9hZLjPWkt/VxRqxzAuo+tdlyJcEzzy+wgfWjzgfQRiWzMDh2tVLkgXsamgr1s7IX4MsyPmrO6SaCY7Iq0GSoj9NLhIm44JZT0g/AKjygaLLgLLFmqdM8CcpXpf8CuMfu9OTRz42RFNl2MpuLjiLkT0Mwd7vVmNXell2+flj8O5Xn2uNRqMrfYEJRJJBZtip/CL2UcqfNT52YSBEPTB8j+abOl6YGBQPRkeaqhOlHRW5i6WYvTcJk7MrTiSI7AkhLnC+pmfQw8g=="}
    a = CoreCrypt()
    data = a.decrypt_public("./sn_test_public.pem", res["randomKey"], res["data"], res["sign"], res)
    print(data)
    assert data


def test_decrypt_private():
    """测试私钥解密"""
    res = {"returnCode": "0", "returnMsg": "成功", "respTime": "2019-12-31 16:55:00",
           "sign": "OGJjZjYzZTI4ZTYzNjVjZGM2NDJkZTM4OTI3MjkyZjAxY2FkMzhiYTM2ZWEwZTBiZjM4MGVmYmRhY2M0ZDIyZQ==",
           "data": "X+KM6s3r+tJq7PiUDO7YSnBkVzXamF9BGIAueVkXSBs1XiZWNkYHeYmWNOOePk+X",
           "randomKey": "dl8UuU15g9FNOmNf4s021ulenEmIu0MkOemxhhoFmhB6rxkfi25KnJdZ8dA4UWUBsMFLNWQsIV54l7GdPr+AtyV8M0wX3N7+iSK/SFPQchWMreSo0w6xRXBOFEUcge03pA6BkKPX2M7vcA5UNKEtSZ0P/BgqmV5VawypjFD5DscuCaflpxggyS+dtmu+aKH8EMIU3OXykZqyqvONCP5sA7HnpT6z8Z5Eiw5UvmzTln/SevC7LJxM5RUoUrvN3MnIzgUR8ugwv1rJghQcemtf0L8UHMnZrS8r1RMl2EqTEKQ80JrvUUk+hK2Hmfq6vimL39l8bgAKY20uih++njQfEg=="}
    a = CoreCrypt()
    data = a.decrypt_private("./sn_test_encrypt.pem", res["randomKey"], res["data"], res["sign"], res)
    print(data)
    assert data
