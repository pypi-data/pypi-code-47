class SentenceSet:
    def __init__(self):
        self._sentences = []

    def add(self, sentenceID, paragraphID: int, content: str, extra: str = ''):
        self._sentences.append({
            'sid': sentenceID,
            'pid': paragraphID,
            'content': content,
            'extra': extra
        })
        return len(self._sentences)-1

    def rm(self, index: int):
        if index not in range(len(self._sentences)):
            raise Exception
        self._sentences.remove(index)

    def get(self, index: int):
        if index not in range(len(self._sentences)):
            raise Exception
        return self._sentences[index]

    def getLength(self):
        return len(self._sentences)

    def clear(self):
        self._sentences.clear()

    def __repr__(self):
        rstr = ''
        for sentence in self._sentences:
            rstr += "<Sentence(sid:{}, pid:{}, content:{}, extra:{})>".format(
                sentence['sid'],
                sentence['pid'],
                sentence['content'],
                sentence['extra']
            )
            rstr += '\n'
        return rstr


class ParallelSentenceSet:
    def __init__(self,
                 SetA: SentenceSet,
                 SetB: SentenceSet):
        self.SetA = SetA
        self.SetB = SetB

    def __repr__(self):
        rstr = ''
        rstr += "<ParallelSentenceSet(\nSetA:\n"
        rstr += self.SetA.__repr__()
        rstr += "SetB:\n"
        rstr += self.SetB.__repr__()
        rstr += ")>\n"
        return rstr


class SentenceHistorySet:
    def __init__(self,
                 SentenceHistories: SentenceSet,
                 VersionIDs: list):
        self.SentenceHistories = SentenceHistories
        self.VersionIDs = VersionIDs

    def __repr__(self):
        rstr = ''
        i = 0
        rstr += '<SentenceHistorySet(\n'
        for s in self.SentenceHistories.__repr__().split('\n'):
            if s.strip() == '':
                break
            rstr += 'VersionID:'
            rstr += str(self.VersionIDs[i])
            rstr += ' '
            rstr += s
            rstr += '\n'
            i += 1
        rstr += ')>\n'
        return rstr


class ParagraphHistorySet:
    def __init__(self,
                 ParagraphHistories: list,
                 VersionIDs: list):
        self.ParagraphHistories = ParagraphHistories
        self.VersionIDs = VersionIDs

    def __repr__(self):
        rstr = ''
        rstr += '<ParagraphHistorySet(\n\n'
        i = 0
        for ph in self.ParagraphHistories:
            rstr += 'VersionID:' + str(self.VersionIDs[i]) + '\n'
            rstr += ph.__repr__()
            rstr += '\n'
            i += 1
        rstr += ')>\n'
        return rstr


class BranchHistorySet:
    def __init__(self,
                 BranchHistories: list,
                 VersionIDs: list):
        self.BranchHistories = BranchHistories
        self.VersionIDs = VersionIDs

    def __repr__(self):
        rstr = ''
        rstr += '<BranchHistorySet(\n'
        for index in range(len(self.VersionIDs)):
            rstr += 'VersionID:' + str(self.VersionIDs[index]) + '\n'
            rstr += self.BranchHistories[index].__repr__()
            rstr += '\n'
        rstr += ')>\n'
        return rstr
