
class NotValidDomain(Exception):
    def __init___(self,dErrorArguments):
        Exception.__init__(self,"Not valid domain.".format(dErrArguments))
        self.dErrorArguments = dErrorArguements