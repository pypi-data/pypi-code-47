# 初始化连接对象
import base64
import datetime
import hashlib
import json
import os
import uuid
from collections import OrderedDict
from urllib.parse import quote, unquote

import M2Crypto
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5, AES
from Crypto.PublicKey import RSA


class CryptoException(Exception):
    """加解密异常"""
    pass


class CryptoAES:
    def __init__(self, key, iv=None, mode=None, block_size=None, use_quote=False):
        try:
            self.key = key.encode()
            self.iv = iv.encode() if iv else key
        except Exception as e:
            self.key = key
            self.iv = iv if iv else key
        self.mode = AES.MODE_ECB if mode is None else mode
        self.bs = AES.block_size if block_size is None else block_size
        self.use_quote = use_quote

    def pad(self, s):
        return s.decode() + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def un_pad(s):
        return s[0:-ord(s[-1])]

    @staticmethod
    def add_to_16(text):

        length = 16
        count = len(text.encode())
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        text = '{0}{1}'.format(text, '\0' * add)
        return text

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        if self.mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB, AES.MODE_OPENPGP]:
            cryptor = AES.new(self.key, self.mode, self.iv)
        else:
            cryptor = AES.new(self.key, self.mode)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        text = self.pad(text.encode())
        ciphertext = cryptor.encrypt(text.encode())
        result = base64.b64encode(ciphertext)
        final_result = quote(result) if self.use_quote else result
        return final_result
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        # return b2a_hex(ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        if self.mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB, AES.MODE_OPENPGP]:
            cryptor = AES.new(self.key, self.mode, self.iv)
        else:
            cryptor = AES.new(self.key, self.mode)
        # plain_text = cryptor.decrypt(a2b_hex(text)).decode()
        text = unquote(text) if self.use_quote else text
        plain_text = cryptor.decrypt(base64.b64decode(text)).decode()
        plain_text = self.un_pad(plain_text)
        return plain_text.rstrip('\0')


class CryptoRsa:
    def __init__(self, public_key_path, private_key_path):
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        self.random_generator = Random.new().read

    def encrypt_public(self, text):
        with open(self.public_key_path) as f:
            key = f.read()
            rsa_key = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsa_key)
            cipher64_text = base64.b64encode(cipher.encrypt(text))
        return cipher64_text

    def decrypt_private(self, cipher64_text):
        with open(self.private_key_path) as f:
            key = f.read()
            rsa_key = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsa_key)
            text = cipher.decrypt(base64.b64decode(cipher64_text), self.random_generator)
        return text

    def encrypt_private(self, text, pad=None):
        rsa_pri = M2Crypto.RSA.load_key(self.private_key_path)
        pad = M2Crypto.RSA.pkcs1_padding if pad is None else pad
        en_pri_text = rsa_pri.private_encrypt(text, pad)  # 这里的方法选择加密填充方式，所以在解密的时候 要对应。
        en_pri64_text = base64.b64encode(en_pri_text)  # 密文是base64 方便保存 encode成str
        return en_pri64_text

    def decrypt_public(self, en_pri64_text, pad=None):
        rsa_pub = M2Crypto.RSA.load_pub_key(self.public_key_path)
        en_pri_text = base64.b64decode(en_pri64_text)  # 先将str转成base64
        pad = M2Crypto.RSA.pkcs1_padding if pad is None else pad
        text = rsa_pub.public_decrypt(en_pri_text, pad)  # 解密
        return text


class GenRsa:
    @staticmethod
    def run_random(path):
        # 利用伪随机数来生成私钥和公钥
        random_generator = Random.new().read
        rsa = RSA.generate(2048, random_generator)
        private_pem = rsa.exportKey()
        f = open(f'{path}/MY_KEY1_pri.pem', 'wb')
        f.write(private_pem)
        f.close()

        public_pem = rsa.publickey().exportKey()
        f = open(f'{path}/MY_KEY1_pub.pem', 'wb')
        f.write(public_pem)
        f.close()

    @staticmethod
    def run(path):
        # 利用默认的generate来生成私钥和公钥
        rsa = RSA.generate(2048)
        private_pem = rsa.exportKey('PEM')
        f = open(f'{path}/MY_KEY2_pri.pem', 'wb')
        f.write(private_pem)
        f.close()

        public_pem = rsa.publickey().exportKey()
        f = open(f'{path}/MY_KEY2_pub.pem', 'wb')
        f.write(public_pem)
        f.close()

    @staticmethod
    def gen_pub_key(pri_path):
        # 根据已有的RSA私钥来生成公钥
        f = open(pri_path, 'rb')
        rsa = RSA.importKey(f.read())
        f.close()

        public_pem = rsa.publickey().exportKey()
        path = os.path.dirname(pri_path)
        f = open(f'{path}/pub.pem', 'wb')
        f.write(public_pem)
        f.close()

    @staticmethod
    def transfer_run(pri_path):
        # 根据已有的RSA PEM格式的私钥来转换成DER格式的私钥
        f = open(pri_path, 'rb')
        rsa = RSA.importKey(f.read())
        f.close()

        private_der = rsa.exportKey('DER')
        path = os.path.dirname(pri_path)
        f = open(f'{path}/pri.der', 'wb')
        f.write(private_der)
        f.close()


class CoreCrypt:
    def __init__(self):
        pass

    @staticmethod
    def gen_random_aes_key():
        # 1.随机生成aesKey 且取16位 转成大写 作为aesKey
        aes_key = uuid.uuid1().hex.upper()[0: 16]
        return aes_key

    @staticmethod
    def make_sorted_params(params: dict):
        """
        params按照key排序
        """
        data = params.items()
        data = sorted(data, key=lambda x: x)
        data = OrderedDict(data)
        return data

    @staticmethod
    def make_sha256(data: str):
        sha256 = hashlib.sha256()
        sha256.update(data.encode())
        res = sha256.hexdigest()
        return res

    def run(self, body: dict, en_key: str, private_key_path: str):
        if "sign" in body:
            body.pop("sign")
        _data = body[en_key]
        _body = body
        aes_key = self.gen_random_aes_key()
        crypto_aes = CryptoAES(aes_key)
        crypto_rsa = CryptoRsa(public_key_path="", private_key_path=private_key_path)
        str_data = json.dumps(_data, ensure_ascii=False)
        en64_aes_data = crypto_aes.encrypt(str_data)
        en64_rsa_key = crypto_rsa.encrypt_private(aes_key.encode())
        _body.update({
            "data": en64_aes_data.decode(),
            "randomKey": en64_rsa_key.decode()
        })
        sorted_body = self.make_sorted_params(_body)
        str_data = json.dumps(sorted_body, separators=(',', ':'), ensure_ascii=False)
        sign = self.make_sha256(str_data)
        sign64 = base64.b64encode(sign.encode())
        _body.update({
            "sign": sign64.decode()
        })
        return _body

    def _decrypt(self, public_key_path: str, private_key_path: str, random_key: str, data: str, sign_from: str, source: dict):
        """
        解密
        :param public_key_path: 公钥路径
        :param private_key_path: 私钥路径（与公钥二选一，传递公钥则通过公钥解密，反之亦然）
        :param random_key: 返回的rsa加密后的随机key
        :param data: 返回的aes加密后的data
        :return:
        """
        # SETUP 0 验证签名是否正确
        source.pop("sign")
        sorted_body = self.make_sorted_params(source)
        str_data = json.dumps(sorted_body, separators=(',', ':'), ensure_ascii=False)
        sign = self.make_sha256(str_data)
        sign64 = base64.b64encode(sign.encode()).decode("utf-8")
        if sign64 != sign_from:
            raise CryptoException("验证签名失败")
        # SETUP 1 通过公钥解密出AES的对称密钥
        if public_key_path:
            r = CryptoRsa(public_key_path, "")
            aes_key = r.decrypt_public(random_key)
        else:
            r = CryptoRsa("", private_key_path)
            aes_key = r.decrypt_private(random_key)
        # SETUP 2 使用上一步获取的AES密钥解密data数据返回
        a = CryptoAES(key=aes_key)
        decrypt_data = a.decrypt(data)
        return decrypt_data

    def decrypt_public(self, public_key_path: str, random_key: str, data: str, sign_from: str, source: dict):
        """
        私钥加密公钥解密
        :param public_key_path: 公钥路径
        :param random_key: 返回的rsa加密后的随机key
        :param data: 返回的aes加密后的data
        :param sign_from: 签名字符串
        :param source: 原始数据字典
        :return:
        """
        return self._decrypt(public_key_path, "", random_key, data, sign_from, source)

    def decrypt_private(self, private_key_path: str, random_key: str, data: str, sign_from: str, source: dict):
        """
        公钥机密私钥解密
        :param private_key_path: 私钥路径
        :param random_key: 返回的rsa加密后的随机key
        :param data: 返回的aes加密后的data
        :param sign_from: 签名字符串
        :param source: 原始数据字典
        :return:
        """
        return self._decrypt("", private_key_path, random_key, data, sign_from, source)


if __name__ == "__main__":
    # ==============
    # g = GenRsa()
    # g.run()
    # ==============
    # ms = "ghjkghjkl"
    # r = CryptoRsa("./MY_KEY2_pub.pem", "./MY_KEY2_pri.pem")
    # encrypt_public = r.encrypt_public(ms)
    # print("encrypt_public======||<", encrypt_public)
    # decrypt_private = r.decrypt_private(encrypt_public)
    # print("decrypt_private======||<", decrypt_private)
    #
    # encrypt_private = r.encrypt_private(ms)
    # print("encrypt_private======||<", encrypt_private)
    # decrypt_public = r.decrypt_public(encrypt_private)
    # print("decrypt_public======||<", decrypt_public)
    # ==============
    #
    #

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
