from psycopg2.extras import NumericRange, DateRange


class InclusiveNumericRange(NumericRange):

    def __init__(self, lower=None, upper=None, bounds='[]', empty=False):
        super().__init__(lower, upper, bounds, empty)


class InclusiveDateRange(DateRange):

    def __init__(self, lower=None, upper=None, bounds='[]', empty=False):
        super().__init__(lower, upper, bounds, empty)