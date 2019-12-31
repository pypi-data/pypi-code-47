# -*- coding: utf-8 -*-
import hashlib
import json
import binascii
import base64
import time

from passlib.utils.pbkdf2 import pbkdf2

from privacyidea.lib.utils import b32encode_and_unicode
from privacyidea.lib.policy import set_policy, SCOPE, delete_policy
from .base import MyApiTestCase
from privacyidea.lib.tokens.HMAC import HmacOtp


class TwoStepInitTestCase(MyApiTestCase):
    """
    test the 2stepinit process.
    
    Here we enroll an HOTP token. One part of the secret key is generated by 
    privacyIDEA and the second part is generated by the client.
    
    A successful authentication with the new key is performed.
    """

    def test_01_init_token(self):
        set_policy(
            name="allow_2step",
            action=["hotp_2step=allow", "enrollHOTP=1", "delete"],
            scope=SCOPE.ADMIN,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "genkey": "1",
                                                 "2stepinit": "1"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            server_component = binascii.unhexlify(otpkey_url.split("/")[2])
            google_url = detail["googleurl"]["value"]
            self.assertIn('2step_difficulty=10000', google_url)
            self.assertIn('2step_salt=8', google_url)
            self.assertIn('2step_output=20', google_url)
            self.assertEqual(detail['2step_difficulty'], 10000)
            self.assertEqual(detail['2step_salt'], 8)
            self.assertEqual(detail['2step_output'], 20)

        client_component = b"VRYSECRT"
        checksum = hashlib.sha1(client_component).digest()[:4]
        base32check_client_component = b32encode_and_unicode(checksum + client_component).strip("=")

        # Try to do a 2stepinit on a second step will raise an error
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "2stepinit": "1",
                                                 "serial": serial,
                                                 "otpkey": base32check_client_component,
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertEqual(res.status_code, 400)
            result = res.json.get("result")
            self.assertIn('2stepinit is only to be used in the first initialization step',
                          result.get("error").get("message"))

        # Invalid base32check will raise an error
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "2stepinit": "1",
                                                 "serial": serial,
                                                 "otpkey": "A" + base32check_client_component[1:],
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertEqual(res.status_code, 400)
            result = res.json.get("result")
            self.assertIn('Malformed base32check data: Incorrect checksum',
                          result.get("error").get("message"))

        # Authentication does not work yet!
        wrong_otp_value = HmacOtp().generate(key=server_component, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": wrong_otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json
            self.assertTrue(result.get("result").get("status"))
            self.assertFalse(result.get("result").get("value"))
            self.assertEqual(result.get("detail").get("message"),
                             u'matching 1 tokens, Token is disabled')

        # Now doing the correct 2nd step
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "serial": serial,
                                                 "otpkey": base32check_client_component,
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey = otpkey_url.split("/")[2]
            self.assertNotIn('2step', detail)

        # Now try to authenticate
        otpkey_bin = binascii.unhexlify(otpkey)
        otp_value = HmacOtp().generate(key=otpkey_bin, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        # Check that the OTP key is what we expected it to be
        expected_secret = pbkdf2(binascii.hexlify(server_component), client_component, 10000, 20)
        self.assertEqual(otpkey_bin, expected_secret)

        with self.app.test_request_context('/token/'+ serial,
                                           method='DELETE',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
        delete_policy("allow_2step")

    def test_02_force_parameters(self):
        set_policy(
            name="force_2step",
            action=["hotp_2step=force", "enrollHOTP=1", "delete"],
            scope=SCOPE.ADMIN,
        )
        set_policy(
            name="2step_params",
            action=["hotp_2step_difficulty=12345",
                    "hotp_2step_serversize=33",
                    "hotp_2step_clientsize=11"],
            scope=SCOPE.ENROLL,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "genkey": "1",
                                                 "2stepinit": "0", # will be forced nevertheless
                                                 "2step_serversize": "3",
                                                 "2step_clientsize": "4",
                                                 "2step_difficulty": "33333"
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            server_component = binascii.unhexlify(otpkey_url.split("/")[2])
            google_url = detail["googleurl"]["value"]
            self.assertIn('2step_difficulty=12345', google_url)
            self.assertIn('2step_salt=11', google_url)
            self.assertIn('2step_output=20', google_url)
        # Authentication does not work yet!
        wrong_otp_value = HmacOtp().generate(key=server_component, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": wrong_otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json
            self.assertTrue(result.get("result").get("status"))
            self.assertFalse(result.get("result").get("value"))
            self.assertEqual(result.get("detail").get("message"),
                         u'matching 1 tokens, Token is disabled')

        client_component = b"wrongsize" # 9 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Supply a client secret of incorrect size
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 400, res)
            result = res.json.get("result")
            self.assertFalse(result.get("status"))

        client_component = b"correctsize" # 11 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Now doing the correct 2nd step
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 "2step_serversize": "3", # will have no effect
                                                 "2step_clientsize": "4",
                                                 "2step_difficulty": "33333"
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey = otpkey_url.split("/")[2]

        # Now try to authenticate
        otpkey_bin = binascii.unhexlify(otpkey)
        otp_value = HmacOtp().generate(key=otpkey_bin, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        # Check serversize
        self.assertEqual(len(server_component), 33)
        # Check that the OTP key is what we expected it to be
        expected_secret = pbkdf2(binascii.hexlify(server_component), client_component, 12345, 20)
        self.assertEqual(otpkey_bin, expected_secret)

        with self.app.test_request_context('/token/'+ serial,
                                           method='DELETE',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)

        delete_policy("force_2step")
        delete_policy("2step_params")

    def test_03_custom_parameters(self):
        set_policy(
            name="enrollhotp",
            action=["enrollHOTP=1", "delete", "hotp_2step=allow"],
            scope=SCOPE.ADMIN,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "genkey": "1",
                                                 "2stepinit": "1",
                                                 "2step_serversize": "5",
                                                 "2step_clientsize": "16",
                                                 "2step_difficulty": "17898",
                                                 "hashlib": "sha512", # force 64-byte secret
                                                 "otplen": "8",
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            server_component = binascii.unhexlify(otpkey_url.split("/")[2])

        client_component = b"wrongsize0" # 10 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Supply a client secret of incorrect size
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 400, res)
            result = res.json.get("result")
            self.assertFalse(result.get("status"))

        client_component = b"correctsizeABCDE" # 16 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Now doing the correct 2nd step
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 "2step_serversize": "3", # will have no effect
                                                 "2step_clientsize": "4",
                                                 "2step_difficulty": "33333"
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey = otpkey_url.split("/")[2]

        # Now try to authenticate
        otpkey_bin = binascii.unhexlify(otpkey)
        otp_value = HmacOtp(digits=8, hashfunc=hashlib.sha512).generate(key=otpkey_bin, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        # Check serversize
        self.assertEqual(len(server_component), 5)
        # Check that the OTP key is what we expected it to be
        expected_secret = pbkdf2(binascii.hexlify(server_component), client_component, 17898, 64)
        self.assertEqual(otpkey_bin, expected_secret)

        with self.app.test_request_context('/token/'+ serial,
                                           method='DELETE',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)

        delete_policy("enrollhotp")

    def test_04_no_2stepinit(self):
        set_policy(
            name="disallow_2step",
            action=["enrollHOTP=1", "delete"], # no 2step policy => disallow by default
            scope=SCOPE.ADMIN,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "hotp",
                                                 "genkey": "1",
                                                 "2stepinit": "1",
                                                 # will be ignored
                                                 "2step_serversize": "5",
                                                 "2step_clientsize": "16",
                                                 "2step_difficulty": "17898",
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey_bin = binascii.unhexlify(otpkey_url.split("/")[2])
            self.assertEqual(detail.get("rollout_state"), "")

        # Now try to authenticate
        otp_value = HmacOtp().generate(key=otpkey_bin, counter=1)
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        delete_policy("disallow_2step")

    def test_05_init_totp_token(self):
        set_policy(
            name="allow_2step",
            action=["totp_2step=allow", "enrollTOTP=1", "delete"],
            scope=SCOPE.ADMIN,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "genkey": "1",
                                                 "2stepinit": "1"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            server_component = binascii.unhexlify(otpkey_url.split("/")[2])
            google_url = detail["googleurl"]["value"]
            self.assertIn('2step_difficulty=10000', google_url)
            self.assertIn('2step_salt=8', google_url)
            self.assertIn('2step_output=20', google_url)
            self.assertEqual(detail['2step_difficulty'], 10000)
            self.assertEqual(detail['2step_salt'], 8)
            self.assertEqual(detail['2step_output'], 20)

        client_component = b"VRYSECRT"
        checksum = hashlib.sha1(client_component).digest()[:4]
        base32check_client_component = base64.b32encode(checksum + client_component).strip(b"=")

        # Try to do a 2stepinit on a second step will raise an error
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "2stepinit": "1",
                                                 "serial": serial,
                                                 "otpkey": base32check_client_component,
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertEqual(res.status_code, 400)
            result = res.json.get("result")
            self.assertIn('2stepinit is only to be used in the first initialization step',
                          result.get("error").get("message"))

        # Invalid base32check will raise an error
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "2stepinit": "1",
                                                 "serial": serial,
                                                 "otpkey": b"A" + base32check_client_component[1:],
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertEqual(res.status_code, 400)
            result = res.json.get("result")
            self.assertIn('Malformed base32check data: Incorrect checksum',
                          result.get("error").get("message"))

        # Authentication does not work yet!
        wrong_otp_value = HmacOtp().generate(key=server_component, counter=int(time.time() // 30))
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": wrong_otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json
            self.assertTrue(result.get("result").get("status"))
            self.assertFalse(result.get("result").get("value"))
            self.assertEqual(result.get("detail").get("message"),
                         u'matching 1 tokens, Token is disabled')

        # Now doing the correct 2nd step
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "serial": serial,
                                                 "otpkey": base32check_client_component,
                                                 "otpkeyformat": "base32check"},
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey = otpkey_url.split("/")[2]
            self.assertNotIn('2step', detail)

        # Now try to authenticate
        otpkey_bin = binascii.unhexlify(otpkey)
        otp_value = HmacOtp().generate(key=otpkey_bin, counter=int(time.time() // 30))
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        # Check that the OTP key is what we expected it to be
        expected_secret = pbkdf2(binascii.hexlify(server_component), client_component, 10000, 20)
        self.assertEqual(otpkey_bin, expected_secret)

        with self.app.test_request_context('/token/'+ serial,
                                           method='DELETE',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
        delete_policy("allow_2step")

    def test_06_force_totp_parameters(self):
        set_policy(
            name="force_2step",
            action=["totp_2step=force", "enrollTOTP=1", "delete"],
            scope=SCOPE.ADMIN,
        )
        set_policy(
            name="2step_params",
            action=["totp_2step_difficulty=12345",
                    "totp_2step_serversize=33",
                    "totp_2step_clientsize=11"],
            scope=SCOPE.ENROLL,
        )
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "genkey": "1",
                                                 "2stepinit": "0", # will be forced nevertheless
                                                 "2step_serversize": "3",
                                                 "2step_clientsize": "4",
                                                 "2step_difficulty": "33333",
                                                 "timeStep": "60",
                                                 "hashlib": "sha512",
                                                 "otplen": "8",
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            serial = detail.get("serial")
            otpkey_url = detail.get("otpkey", {}).get("value")
            server_component = binascii.unhexlify(otpkey_url.split("/")[2])
            google_url = detail["googleurl"]["value"]
            self.assertIn('2step_difficulty=12345', google_url)
            self.assertIn('2step_salt=11', google_url)
            self.assertIn('2step_output=64', google_url)
        # Authentication does not work yet!
        wrong_otp_value = HmacOtp(digits=8,
                                  hashfunc=hashlib.sha512).generate(key=server_component,
                                                                    counter=int(time.time() // 60))
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": wrong_otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json
            self.assertTrue(result.get("result").get("status"))
            self.assertFalse(result.get("result").get("value"))
            self.assertEqual(result.get("detail").get("message"),
                         u'matching 1 tokens, Token is disabled')

        client_component = b"wrongsize" # 9 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Supply a client secret of incorrect size
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 400, res)
            result = res.json.get("result")
            self.assertFalse(result.get("status"))

        client_component = b"correctsize" # 11 bytes
        hex_client_component = binascii.hexlify(client_component)

        # Now doing the correct 2nd step
        with self.app.test_request_context('/token/init',
                                           method='POST',
                                           data={"type": "totp",
                                                 "serial": serial,
                                                 "otpkey": hex_client_component,
                                                 "2step_serversize": "3", # will have no effect
                                                 "2step_clientsize": "4",
                                                 "2step_difficulty": "33333"
                                                 },
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertTrue(result.get("status") is True, result)
            self.assertTrue(result.get("value") is True, result)
            detail = res.json.get("detail")
            otpkey_url = detail.get("otpkey", {}).get("value")
            otpkey = otpkey_url.split("/")[2]

        # Now try to authenticate
        otpkey_bin = binascii.unhexlify(otpkey)
        otp_value = HmacOtp(digits=8,
                            hashfunc=hashlib.sha512).generate(key=otpkey_bin,
                                                              counter=int(time.time() // 60))
        with self.app.test_request_context('/validate/check',
                                           method='POST',
                                           data={"serial": serial,
                                                 "pass": otp_value}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.json.get("result")
            self.assertEqual(result.get("status"), True)
            self.assertEqual(result.get("value"), True)

        # Check serversize
        self.assertEqual(len(server_component), 33)
        # Check that the OTP key is what we expected it to be
        expected_secret = pbkdf2(binascii.hexlify(server_component), client_component, 12345, 64)
        self.assertEqual(otpkey_bin, expected_secret)

        with self.app.test_request_context('/token/'+ serial,
                                           method='DELETE',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)

        delete_policy("force_2step")
        delete_policy("2step_params")
