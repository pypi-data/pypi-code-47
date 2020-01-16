#
class RankBase(object):
    def predict(self, scores, ids):
        raise NotImplementedError("Rank plugin must have predict function")
