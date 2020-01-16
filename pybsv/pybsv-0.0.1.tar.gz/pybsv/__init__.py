from bitsv import Key

MAIN_NETWORK_TYPE = "main"
SCALING_NETWORK_TYPE = "stn"
TEST_NETWORK_TYPE = "test"
SUPPORTED_NETWORKS = [MAIN_NETWORK_TYPE, SCALING_NETWORK_TYPE, TEST_NETWORK_TYPE]

BSV_CURRENCY_KEY = "bsv"
USD_CURRENCY_KEY = "usd"
SUPPORTED_CURRENCIES = [BSV_CURRENCY_KEY, USD_CURRENCY_KEY]

# PyBSV Client Singleton
class PyBSVClient:
    class __PyBSVClient:
        def __init__(self, wif, network):
            if network not in SUPPORTED_NETWORKS:
                raise Exception(
                    f"Unsupported network: {network} please use one of {SUPPORTED_NETWORKS}"
                )
            self.key = Key(wif, network=network)

        def __str__(self):
            return repr(self) + f" Address: {self.key.address}"

    instance = None

    def __init__(self, wif, network):
        if not PyBSVClient.instance:
            PyBSVClient.instance = PyBSVClient.__PyBSVClient(wif, network)
        else:
            PyBSVClient.instance.key = Key(wif, network=network)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def send_bsv(self, address, amount, currency):
        if currency not in SUPPORTED_CURRENCIES:
            raise Exception(
                f"Unsupported currency: {currency} please use one of {SUPPORTED_CURRENCIES}"
            )
        outputs = [(address, amount, currency)]
        trans_id = self.instance.key.send(outputs)
        return trans_id

    def get_balance(self, currency=BSV_CURRENCY_KEY):
        if currency not in SUPPORTED_CURRENCIES:
            raise Exception(
                f"Unsupported currency: {currency} please use one of {SUPPORTED_CURRENCIES}"
            )
        self.instance.key.get_balance(currency)

    def get_address(self):
        return self.instance.key.address
