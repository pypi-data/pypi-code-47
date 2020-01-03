from sqlalchemy import Numeric


class Monetary(Numeric):
    def __init__(self):
        super().__init__(precision=10, scale=2)
