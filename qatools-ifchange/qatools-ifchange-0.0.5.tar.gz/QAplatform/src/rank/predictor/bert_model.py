#
from src.rank.rank_base import RankBase
import numpy as np

class BertRank(RankBase):
    def predict(self, scores, ids):
        scores = np.array(scores)
        max_id = np.argmax(scores)
        return ids[max_id], scores[max_id]
