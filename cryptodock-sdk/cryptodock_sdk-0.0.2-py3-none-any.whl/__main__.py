from .cryptodock_sdk import CryptoDockSdk

def prove_instance() :
    print('Package Instance Test: ', CryptoDockSdk(base="localhost", port=5000, version="v1"))

if __name__ == '__main__':
    prove_instance()
