try:
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto import Random
    from Crypto.PublicKey import RSA
except:
    raise ImportError("LoopyCryptor depends on Crypto, "
                      "which was not found, please `pip install pycryptodome`.\n"
                      "If there's still an error, please go to "
                      "https://pycryptodome.readthedocs.io/en/latest/src/installation.html"
                      "to make sure you have successfully install Crypto")

from __main__ import Cryptor