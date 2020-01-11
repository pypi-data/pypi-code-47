class StrategyOptions:
    def __init__(self):
        self.enabled = False
        self.enterPeriod = 20
        self.closePeriod = 10
        self.ATRLength = 20
        self.EMALength = 20
        self.pyramiding = 4
        self.NStepUp = 0.5
        self.NStepStop = 2
        self.moneyMngmtPercentage = 0.06
        self.initialCapital = 10000
        self.capitalFloorPercentage = 0.4
        self.hardCapSize = 0.18
        self.repartition = 0.7
