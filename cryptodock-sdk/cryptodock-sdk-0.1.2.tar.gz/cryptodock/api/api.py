from .controllers import CoinbasePro, Kucoin, Local

class CryptoDockApi :

    def __init__(self, base, port, version) :
        self.base = base
        self.port = port
        self.version = version
        self.uri = "http://{}:{}/api/{}".format(self.base, self.port, self.version)

        self.Local = Local(self.uri)
        self.Kucoin = Kucoin(self.uri)
        self.CoinbasePro = CoinbasePro(self.uri)
