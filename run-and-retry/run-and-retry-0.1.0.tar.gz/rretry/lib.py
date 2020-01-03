
class AttemptResults(list):
    def __init__(self, tries):
        return super(AttemptResults, self).extend(['ND'] * tries)
