from dataclasses import dataclass


@dataclass
class ExBestOffersOverrides:
    '''
    Options to alter the default representation of best offer prices
    :param best_prices_depth: The maximum number of
    prices to return on each side for each runner.
     If unspecified defaults to 3.

      Maximum returned price depth returned is 10.
    :param rollup_model: The model to use when rolling
     up available sizes. If unspecified defaults to
     STAKE rollup model with rollupLimit of
      minimum stake in the specified currency.

    :param rollup_limit: The volume limit to use
    when rolling up returned sizes. The exact
    definition of the limit depends on the rollupModel.
    If no limit is provided it will use minimum
    stake as default the value.
    Ignored if no rollup model is specified.

    :param rollup_liability_threshold: Only applicable
    when rollupModel is MANAGED_LIABILITY.
    The rollup model switches from being stake based
     to liability based at the smallest lay
     price which is >= rollupLiabilityThreshold.service
     level default (TBD). Not supported as yet.

    :param rollup_liability_factor: Only applicable
    when rollupModel is MANAGED_LIABILITY.
    (rollupLiabilityFactor * rollupLimit)
    is the minimum liabilty the user is deemed to
    be comfortable with. After the rollupLiabilityThreshold
     price subsequent volumes will be rolled up
      to minimum value such that the
      liability >= the minimum liability.service
      level default (5). Not supported as yet.
    '''

    best_prices_depth: int = None
    rollup_model: str = None
    rollup_limit: int = None
    rollup_liability_threshold: float = None
    rollup_liability_factor: int = None

    @property
    def ex_best_offers_overrides_data(self):
        return {
            'bestPricesDepth': self.best_prices_depth,
            'rollupModel': self.rollup_model,
            'rollupLimit': self.rollup_limit,
            'rollupLiabilityThreshold': self.rollup_liability_threshold,
            'rollupLiabilityFactor': self.rollup_liability_factor,
        }
