from jdog.placeholder.placeholder import Placeholder


class RangePlaceholder(Placeholder):
    def __init__(self, full_name, args):
        super().__init__(full_name, args)
        self.prop = args[0]
        self.low = args[1]
        if len(args) > 2:
            self.high = args[2]

    def exec(self):
        pass

