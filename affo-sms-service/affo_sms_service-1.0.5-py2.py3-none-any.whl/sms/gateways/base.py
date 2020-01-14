class BaseSMSGateway:
    def send(self, to, from_, body):
        raise NotImplementedError()
