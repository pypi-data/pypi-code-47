from sqlalchemy.orm import Session
from sqlalchemy import and_
from pavis.snowflake import pavisSnowflake
from pavis.objects import Corpora as CorporaO
from pavis.objects import OriginalSentenceSet as OriginalSentenceSetO
from pavis.objects import CorporaSet as CorporaSetO
from pavis.objects import BranchSet as BranchSetO
from pavis.objects import VersionSet as VersionSetO
from pavis.objects import Diff as DiffO
from pavis.objects import LatestCache as LatestCacheO
from pavis.objects import SnapshotCache as SnapshotCacheO
from pavis.objects import History as HistoryO
from pavis.datastructs import SentenceSet
import copy


class pavisCurds:
    def __init__(self):
        self._Snowflake = pavisSnowflake(1, 1)

    def getNewID(self):
        return self._Snowflake.next()

    def newCorpora(
            self,
            session: Session,
            SentenceID: int,
            ParagraphID: int,
            Corpora: str,
            ExtraData: str):
        newCorpora = CorporaO()
        newCorporaID = self._Snowflake.next()
        newCorpora.CorporaID = newCorporaID
        newCorpora.SentenceID = SentenceID
        newCorpora.ParagraphID = ParagraphID
        newCorpora.Corpora = Corpora
        newCorpora.ExtraData = ExtraData
        session.add(newCorpora)
        return newCorporaID

    def newOriginalSentenceSet(
            self,
            session: Session,
            newOriginalSentenceSetID: int,
            CorporaID: int):
        newOriginalSentenceSet = OriginalSentenceSetO()
        newOriginalSentenceSet.OriginalSentenceSetID = newOriginalSentenceSetID
        newOriginalSentenceSet.CorporaID = CorporaID
        session.add(newOriginalSentenceSet)

    def newCorporaSet(
            self,
            session: Session,
            CorporaSetName: str,
            OriginalSentenceSetID: int,
            ExtraData: str):
        newCorporaSet = CorporaSetO()
        newCorporaSetID = self._Snowflake.next()
        newCorporaSet.CorporaSetID = newCorporaSetID
        newCorporaSet.CorporaSetName = CorporaSetName
        newCorporaSet.OriginalSentenceSetID = OriginalSentenceSetID
        newCorporaSet.ExtraData = ExtraData
        session.add(newCorporaSet)
        return newCorporaSetID

    def newCorporaSetByCorporaSet(
            self,
            session: Session,
            CorporaSetName: str,
            CorporaSet: CorporaSetO):
        oriosss = session.query(OriginalSentenceSetO) \
            .filter(OriginalSentenceSetO.OriginalSentenceSetID == CorporaSet.OriginalSentenceSetID) \
            .order_by(OriginalSentenceSetO.Sequence) \
            .all()
        nossid = self._Snowflake.next()
        for os in oriosss:
            c = session.query(CorporaO) \
                .filter(CorporaO.CorporaID == os.CorporaID) \
                .first()
            ncid = self.newCorpora(session,
                                   c.SentenceID,
                                   c.ParagraphID,
                                   c.Corpora,
                                   c.ExtraData)
            self.newOriginalSentenceSet(session, nossid, ncid)
        ncsid = self.newCorporaSet(
            session, CorporaSetName, nossid, CorporaSet.ExtraData)
        diffS = 0
        oribs = session.query(BranchSetO) \
            .filter(BranchSetO.CorporaSetID == CorporaSet.CorporaSetID) \
            .all()
        for b in oribs:
            nbid = self.newBranchSet(
                session,
                b.BranchName,
                b.IsMainBranch,
                ncsid,
                b.ExtraData)
            orivs = session.query(VersionSetO) \
                .filter(VersionSetO.BranchID == b.BranchID) \
                .order_by(VersionSetO.Sequence) \
                .all()
            for v in orivs:
                nvid = self.newVersionSet(
                    session,
                    nbid,
                    v.ExtraData)
                oridiffs = session.query(DiffO) \
                    .filter(DiffO.VersionID == v.VersionID) \
                    .order_by(DiffO.Sequence) \
                    .all()
                orissc = session.query(SnapshotCacheO) \
                    .filter(and_(
                        SnapshotCacheO.BranchID == b.BranchID,
                        SnapshotCacheO.VersionID == v.VersionID)) \
                    .all()
                orilcs = session.query(LatestCacheO).all()
                for d in oridiffs:
                    c = session.query(CorporaO) \
                        .filter(CorporaO.CorporaID == d.CorporaID) \
                        .first()
                    ncid = self.newCorpora(
                        session,
                        c.SentenceID,
                        c.ParagraphID,
                        c.Corpora,
                        c.ExtraData)
                    self.newDiff(session, nvid, ncid)
                    for lc in orilcs:
                        if lc.CorporaID == c.CorporaID:
                            self.newLatestCache(
                                session,
                                nbid, ncid, nvid)
                            break
                    session.commit()
                    for ssc in orissc:
                        if ssc.CorporaID == c.CorporaID:
                            self.newSnapshotCache(
                                session,
                                nbid, nvid,
                                self.getDiffSequence(session, nbid),
                                ncid)
                            break
                    orihis = session.query(HistoryO) \
                        .filter(and_(
                            HistoryO.BranchID == b.BranchID,
                            HistoryO.VersionID == v.VersionID))\
                        .order_by(HistoryO.Sequence) \
                        .all()
                    for h in orihis:
                        self.newHistory(
                            session,
                            nbid,
                            h.SentenceID,
                            h.ParagraphID,
                            nvid)
        return ncsid

    def newBranchSet(
            self,
            session: Session,
            BranchName: str,
            IsMainBranch: bool,
            CorporaSetID: int,
            ExtraData: str):
        newBranchSet = BranchSetO()
        newBranchSetID = self._Snowflake.next()
        newBranchSet.BranchID = newBranchSetID
        newBranchSet.BranchName = BranchName
        newBranchSet.IsMainBranch = IsMainBranch
        newBranchSet.CorporaSetID = CorporaSetID
        newBranchSet.ExtraData = ExtraData
        session.add(newBranchSet)
        return newBranchSetID

    def newVersionSet(
            self,
            session: Session,
            BranchID: int,
            ExtraData: str):
        newVersionSet = VersionSetO()
        newVersionSetID = self._Snowflake.next()
        newVersionSet.VersionID = newVersionSetID
        newVersionSet.BranchID = BranchID
        newVersionSet.ExtraData = ExtraData
        session.add(newVersionSet)
        return newVersionSetID

    def newDiff(
            self,
            session: Session,
            VersionID: int,
            CorporaID: int):
        newDiff = DiffO()
        newDiff.VersionID = VersionID
        newDiff.CorporaID = CorporaID
        session.add(newDiff)

    def newEmptyCorporasByCorporas(
            self,
            session: Session,
            Corporas: list):
        cids = []
        for corpora in Corporas:
            newCorpora = CorporaO()
            newCorporaID = self._Snowflake.next()
            newCorpora.CorporaID = newCorporaID
            newCorpora.SentenceID = corpora.SentenceID
            newCorpora.ParagraphID = corpora.ParagraphID
            newCorpora.Corpora = ''
            newCorpora.ExtraData = ''
            session.add(newCorpora)
            cids.append(newCorporaID)
        return cids

    def newVersionSet(
            self,
            session: Session,
            BranchID: int,
            ExtraData: str):
        newVersionSet = VersionSetO()
        newVersionSetID = self._Snowflake.next()
        newVersionSet.VersionID = newVersionSetID
        newVersionSet.BranchID = BranchID
        newVersionSet.ExtraData = ExtraData
        session.add(newVersionSet)
        return newVersionSetID

    def newLatestCache(
            self,
            session: Session,
            BranchID: int,
            CorporaID: int,
            VersionID: int):
        newLatestCache = LatestCacheO()
        newLatestCache.BranchID = BranchID
        newLatestCache.CorporaID = CorporaID
        newLatestCache.VersionID = VersionID
        session.add(newLatestCache)

    def newSnapshotCache(
            self,
            session: Session,
            BranchID: int,
            VersionID: int,
            DiffSequence: int,
            CorporaID: int):
        newSnapshotCache = SnapshotCacheO()
        newSnapshotCache.BranchID = BranchID
        newSnapshotCache.VersionID = VersionID
        newSnapshotCache.DiffSequence = DiffSequence
        newSnapshotCache.CorporaID = CorporaID
        session.add(newSnapshotCache)

    def newHistory(
            self,
            session: Session,
            BranchID: int,
            SentenceID: int,
            ParagraphID: int,
            VersionID: int):
        newHistory = HistoryO()
        newHistory.BranchID = BranchID
        newHistory.SentenceID = SentenceID
        newHistory.ParagraphID = ParagraphID
        newHistory.VersionID = VersionID
        session.add(newHistory)

    def newHistoriesByCorporas(
            self,
            session: Session,
            BranchID: int,
            VersionID: int,
            Corporas: list):
        for corpora in Corporas:
            self.newHistory(
                session,
                BranchID,
                corpora.SentenceID,
                corpora.ParagraphID,
                VersionID)

    def getSentenceSetAndExtraDataByVersionID(
            self,
            session: Session,
            BranchID: int,
            VersionID: int):
        Corporas = self.getCorporasByDiffs(session,
                                           self.getDiffsByVersionID(session, VersionID))
        Changes = SentenceSet()
        for corpora in Corporas:
            Changes.add(
                corpora.SentenceID,
                corpora.ParagraphID,
                corpora.Corpora,
                corpora.ExtraData)
        ExtraData = session.query(VersionSetO) \
            .filter(VersionSetO.VersionID == VersionID) \
            .first().ExtraData
        return Changes, ExtraData

    def getDiffSequence(
            self,
            session: Session,
            BranchID: int):
        vid = session.query(VersionSetO) \
            .filter(VersionSetO.BranchID == BranchID) \
            .order_by(VersionSetO.Sequence.desc()) \
            .first().VersionID
        return session.query(DiffO) \
            .filter(DiffO.VersionID == vid) \
            .order_by(DiffO.Sequence.desc()) \
            .first().Sequence

    def getDiffsByVersionID(
            self,
            session: Session,
            VersionID: int):
        return session.query(DiffO) \
            .filter(DiffO.VersionID == VersionID) \
            .all()

    def getSnapshotCacheSequence(
            self,
            session: Session,
            BranchID: int):
        return session.query(SnapshotCacheO) \
            .filter(SnapshotCacheO.BranchID == BranchID) \
            .order_by(SnapshotCacheO.DiffSequence.desc()) \
            .first().DiffSequence

    def getCorporaSetByID(
            self,
            session: Session,
            CorporaSetID: int):
        if CorporaSetID == 0:
            return session.query(CorporaSetO).all()
        return session.query(CorporaSetO) \
            .filter(CorporaSetO.CorporaSetID == CorporaSetID) \
            .first()

    def getCorporasByIDs(
            self,
            session: Session,
            CorporaIDs: list):
        CorporaIDs.sort(reverse=True)
        corporas = []
        for id in CorporaIDs:
            corporas.append(
                session.query(CorporaO)
                    .filter(CorporaO.CorporaID == id)
                    .first())
        return corporas

    def getOriginalSentenceSetsByCorporaSet(
            self,
            session: Session,
            CorporaSet: CorporaSetO):
        return session.query(OriginalSentenceSetO) \
            .filter(OriginalSentenceSetO.OriginalSentenceSetID == CorporaSet.OriginalSentenceSetID) \
            .all()

    def getCorporasByOriginalSentenceSet(
            self,
            session: Session,
            OriginalSentenceSet: list):
        CorporaSet = []
        for oss in OriginalSentenceSet:
            CorporaSet.append(
                session.query(CorporaO)
                .filter(CorporaO.CorporaID == oss.CorporaID)
                .first())
        return CorporaSet

    def getBranchesByCorporaSet(
            self,
            session: Session,
            CorporaSet: CorporaSetO):
        return session.query(BranchSetO) \
            .filter(BranchSetO.CorporaSetID == CorporaSet.CorporaSetID)\
            .all()

    def getBranchByID(
            self,
            session: Session,
            BranchID: int):
        if BranchID == 0:
            return session.query(BranchSetO).all()
        return session.query(BranchSetO) \
            .filter(BranchSetO.BranchID == BranchID) \
            .first()

    def getVersionsByBranches(
            self,
            session: Session,
            Branches: list):
        Versions = []
        for b in Branches:
            for v in session.query(VersionSetO) \
                .filter(VersionSetO.BranchID == b.BranchID) \
                    .order_by(VersionSetO.Sequence.desc()) \
                    .all():
                Versions.append(v)
        return Versions

    def getDiffsByVersions(
            self,
            session: Session,
            Versions: list):
        Diffs = []
        for v in Versions:
            for d in session.query(DiffO) \
                    .filter(DiffO.VersionID == v.VersionID) \
                    .all():
                Diffs.append(d)
        return Diffs

    def getCorporasByDiffs(
            self,
            session: Session,
            Diffs: list):
        Corporas = []
        for d in Diffs:
            for c in session.query(CorporaO) \
                            .filter(CorporaO.CorporaID == d.CorporaID) \
                            .all():
                Corporas.append(c)
        return Corporas

    def getBranchesIDs(
            self,
            Branches: list):
        ids = []
        for b in Branches:
            ids.append(b.BranchID)
        return ids

    def getBranchByVersionID(
            self,
            session: Session,
            VersionID: int):
        v = session.query(VersionSetO) \
            .filter(VersionSetO.VersionID == VersionID) \
            .first()
        return session.query(BranchSetO) \
            .filter(BranchSetO.BranchID == v.BranchID) \
            .first()

    def getSentenceSetOfLatestVersionByBranchID(
            self,
            session: Session,
            BranchID: int):
        ss = SentenceSet()
        cs = []
        lcs = session.query(LatestCacheO) \
            .filter(LatestCacheO.BranchID == BranchID) \
            .all()
        for lc in lcs:
            cs.append(session.query(CorporaO)
                      .filter(CorporaO.CorporaID == lc.CorporaID)
                      .first())
        for c in cs:
            ss.add(c.SentenceID, c.ParagraphID, c.Corpora, c.ExtraData)
        return ss

    def getSentenceSetOfOriginalSentenceSetByBranchID(
            self,
            session: Session,
            BranchID: int):
        ss = SentenceSet()
        cs = session.query(CorporaSetO) \
            .filter(CorporaSetO.CorporaSetID == session.query(BranchSetO)
                    .filter(BranchSetO.BranchID == BranchID)
                    .first().CorporaSetID) \
            .first()
        corporas = self.getCorporasByOriginalSentenceSet(
            session,
            self.getOriginalSentenceSetsByCorporaSet(session, cs))
        for c in corporas:
            ss.add(c.SentenceID, c.ParagraphID, c.Corpora, c.ExtraData)
        return ss

    def getSentenceSetHistoriesAndVersionIDsByBranchIDAndSentenceID(
            self,
            session: Session,
            BranchID: int,
            SentenceID: int):
        HistoryCorporas = []
        HistoryVersionIDs = []
        histories = session.query(HistoryO) \
            .filter(HistoryO.BranchID == BranchID, HistoryO.SentenceID == SentenceID) \
            .order_by(HistoryO.Sequence) \
            .all()
        for history in histories:
            HistoryVersionIDs.append(history.VersionID)
            for diff in session.query(DiffO) \
                .filter(DiffO.VersionID == history.VersionID) \
                    .all():
                c = session.query(CorporaO) \
                    .filter(CorporaO.CorporaID == diff.CorporaID) \
                    .first()
                if c.SentenceID == SentenceID:
                    HistoryCorporas.append(c)
                    break
        ss = SentenceSet()
        for hc in HistoryCorporas:
            ss.add(hc.SentenceID, hc.ParagraphID, hc.Corpora, hc.ExtraData)
        return ss, HistoryVersionIDs

    def getParagraphHistoriesAndVersionIDsByBranchIDAndParagraphID(
            self,
            session: Session,
            BranchID: int,
            ParagraphID: int):
        HistoryVersionIDs = []
        HistoryParagraphs = []
        histories = session.query(HistoryO) \
            .filter(and_(HistoryO.BranchID == BranchID, HistoryO.ParagraphID == ParagraphID)) \
            .order_by(HistoryO.Sequence) \
            .all()
        for history in histories:
            if history.VersionID in HistoryVersionIDs:
                continue
            else:
                ss = SentenceSet()
                for diff in session.query(DiffO) \
                        .filter(DiffO.VersionID == history.VersionID) \
                        .all():
                    c = session.query(CorporaO) \
                        .filter(and_(
                            CorporaO.CorporaID == diff.CorporaID,
                            CorporaO.ParagraphID == ParagraphID)) \
                        .first()
                    if c is not None:
                        ss.add(c.SentenceID, c.ParagraphID,
                               c.Corpora, c.ExtraData)
                HistoryParagraphs.append(ss)
                HistoryVersionIDs.append(history.VersionID)
        return HistoryParagraphs, HistoryVersionIDs

    def getBranchHistoriesByBranchID(
            self,
            session: Session,
            BranchID: int):
        versions = session.query(VersionSetO) \
            .filter(VersionSetO.BranchID == BranchID) \
            .order_by(VersionSetO.Sequence) \
            .all()
        snapshots = session.query(SnapshotCacheO) \
            .filter(SnapshotCacheO.BranchID == BranchID) \
            .order_by(SnapshotCacheO.DiffSequence) \
            .all()
        latest = session.query(LatestCacheO) \
            .filter(LatestCacheO.BranchID == BranchID) \
            .all()
        BranchVersions = []
        VersionIDs = []
        for v in versions:
            VersionIDs.append(v.VersionID)
            if v.VersionID == versions[-1].VersionID:
                ss = SentenceSet()
                for l in latest:
                    corpora = session.query(CorporaO) \
                        .filter(CorporaO.CorporaID == l.CorporaID) \
                        .first()
                    ss.add(
                        corpora.SentenceID,
                        corpora.ParagraphID,
                        corpora.Corpora,
                        corpora.ExtraData)
                BranchVersions.append(ss)
                break
            snaped = False
            ss = SentenceSet()
            for s in snapshots:
                if v.VersionID == s.VersionID:
                    corpora = session.query(CorporaO) \
                        .filter(CorporaO.CorporaID == s.CorporaID) \
                        .first()
                    ss.add(
                        corpora.SentenceID,
                        corpora.ParagraphID,
                        corpora.Corpora,
                        corpora.ExtraData)
                    snaped = True
            if snaped:
                BranchVersions.append(ss)
            else:
                d = session.query(DiffO) \
                    .filter(DiffO.VersionID == v.VersionID) \
                    .all()
                cs = self.getCorporasByDiffs(session, d)
                Version = copy.deepcopy(BranchVersions[-1])
                for c in cs:
                    for index in range(Version.getLength()):
                        if Version.get(index)['sid'] == c.SentenceID:
                            Version.get(index)['content'] = c.Corpora
                            Version.get(index)['extra'] = c.ExtraData
                BranchVersions.append(Version)
        return BranchVersions, VersionIDs

    def getMainBranchID(
            self,
            session: Session,
            CorporaSetID: int):
        bs = self.getBranchesByCorporaSet(session,
                                          self.getCorporaSetByID(session, CorporaSetID))
        for b in bs:
            if b.IsMainBranch:
                return b.BranchID

    def getCorporaSetByBranch(
            self,
            session: Session,
            Branch: BranchSetO):
        return session.query(CorporaSetO) \
            .filter(CorporaSetO.CorporaSetID == Branch.CorporaSetID) \
            .first()

    def delCorporas(
            self,
            session: Session,
            Corpora: list):
        for corpora in Corpora:
            session.delete(corpora)

    def delOriginalSentenceSets(
            self,
            session: Session,
            OriginalSentenceSet: list):
        for originalsentenceset in OriginalSentenceSet:
            session.delete(originalsentenceset)

    def delCorporaSet(
            self,
            session: Session,
            CorporaSet: CorporaSetO):
        session.delete(CorporaSet)

    def delBranches(
            self,
            session: Session,
            Branches: list):
        for branch in Branches:
            session.delete(branch)

    def delVersions(
            self,
            session: Session,
            Versions: list):
        for version in Versions:
            session.delete(version)

    def delDiffs(
            self,
            session: Session,
            Diffs: list):
        for diff in Diffs:
            session.delete(diff)

    def delLatestCache(
            self,
            session: Session,
            BranchID: int):
        LatestCaches = session.query(LatestCacheO) \
            .filter(LatestCacheO.BranchID == BranchID) \
            .all()
        for lc in LatestCaches:
            session.delete(lc)

    def delSnapshotCache(
            self,
            session: Session,
            BranchID: int):
        SnapshotCaches = session.query(SnapshotCacheO) \
            .filter(SnapshotCacheO.BranchID == BranchID) \
            .all()
        for ssc in SnapshotCaches:
            session.delete(ssc)

    def delHistories(
            self,
            session: Session,
            BranchID: int):
        Histories = session.query(HistoryO) \
            .filter(HistoryO.BranchID == BranchID) \
            .all()
        for h in Histories:
            session.delete(h)

    def isMainBranch(
            self,
            session: Session,
            BranchID: int):
        return session.query(BranchSetO) \
            .filter(BranchSetO.BranchID == BranchID) \
            .first().IsMainBranch

    def updateLatestCacheByCorporas(
            self,
            session: Session,
            BranchID: int,
            Corporas: list):
        LatestCaches = session.query(LatestCacheO) \
            .filter(LatestCacheO.BranchID == BranchID) \
            .order_by(LatestCacheO.CorporaID.desc()) \
            .all()
        corporas = session.query(CorporaO) \
            .order_by(CorporaO.CorporaID.desc()) \
            .filter(CorporaO.CorporaID >= LatestCaches[-1].CorporaID) \
            .all()
        pointer = 0
        map = {}
        for corpora in corporas:
            if corpora.CorporaID == LatestCaches[pointer].CorporaID:
                map[corpora.SentenceID] = pointer
                pointer += 1
            if pointer == len(LatestCaches):
                break
        for c in Corporas:
            LatestCaches[map[c.SentenceID]].CorporaID = c.CorporaID

    def updateSnapshotCacheIfNeeded(
            self,
            session: Session,
            BranchID: int,
            VersionID: int,
            Delta: int):
        ds = self.getDiffSequence(session, BranchID)
        if ds - self.getSnapshotCacheSequence(session, BranchID) > Delta:
            for latestcache in session.query(LatestCacheO) \
                .filter(LatestCacheO.BranchID == BranchID) \
                    .all():
                corpora = session.query(CorporaO) \
                    .filter(CorporaO.CorporaID == latestcache.CorporaID) \
                    .first()
                ncid = self.newCorpora(session,
                                       corpora.SentenceID,
                                       corpora.ParagraphID,
                                       corpora.Corpora,
                                       corpora.ExtraData)
                self.newSnapshotCache(session,
                                      BranchID,
                                      VersionID,
                                      ds,
                                      ncid)

    def setCorporaSetMainBranch(
            self,
            session: Session,
            CorporaSetID: int,
            BranchID: int):
        bs = self.getBranchesByCorporaSet(session,
                                          self.getCorporaSetByID(session, CorporaSetID))
        task = 0
        for b in bs:
            if b.IsMainBranch:
                b.IsMainBranch = False
                task += 1
            if b.BranchID == BranchID:
                b.IsMainBranch = True
                task += 1
            if task == 2:
                break

    def compareOriginalSentenceSets(
            self,
            session: Session,
            SetsA: list,
            SetsB: list):
        cas = self.getCorporasByOriginalSentenceSet(session, SetsA)
        cbs = self.getCorporasByOriginalSentenceSet(session, SetsB)
        for ca in cas:
            found = False
            for cb in cbs:
                if cb.SentenceID == ca.SentenceID:
                    found = True
                    break
            if not found:
                return False
        return True

    def isVersionInBranch(
            self,
            session: Session,
            VersionID: int,
            BranchID: int):
        vs = session.query(VersionSetO) \
            .filter(VersionSetO.BranchID == BranchID) \
            .all()
        for v in vs:
            if v.VersionID == VersionID:
                return True
        return False

    def rollbackBranchToVersion(
            self,
            session: Session,
            BranchID: int,
            VersionID: int):
        Versions = session.query(VersionSetO) \
            .filter(VersionSetO.BranchID == BranchID) \
            .order_by(VersionSetO.Sequence) \
            .all()
        VersionsSentenceSet, VersionIDs = self.getBranchHistoriesByBranchID(
            session, BranchID)
        OutVersions = []
        tvs = 0
        for i in range(len(Versions)):
            if Versions[i].VersionID == VersionID:
                tvs = Versions[i].Sequence
                for index in range(i, len(Versions)):
                    if Versions[index].Sequence > Versions[i].Sequence:
                        OutVersions.append(Versions[index])
                break
        lcs = session.query(LatestCacheO) \
            .filter(LatestCacheO.BranchID == BranchID) \
            .all()
        lccs = []
        for lc in lcs:
            lccs.append(
                session.query(CorporaO)
                .filter(CorporaO.CorporaID == lc.CorporaID)
                .first())
        for v in Versions:
            if v.Sequence > tvs:
                break
            else:
                cs = self.getCorporasByDiffs(
                    session,
                    self.getDiffsByVersions(
                        session,
                        [v, ]))
                for c in cs:
                    for i in range(len(lcs)):
                        if c.SentenceID == lccs[i].SentenceID \
                                and c.ParagraphID == lccs[i].ParagraphID:
                            lcs[i].CorporaID = c.CorporaID
        for ov in OutVersions:
            for df in session.query(DiffO) \
                .filter(DiffO.VersionID == ov.VersionID) \
                    .all():
                session.delete(session.query(CorporaO)
                               .filter(CorporaO.CorporaID == df.CorporaID)
                               .first())
                session.delete(df)
            for hi in session.query(HistoryO) \
                .filter(HistoryO.VersionID == ov.VersionID) \
                    .all():
                session.delete(hi)
            for sn in session.query(SnapshotCacheO) \
                .filter(and_(
                    SnapshotCacheO.BranchID == BranchID,
                    SnapshotCacheO.VersionID == ov.VersionID)) \
                    .all():
                session.delete(sn)
            session.delete(ov)
