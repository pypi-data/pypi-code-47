from loguru import logger


class EstimatorActor:
    def __init__(self, actor):
        self.actor = actor

    def estimate(self, message):
        logger.info("Actor running its model")
        return message
        #raise NotImplementedError("Should have implemented this")
