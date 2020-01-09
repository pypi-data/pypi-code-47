import random
from jdog.placeholder.placeholder import Placeholder


class OptionPlaceholder(Placeholder):
    """
        Option placeholder picks randomly one of arguments.
        Each argument can be nested placeholder.
    """
    def __init__(self, full_name, args):
        super().__init__(full_name, args)

    def exec(self):
        """
            Choose randomly one of arguments. If chosen argument is placeholder executes it
            and return otherwise return argument enclosed as string
        """
        pick = random.choice(self.arguments)
        try:
            return pick.exec()
        except AttributeError:
            return f'"{pick}"'
