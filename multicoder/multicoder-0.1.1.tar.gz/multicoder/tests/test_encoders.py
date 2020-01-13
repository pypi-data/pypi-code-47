from unittest import TestCase

# noinspection PyPackageRequirements
from hypothesis import given
# noinspection PyPackageRequirements
from hypothesis.strategies import text

from multicoder.encoders import encoders


class TestEncoders(TestCase):
    @given(text())
    def test_decode_inverts_encode(self, text_to_encode):
        for encoder in encoders.values():
            if encoder.decoder is None:
                continue
            encoded_text = encoder.encode(text_to_encode)
            decoded_text = encoder.decode(encoded_text)
            # if decoded_text != text_to_encode:
            #     print(
            #         "%s %r -> %r -> %r"
            #         % (encoder.encode_name, text_to_encode, encoded_text, decoded_text)
            #     )
            if encoder.encode_name == "email.header.Header":
                for k in "\x0b", "\x0c", "\x1c", "\x1d", "\x1e", "\x1f", "\n", "\r", " ", "\t":
                    text_to_encode = text_to_encode.replace(k, "")
                    decoded_text = decoded_text.replace(k, "")
            self.assertEqual(decoded_text, text_to_encode)

    def test_encoders_nfkd(self):
        text_to_encode = "=.$ @# -_—'\" ËæéŦǆϡӾ"
        expected_values = {
            "email.header.Header": "=?utf-8?b?PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpmR6zIzPodO+?=",
            "quopri.encodestring": "=3D.$ @# -_=E2=80=94'\" E=CC=88=C3=A6e=CC=81=C5=A6dz=CC=8C=CF=A1=D3=BE",
            "urllib.parse.quote": "%3D.%24%20%40%23%20-_%E2%80%94%27%22%20E%CC%88%C3%A6e%CC%81%C5%A6dz%CC%8C%CF%A1%D3%BE",
            "urllib.parse.quote_plus": "%3D.%24+%40%23+-_%E2%80%94%27%22+E%CC%88%C3%A6e%CC%81%C5%A6dz%CC%8C%CF%A1%D3%BE",
            "html.escape": "=.$ @# -_—&#x27;&quot; ËæéŦdžϡӾ",
            "shlex.quote": "'=.$ @# -_—'\"'\"'\" ËæéŦdžϡӾ'",
            "base64.b64encode": "PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpmR6zIzPodO+",
            "base64.urlsafe_b64encode": "PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpmR6zIzPodO-",
            "base64.b32encode": "HUXCIICAEMQC2X7CQCKCOIRAIXGIRQ5GMXGIDRNGMR5MZDGPUHJ34===",
            "base64.b16encode": "3D2E24204023202D5FE2809427222045CC88C3A665CC81C5A6647ACC8CCFA1D3BE",
            "base64.a85encode": "4YA!&5U.C'?fHU#-R'[%b_X06A^#_EVIY\"sN6e3H^&",
            "base64.b85encode": "JuW05KqDY6U*dq2Cn6w4%!tFLWz2!areu1|jL)Idz5",
            "hashlib.blake2b": "04bee527537b58cdbaa027fc99a0123711660acb161d22677e725630f7b6e1ad920ec08fac0f77641e9c0bf0d156ceac0dd1054fea6c06cd30cb11efa6bba2f9",
            "hashlib.blake2s": "ffef64578532c36a2aaad60cf58381bb7278350007c75a6bee3e0b395444fc7e",
            "hashlib.md5": "f9e250d2f1a374e165a4ce6257f228b6",
            "hashlib.sha1": "4db573308a17b4b91dd3f9b77217b455fa64c997",
            "hashlib.sha224": "64fc1b33243f2033027b491318c11fe6343bf3a9e8a85b014cd64241",
            "hashlib.sha256": "a4f4675c7c6275470ddefe18b5eb4a677e3a208c079f9c2aa9ca26c1b7820978",
            "hashlib.sha384": "6beac6410bebbf8c04a7b46e96e305613c3ba0418e903fd80c837a6a26c3b7b5ef8207029fb9a2da3fd63a9342cb0ad1",
            "hashlib.sha3_224": "582239199297b0ccb5ede83f6e890121126dde62bc0ab164e2874f7c",
            "hashlib.sha3_256": "c5462eec8eca2af57d4d5c8fc1a378bb24842cf5e6899befb3776deaf8531a7c",
            "hashlib.sha3_384": "f5f86457cf6ae36469866ca1f9cd716326b8b9d1ad8ffc8aa270c210ecf8b832e522ec40c0cb88573ab19be20e11d726",
            "hashlib.sha3_512": "b29bb7cd43f90708b0fa4047076720a684c1cf611af32c7225d0abdf17761e73dedab16c86a6d24adeb69f37d95f2a76a3feeb11f854953e05c06f187e7947d2",
            "hashlib.sha512": "890a3e66632e5df1fc9bf26cc4de94403070cc49f1f3a786c52d058b7315e57131d89d2a5590def1481fbfc93131ffa755ae093d3be34eed074a51fca14294ce",
        }
        for encoder in encoders.values():
            encoded_text = encoder.encode(text_to_encode, normalization="NFKD")
            self.assertEqual(expected_values[encoder.encode_name], encoded_text)

    def test_encoders_nfkc(self):
        text_to_encode = "=.$ @# -_—'\" ËæéŦǆϡӾ"
        expected_values = {
            "email.header.Header": "=?utf-8?b?PS4kIEAjIC1f4oCUJyIgw4vDpsOpxaZkxb7PodO+?=",
            "quopri.encodestring": "=3D.$ @# -_=E2=80=94'\" =C3=8B=C3=A6=C3=A9=C5=A6d=C5=BE=CF=A1=D3=BE",
            "urllib.parse.quote": "%3D.%24%20%40%23%20-_%E2%80%94%27%22%20%C3%8B%C3%A6%C3%A9%C5%A6d%C5%BE%CF%A1%D3%BE",
            "urllib.parse.quote_plus": "%3D.%24+%40%23+-_%E2%80%94%27%22+%C3%8B%C3%A6%C3%A9%C5%A6d%C5%BE%CF%A1%D3%BE",
            "html.escape": "=.$ @# -_—&#x27;&quot; ËæéŦdžϡӾ",
            "shlex.quote": "'=.$ @# -_—'\"'\"'\" ËæéŦdžϡӾ'",
            "base64.b64encode": "PS4kIEAjIC1f4oCUJyIgw4vDpsOpxaZkxb7PodO+",
            "base64.urlsafe_b64encode": "PS4kIEAjIC1f4oCUJyIgw4vDpsOpxaZkxb7PodO-",
            "base64.b32encode": "HUXCIICAEMQC2X7CQCKCOIRAYOF4HJWDVHC2MZGFX3H2DU56",
            "base64.b16encode": "3D2E24204023202D5FE28094272220C38BC3A6C3A9C5A664C5BECFA1D3BE",
            "base64.a85encode": "4YA!&5U.C'?fHU#-R'\\NMo2F0WPt`F`P0Zle%P",
            "base64.b85encode": "JuW05KqDY6U*dq2Cn6xji^HbFsl}#b#lFv>)4l",
            "hashlib.blake2b": "b7872677d7ee540d3604d74b57ea2129649ecaedfc05f82eed2f85770c3613f7b91545ecaa86344851f3ccbbaf790a76aae2dc1d8c3b4ca0447031a29e28b3c2",
            "hashlib.blake2s": "7a51370c23651c41c064f4382ae43e89b08f577c87a515f5f3e0a77c6476d407",
            "hashlib.md5": "437f2b59207051bcea37e6a93ee2e160",
            "hashlib.sha1": "71e10a9e30351e33a7f81fbf984da8a376fdfb66",
            "hashlib.sha224": "cf7f3de9151b04f61cdf1e431d268f9f4727145a6c61752ddf2b36de",
            "hashlib.sha256": "9a5c8bac359e248fb529324d87f421c5f1e8425963514401981e7a9f8ab75b8e",
            "hashlib.sha384": "98a036a5d5f6cf94d2e7d1a01e13de5767b2671c64275af8257960e0055e0c84cb1ba0da90aef46b58acce62b0f2cd43",
            "hashlib.sha3_224": "309ef2d557b0799dc70d25a7efa5fb6176f80d37f72cfc319227dffb",
            "hashlib.sha3_256": "e8be37b61e1c77c2969e9b4f67ba39d06478acc42fb0c159a41b254f233acd72",
            "hashlib.sha3_384": "38d18a2289a13f655560fb61e04d8ea92a7d145dec52f3351243a7a32dad3c6c33e9d07b436b73338bb5a3666bee3dfd",
            "hashlib.sha3_512": "3398e0af7bf000e5dd791c7287c1660673e7d16d954f3e9f7027b29f2b1339b32c2bcb26dbae8aeef825fed4bb080170008e7f11649b824952c5ae7499e09d23",
            "hashlib.sha512": "1e3565b34524f040988a04ba9ffdb1b9e19589318640aeac4395279f9b87fb0e581082459937ea3f47ec8add4709743c80a3d3894fa20bb5875e8c5011b77bab",
        }
        for encoder in encoders.values():
            encoded_text = encoder.encode(text_to_encode, normalization="NFKC")
            self.assertEqual(expected_values[encoder.encode_name], encoded_text)

    def test_encoders_nfd(self):
        text_to_encode = "=.$ @# -_—'\" ËæéŦǆϡӾ"
        expected_values = {
            "email.header.Header": "=?utf-8?b?PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpseGz6HTvg==?=",
            "quopri.encodestring": "=3D.$ @# -_=E2=80=94'\" E=CC=88=C3=A6e=CC=81=C5=A6=C7=86=CF=A1=D3=BE",
            "urllib.parse.quote": "%3D.%24%20%40%23%20-_%E2%80%94%27%22%20E%CC%88%C3%A6e%CC%81%C5%A6%C7%86%CF%A1%D3%BE",
            "urllib.parse.quote_plus": "%3D.%24+%40%23+-_%E2%80%94%27%22+E%CC%88%C3%A6e%CC%81%C5%A6%C7%86%CF%A1%D3%BE",
            "html.escape": "=.$ @# -_—&#x27;&quot; ËæéŦǆϡӾ",
            "shlex.quote": "'=.$ @# -_—'\"'\"'\" ËæéŦǆϡӾ'",
            "base64.b64encode": "PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpseGz6HTvg==",
            "base64.urlsafe_b64encode": "PS4kIEAjIC1f4oCUJyIgRcyIw6ZlzIHFpseGz6HTvg==",
            "base64.b32encode": "HUXCIICAEMQC2X7CQCKCOIRAIXGIRQ5GMXGIDRNGY6DM7IOTXY======",
            "base64.b16encode": "3D2E24204023202D5FE2809427222045CC88C3A665CC81C5A6C786CFA1D3BE",
            "base64.a85encode": "4YA!&5U.C'?fHU#-R'[%b_X06A^#_EVT4G;U!p^",
            "base64.b85encode": "JuW05KqDY6U*dq2Cn6w4%!tFLWz2!arpJcQq0_z",
            "hashlib.blake2b": "60e8f76c667eec97ef442f989469070d5ac7c5fcea8f8df1233b815f05df50bff5ad944cbeff40e002e4e933ec90b7801420436014109057f80022792538418d",
            "hashlib.blake2s": "659750ae7f453061e54deaca590315750091aec455896f21fb17e4b14ee44c50",
            "hashlib.md5": "3840b88f91f18e9018b2d3ca730fedda",
            "hashlib.sha1": "6f6b2d58b43ad24e7b691404720440abbad750c0",
            "hashlib.sha224": "a86471842e9e65c3e4318c6929de87b61471e9cb47a01ed185a834a7",
            "hashlib.sha256": "31e08dc4fb3049b297a2e9989f73e28ceb30047c47eaf48684e342a4e9bcaeb1",
            "hashlib.sha384": "810dba87b03dd0d522ba94b8e0a8dce006af6e65350e9bf88db094759e78cecd6a5dfaf362892f206c971bb62be71bba",
            "hashlib.sha3_224": "3a2ab138841502f737ef399899d25aa3287f4c25b0d2692a7722fbb6",
            "hashlib.sha3_256": "d36a8769203f71cd97ec5a2a8052abf45715030042a723ad9f9cdd47e26aa38c",
            "hashlib.sha3_384": "d70b5ed39bcc5e0b65a43a44968955c6155596ae01cdb87b4be0f0d8155390f705e9fa1b97a8d051ddd5e76fdad24d14",
            "hashlib.sha3_512": "fea9f10287749bf153ebfa6c83d818e9499498912922a982b82c2ea87bc95531e189e265c6bec9b5dd08e8846bec52e481d9a89ab9cca42ff8bb45e41f8b3c54",
            "hashlib.sha512": "6a45eb124854bc2e9c131835b1b6d10ee8a364db34b15d66acf8122a501a2a4627b808268296d4baebee5b211ecea0635273074b1dd2a79d9b48c058ba5578ec",
        }

        for encoder in encoders.values():
            encoded_text = encoder.encode(text_to_encode, normalization="NFD")
            self.assertEqual(expected_values[encoder.encode_name], encoded_text)

    def test_encoders_nfc(self):
        text_to_encode = "=.$ @# -_—'\" ËæéŦǆϡӾ"
        expected_values = {
            "email.header.Header": "=?utf-8?b?PS4kIEAjIC1f4oCUJyIgw4vDpsOpxabHhs+h074=?=",
            "quopri.encodestring": "=3D.$ @# -_=E2=80=94'\" =C3=8B=C3=A6=C3=A9=C5=A6=C7=86=CF=A1=D3=BE",
            "urllib.parse.quote": "%3D.%24%20%40%23%20-_%E2%80%94%27%22%20%C3%8B%C3%A6%C3%A9%C5%A6%C7%86%CF%A1%D3%BE",
            "urllib.parse.quote_plus": "%3D.%24+%40%23+-_%E2%80%94%27%22+%C3%8B%C3%A6%C3%A9%C5%A6%C7%86%CF%A1%D3%BE",
            "html.escape": "=.$ @# -_—&#x27;&quot; ËæéŦǆϡӾ",
            "shlex.quote": "'=.$ @# -_—'\"'\"'\" ËæéŦǆϡӾ'",
            "base64.b64encode": "PS4kIEAjIC1f4oCUJyIgw4vDpsOpxabHhs+h074=",
            "base64.urlsafe_b64encode": "PS4kIEAjIC1f4oCUJyIgw4vDpsOpxabHhs-h074=",
            "base64.b32encode": "HUXCIICAEMQC2X7CQCKCOIRAYOF4HJWDVHC2NR4GZ6Q5HPQ=",
            "base64.b16encode": "3D2E24204023202D5FE28094272220C38BC3A6C3A9C5A6C786CFA1D3BE",
            "base64.a85encode": "4YA!&5U.C'?fHU#-R'\\NMo2F0WPtaTL<lRB^&",
            "base64.b85encode": "JuW05KqDY6U*dq2Cn6xji^HbFsl}$phR>nXz5",
            "hashlib.blake2b": "68c71ebf1aa4713e6b32b8b1b68e5f05b1b457139f9562e0eebec0460ba2e14f81c49f2b08bc92867459ef156921633c40b6b6fc5466b5709bab0c02e94103c9",
            "hashlib.blake2s": "12baf117d5fa1fc38ed0be718861a7cbfbfbf06bd69db53f93e332af5fd9b619",
            "hashlib.md5": "e7c8c75a8f67cbda9b6173ac5bcd7a15",
            "hashlib.sha1": "f069402ba89ab1caca097e7c1aa27a8a05f331d1",
            "hashlib.sha224": "c304ff4c88004ff0273be8d9a2231ab652cea04ac93486514e0447e5",
            "hashlib.sha256": "1381513b7adee94157ef284d33f62be2c86222f9717cbdc63a193d29cfeb820a",
            "hashlib.sha384": "cb4a46a9358d2b30e05b7ab69b75b3a46129997899565a2a6eb3b3f3a3b2daacee3b683e8cffc2845b61b9e51d12f940",
            "hashlib.sha3_224": "362ce776d2843755e649458d10a30616cf65c6b2cd0bfb3b40c37b71",
            "hashlib.sha3_256": "def72158d066c371495ebf3789f2124bb707d8a37fc082e42ca99e1e4670d085",
            "hashlib.sha3_384": "66bd443e347685b6be1333de43e18484be60e017b77211e98b9e93ba6fbbc7d93bcf731de642735334bdb5702509485f",
            "hashlib.sha3_512": "bc03a10430ae7b1f98c9582102f0481c1e4a12795c27cbe863a2b4fa0771aa036a5960953695be1e7c36bb5155e7bb6223108f8ebb0405892b4733eca0f42ada",
            "hashlib.sha512": "87e0244047f13c8af1acbe72f28d0343e6d09311a43cf19d32acc1ebd419ac17eaefee6f740221d6a3a6a2b078ccc1295e37c3b0682dea9cf8e8d717be2231ba",
        }
        for encoder in encoders.values():
            encoded_text = encoder.encode(text_to_encode, normalization="NFC")
            self.assertEqual(expected_values[encoder.encode_name], encoded_text)
