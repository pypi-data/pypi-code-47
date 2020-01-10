from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 仅仅为了读写定义，省略了主键、外键、自增等


class Corpora(Base):
    __tablename__ = 'CorporaT'
    CorporaID = Column(Integer, primary_key=True)
    SentenceID = Column(Integer)
    ParagraphID = Column(Integer)
    Corpora = Column(String)
    ExtraData = Column(String)

    def __repr__(self):
        return "<Corpora(CID:{}, SID:{}, PID:{}, C:{}, ED:{})>".format(
            self.CorporaID,
            self.SentenceID,
            self.ParagraphID,
            self.Corpora,
            self.ExtraData
        )


class OriginalSentenceSet(Base):
    __tablename__ = 'OriginalSentenceSetT'
    OriginalSentenceSetID = Column(Integer)
    CorporaID = Column(Integer)
    Sequence = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<OriginalSentenceSet(OSID:{}, CID:{}, S:{})>".format(
            self.OriginalSentenceSetID,
            self.CorporaID,
            self.Sequence
        )


class CorporaSet(Base):
    __tablename__ = 'CorporaSetT'
    CorporaSetID = Column(Integer, primary_key=True)
    CorporaSetName = Column(String)
    OriginalSentenceSetID = Column(Integer)
    ExtraData = Column(String)

    def __repr__(self):
        return "<CorporaSet(CSID:{}, CSN:{}, OSID:{}, ED:{})>".format(
            self.CorporaSetID,
            self.CorporaSetName,
            self.OriginalSentenceSetID,
            self.ExtraData
        )


class BranchSet(Base):
    __tablename__ = 'BranchSetT'
    BranchID = Column(Integer, primary_key=True)
    BranchName = Column(String)
    IsMainBranch = Column(Boolean)
    CorporaSetID = Column(Integer)
    ExtraData = Column(String)

    def __repr__(self):
        return "<BranchSet(BID:{}, BN:{}, IMB:{}, CSID:{}, ED:{})>".format(
            self.BranchID,
            self.BranchName,
            self.IsMainBranch,
            self.CorporaSetID,
            self.ExtraData
        )


class VersionSet(Base):
    __tablename__ = 'VersionSetT'
    VersionID = Column(Integer, primary_key=True)
    BranchID = Column(Integer)
    Sequence = Column(Integer)
    ExtraData = Column(String)

    def __repr__(self):
        return "<VersionSet(VID:{}, BID:{}, S:{}, ED:{})>".format(
            self.VersionID,
            self.BranchID,
            self.Sequence,
            self.ExtraData
        )


class Diff(Base):
    __tablename__ = 'DiffT'
    VersionID = Column(Integer)
    CorporaID = Column(Integer)
    Sequence = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Diff(VID:{}, CID{}, S:{})>".format(
            self.VersionID,
            self.CorporaID,
            self.Sequence
        )


class LatestCache(Base):
    __tablename__ = 'LatestCacheT'
    BranchID = Column(Integer)
    CorporaID = Column(Integer, primary_key=True)
    VersionID = Column(Integer)

    def __repr__(self):
        return "<LatestCache(BID:{}, CID:{}, VID:{})>".format(
            self.BranchID,
            self.CorporaID,
            self.VersionID
        )


class SnapshotCache(Base):
    __tablename__ = 'SnapshotCacheT'
    BranchID = Column(Integer)
    VersionID = Column(Integer)
    DiffSequence = Column(Integer)
    CorporaID = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<SnapshotCache(BID:{}, VID:{}, DS:{}, CID:{})>".format(
            self.BranchID,
            self.VersionID,
            self.DiffSequence,
            self.CorporaID
        )


class History(Base):
    __tablename__ = "HistoryT"
    BranchID = Column(Integer)
    SentenceID = Column(Integer)
    ParagraphID = Column(Integer)
    VersionID = Column(Integer)
    Sequence = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<History(BID:{}, SID:{}. PID:{}, VID:{}, S:{})>".format(
            self.BranchID,
            self.SentenceID,
            self.ParagraphID,
            self.VersionID,
            self.Sequence
        )
