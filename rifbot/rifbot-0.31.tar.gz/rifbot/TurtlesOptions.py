from .EngineOptions import EngineOptions
from .StrategyOptions import StrategyOptions
from .JsonHelpers import options_to_json

class TurtlesOptions:
    def __init__(self):
        # self.name = name
        self.engine = EngineOptions()
        # self.indicators_options = IndicatorsOptions()
        self.S1 = StrategyOptions()
        self.S2 = StrategyOptions()

    def to_json(self):
        return options_to_json(self)
