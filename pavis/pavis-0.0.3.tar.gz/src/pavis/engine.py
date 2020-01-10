import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from pavis.datastructs import SentenceSet
from pavis.datastructs import ParallelSentenceSet
from pavis.datastructs import SentenceHistorySet
from pavis.datastructs import ParagraphHistorySet
from pavis.datastructs import BranchHistorySet
from pavis.curds import pavisCurds
from pavis.Profiler import func_time


def Hello():
    return 'Hello Pavis'


class pavisEngine:
    def __init__(self, dblink: str):
        self._SnapshotDelta = 50
        try:
            self._SQLEngine = create_engine(dblink)
            self._SQLSessionFactory = sessionmaker(bind=self._SQLEngine)
            self._SQLScopedSession = scoped_session(self._SQLSessionFactory)
        except Exception as e:
            raise e
        self._Curds = pavisCurds()

    def shutdown(self):
        self._SQLScopedSession.remove()

    def newCorporaSet(
            self,
            CorporaSetName: str,
            OriginalSentenceSet: SentenceSet,
            ExtraData: str = ''):
        ses = self._SQLScopedSession()
        try:
            CorporaIDs = []
            for i in range(OriginalSentenceSet.getLength()):
                newCorporaID = self._Curds.newCorpora(ses,
                                                      OriginalSentenceSet.get(
                                                          i)['sid'],
                                                      OriginalSentenceSet.get(
                                                          i)['pid'],
                                                      OriginalSentenceSet.get(
                                                          i)['content'],
                                                      OriginalSentenceSet.get(i)['extra'])
                CorporaIDs.append(newCorporaID)
            ses.commit()
            newOriginalSentenceSetID = self._Curds.getNewID()
            for id in CorporaIDs:
                self._Curds.newOriginalSentenceSet(
                    ses, newOriginalSentenceSetID, id)
            ses.commit()
            initialCorporaIDs = []
            for i in range(OriginalSentenceSet.getLength()):
                newInitialCorporaID = self._Curds.newCorpora(ses,
                                                             OriginalSentenceSet.get(
                                                                 i)['sid'],
                                                             OriginalSentenceSet.get(
                                                                 i)['pid'],
                                                             '', OriginalSentenceSet.get(i)['extra'])
                initialCorporaIDs.append(newInitialCorporaID)
            ses.commit()
            newCorporaSetID = self._Curds.newCorporaSet(
                ses, CorporaSetName, newOriginalSentenceSetID, ExtraData)
            ses.commit()
            self.newBranch(newCorporaSetID, 'default', True, '')
        except Exception as e:
            ses.rollback()
            raise e
        finally:
            ses.close()
        return newCorporaSetID

    def delCorporaSet(
            self,
            CorporaSetID: int):
        ses = self._SQLScopedSession()
        try:
            cs = self._Curds.getCorporaSetByID(ses, CorporaSetID)
            oss = self._Curds.getOriginalSentenceSetsByCorporaSet(ses, cs)
            c = self._Curds.getCorporasByOriginalSentenceSet(ses, oss)
            b = self._Curds.getBranchesByCorporaSet(ses, cs)
            v = self._Curds.getVersionsByBranches(ses, b)
            d = self._Curds.getDiffsByVersions(ses, v)
            cd = self._Curds.getCorporasByDiffs(ses, d)
            self._Curds.delCorporaSet(ses, cs)
            ses.commit()
            self._Curds.delOriginalSentenceSets(ses, oss)
            ses.commit()
            self._Curds.delCorporas(ses, c)
            self._Curds.delCorporas(ses, cd)
            ses.commit()
            self._Curds.delBranches(ses, b)
            ses.commit()
            self._Curds.delVersions(ses, v)
            ses.commit()
            self._Curds.delDiffs(ses, d)
            ses.commit()
            for bid in self._Curds.getBranchesIDs(b):
                self._Curds.delLatestCache(ses, bid)
                self._Curds.delSnapshotCache(ses, bid)
                self._Curds.delHistories(ses, bid)
            ses.commit()
        except Exception as e:
            ses.rollback()
            raise e
        finally:
            ses.close()

    def getAllCorporaSets(self):
        ses = self._SQLScopedSession()
        return self._Curds.getCorporaSetByID(ses, 0)

    def getAllBranches(self, CorporaSetID: int):
        ses = self._SQLScopedSession()
        return self._Curds.getBranchesByCorporaSet(
            ses, self._Curds.getCorporaSetByID(
                ses, CorporaSetID))

    def newBranch(
            self,
            CorporaSetID: int,
            BranchName: str,
            IsMainBranch: bool,
            ExtraData: str):
        ses = self._SQLScopedSession()
        try:
            c = self._Curds.getCorporasByOriginalSentenceSet(
                ses, self._Curds.getOriginalSentenceSetsByCorporaSet(
                    ses, self._Curds.getCorporaSetByID(
                        ses, CorporaSetID)))
            ncids = self._Curds.newEmptyCorporasByCorporas(ses, c)
            bsid = self._Curds.newBranchSet(
                ses, BranchName, IsMainBranch, CorporaSetID, ExtraData)
            ses.commit()
            vid = self._Curds.newVersionSet(
                ses, bsid, '')
            ses.commit()
            for ncid in ncids:
                self._Curds.newDiff(
                    ses, vid, ncid)
            ses.commit()
            ds = self._Curds.getDiffSequence(ses, bsid)
            for ncid in ncids:
                self._Curds.newLatestCache(ses, bsid, ncid, vid)
                self._Curds.newSnapshotCache(ses, bsid, vid, ds, ncid)
            ses.commit()
            ncorporas = self._Curds.getCorporasByIDs(ses, ncids)
            self._Curds.newHistoriesByCorporas(ses, bsid, vid, ncorporas)
            ses.commit()
            return bsid
        except Exception as e:
            ses.rollback()
            raise e
        finally:
            ses.close()

    def delBranch(
            self,
            BranchID: int):
        ses = self._SQLScopedSession()
        try:
            if self._Curds.isMainBranch(ses, BranchID):
                raise Exception()
            b = self._Curds.getBranchByID(ses, BranchID)
            v = self._Curds.getVersionsByBranches(ses, [b, ])
            d = self._Curds.getDiffsByVersions(ses, v)
            cd = self._Curds.getCorporasByDiffs(ses, d)
            self._Curds.delCorporas(ses, cd)
            ses.commit()
            self._Curds.delBranches(ses, [b, ])
            ses.commit()
            self._Curds.delVersions(ses, v)
            ses.commit()
            self._Curds.delDiffs(ses, d)
            ses.commit()
            self._Curds.delLatestCache(ses, BranchID)
            self._Curds.delSnapshotCache(ses, BranchID)
            self._Curds.delHistories(ses, BranchID)
            ses.commit()
        except Exception as e:
            ses.rollback()
            raise e
        finally:
            ses.close()

    def newVersion(
            self,
            BranchID: int,
            Changes: SentenceSet,
            ExtraData: str):
        if Changes.getLength() == 0:
            raise Exception
        ses = self._SQLScopedSession()
        try:
            cids = []
            for i in range(Changes.getLength()):
                cids.append(self._Curds.newCorpora(ses,
                                                   Changes.get(i)['sid'],
                                                   Changes.get(i)['pid'],
                                                   Changes.get(i)['content'],
                                                   Changes.get(i)['extra']))
            ses.commit()
            vid = self._Curds.newVersionSet(ses, BranchID, ExtraData)
            ses.commit()
            for cid in cids:
                self._Curds.newDiff(ses, vid, cid)
            ses.commit()
            self._Curds.updateLatestCacheByCorporas(ses, BranchID,
                self._Curds.getCorporasByIDs(ses, cids))
            ses.commit()
            self._Curds.updateSnapshotCacheIfNeeded(
                ses, BranchID, vid, self._SnapshotDelta)
            ses.commit()
            ncorporas = self._Curds.getCorporasByIDs(ses, cids)
            self._Curds.newHistoriesByCorporas(ses, BranchID, vid, ncorporas)
            ses.commit()
            return vid
        except Exception as e:
            ses.rollback()
            raise e
        finally:
            ses.close()

    def getParallelCorporas(
            self,
            BranchID: int):
        ses = self._SQLScopedSession()
        return ParallelSentenceSet(
            self._Curds.getSentenceSetOfOriginalSentenceSetByBranchID(
                ses, BranchID),
            self._Curds.getSentenceSetOfLatestVersionByBranchID(
                ses, BranchID))

    def getSentenceHistorySet(
            self,
            BranchID: int,
            SentenceID: int):
        ses = self._SQLScopedSession()
        ss, hvs = self._Curds.getSentenceSetHistoriesAndVersionIDsByBranchIDAndSentenceID(
            ses,
            BranchID,
            SentenceID)
        return SentenceHistorySet(ss, hvs)

    def getParagraphHistorySet(
            self,
            BranchID: int,
            ParagraphID: int):
        ses = self._SQLScopedSession()
        ph, vis = self._Curds.getParagraphHistoriesAndVersionIDsByBranchIDAndParagraphID(
            ses,
            BranchID,
            ParagraphID)
        return ParagraphHistorySet(ph, vis)

    def getBranchHistorySet(
            self,
            BranchID: int):
        ses = self._SQLScopedSession()
        bh, vids = self._Curds.getBranchHistoriesByBranchID(ses, BranchID)
        return BranchHistorySet(bh, vids)

    def getMainBranchID(
            self,
            CorporaSetID):
        ses = self._SQLScopedSession()
        return self._Curds.getMainBranchID(ses, CorporaSetID)

    def setMainBranch(
            self,
            CorporaSetID,
            BranchID):
        ses = self._SQLScopedSession()
        if self._Curds.isMainBranch(ses, BranchID):
            return
        self._Curds.setCorporaSetMainBranch(ses, CorporaSetID, BranchID)
        ses.commit()

    def coverBranchWithVersion(
            self,
            BranchID: int,
            VersionID: int):
        ses = self._SQLScopedSession()
        branch = self._Curds.getBranchByVersionID(ses, VersionID)
        newori = self._Curds.getOriginalSentenceSetsByCorporaSet(
            ses,
            self._Curds.getCorporaSetByBranch(
                ses,
                branch))
        originalBranch = self._Curds.getBranchByID(ses, BranchID)
        oriori = self._Curds.getOriginalSentenceSetsByCorporaSet(
            ses,
            self._Curds.getCorporaSetByBranch(
                ses,
                originalBranch))
        if not self._Curds.compareOriginalSentenceSets(
                ses,
                oriori, newori):
            raise Exception()
        else:
            changes, extra = self._Curds.getSentenceSetAndExtraDataByVersionID(
                ses, BranchID, VersionID)
            return self.newVersion(BranchID, changes, extra)

    def rollbackBranchToVersion(
            self,
            BranchID: int,
            VersionID: int):
        ses = self._SQLScopedSession()
        if not self._Curds.isVersionInBranch(ses, VersionID, BranchID):
            raise Exception()
        self._Curds.rollbackBranchToVersion(
            ses, BranchID, VersionID)
        ses.commit()

    def mirrorCorporaSet(
            self,
            NewCorporaSetName: str,
            CorporaSetID: int):
        ses = self._SQLScopedSession()
        ncsid = self._Curds.newCorporaSetByCorporaSet(
            ses, NewCorporaSetName,
            self._Curds.getCorporaSetByID(
                ses, CorporaSetID))
        ses.commit()
        return ncsid


def createEngine(
        engine: str = 'mysql',
        url: str = 'localhost:3306',
        user: str = 'root', password: str = '', dbname: str = 'pavis', filepath: str = '') -> pavisEngine:
    if not re.match(r'^[a-zA-Z0-9\.]*?:\d+$', url):
        raise Exception
    if engine not in ['mysql', 'sqlite3']:
        raise Exception
    dblink = ''
    if engine == 'mysql':
        dblink = 'mysql+pymysql://{}:{}@{}/{}'.format(
            user, password,
            url, dbname)
    elif engine == 'sqlite3':
        dblink = 'sqlite:///{}'.format(filepath)
    return pavisEngine(dblink)
