import pytest
import os
from pytezos import pytezos

sandbox_ids = (
    'edsk3gUfUPyBSfrS9CCgmCiQsTCHGkviBDusMxDJstFtojtc1zcpsh',
    'edsk39qAm1fiMjgmPkw1EgQYkMzkJezLNewd7PLNHTkr6w9XA2zdfo',
    'edsk4ArLQgBTLWG5FJmnGnT689VKoqhXwmDPBuGx3z4cvwU9MmrPZZ',
    'edsk2uqQB9AY4FvioK2YMdfmyMrer5R8mGFyuaLLFfSRo8EoyNdht3',
    'edsk4QLrcijEffxV31gGdN2HU7UpyJjA8drFoNcmnB28n89YjPNRFm',
)


class Tezos:
    def __init__(self):
        self.addresses = []
        self.clients = []
        for i in sandbox_ids:
            key = pytezos.key.from_encoded_key(i)
            self.addresses.append(key.public_key_hash())
            host = 'tz' if os.getenv('CI') else 'localhost'
            self.clients.append(pytezos.using(
                key=key,
                shell=f'http://{host}:8732',
            ))

    def wait(self, origination):
        import time
        tries = 15
        while tries:
            try:
                return self.clients[0].shell.blocks[-5:].find_operation(origination['hash'])
            except:
                time.sleep(1)
                tries -= 1
                if not tries:
                    raise

    def contract_address(self, origination):
        result = self.wait(origination)['contents'][0]['metadata']['operation_result']
        return result['originated_contracts'][0]


@pytest.fixture
def tezos():
    return Tezos()
