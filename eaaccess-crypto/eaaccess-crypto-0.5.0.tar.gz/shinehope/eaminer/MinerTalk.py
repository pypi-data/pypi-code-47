from .EAInfo import EAInfo
from .EACtrl import EACtrl
from threading import Lock
from typing import Dict
from multiprocessing.connection import _ConnectionBase

class MinerTalk:
    __conn_p: _ConnectionBase = None
    __conn_c: _ConnectionBase = None
    __EAStatusList: Dict[str, EAInfo] = {}                  # : {str, EAInfo}
    __LockList: Dict[str, Lock] = {}                        # : {str, Lock}
    __CommandCtrl: EACtrl = EACtrl()
    __LockCommand: Lock = Lock()
    __EACtrlList: Dict[str, EACtrl] = {}                    # : {str, EACtrl} 
    __LockEACtrl: Dict[str, Lock] = {}                      # : {str, Lock} 

    @classmethod
    def _conn_p_set(cls, conn=None):
        cls.__conn_p = conn
        print("MinerTalk parent pipe: ", conn)

    @classmethod
    def _conn_c_set(cls, conn=None):
        cls.__conn_c = conn
        print("MinerTalk child pipe: ", conn)

    @classmethod
    def send(cls, eaInfo:EAInfo):
        # print("MinerTalk.send...", cls.__conn_c)
        if isinstance(cls.__conn_c, _ConnectionBase):
            cls.__conn_c.send(eaInfo)
        else: 
            account:str = str(eaInfo.account).strip()

            lock: Lock = None

            try:
                # Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:           
                # if (MinerTalk.__LockList.__contains__(account)):  # 可以使用... 但是使用 __ 命名就是不希望被直接拿來用啊 !!
                if (account in cls.__LockList.keys()):
                    lock = cls.__LockList.get(account)
                else:
                    lock = Lock()       # 锁对象  
                lock.acquire()
                cls.__EAStatusList[account] = eaInfo
                cls.__LockList[account] = lock
                
            finally:
                lock.release()

    @classmethod
    def get(cls, account:str) -> EAInfo:
        eaInfo:EAInfo = None

        if isinstance(cls.__conn_p, _ConnectionBase):
            while cls.__conn_p.poll():
                eaInfo = cls.__conn_p.recv()
            return eaInfo
        else: 
            account = account.strip()
            lock:Lock = None

            try:
                # if (MinerTalk.__LockList.__contains__(account)):
                if (account in cls.__LockList.keys()):
                    lock = cls.__LockList.get(account)
                    lock.acquire()
                    eaInfo = cls.__EAStatusList.get(account)
                else:
                    eaInfo: EAInfo = None
            finally:
                if not (lock is None):
                    lock.release()

            return eaInfo

    @classmethod
    def sendCommands(cls, eaCtrl:EACtrl):
        try:
            cls.__LockCommand.acquire()
            cls.__CommandCtrl = eaCtrl
        finally:
            cls.__LockCommand.release()

    @classmethod
    def sendCommands(cls, acc:str, eaCtrl:EACtrl):
        # String account = Long.toString(eaInfo.account).trim();
        account:str = acc.strip()
        lock: Lock = None

        try:
            # if (MinerTalk.__LockEACtrl.__contains__(account)):
            if (account in cls.__LockEACtrl.keys()):
                lock = cls.__LockEACtrl.get(account)
            else:
                lock = Lock()       # 锁对象  
            lock.acquire()
            cls.__EACtrlList[account] = eaCtrl
            cls.__LockEACtrl[account] = lock            
        finally:
            lock.release()

    @classmethod
    def getCommands(cls) -> EACtrl:
        eaCtrl:EACtrl = None

        try:
            cls.__LockCommand.acquire()
            eaCtrl = cls.__CommandCtrl
            # 2019.04.30 加入此動作造成... StrategyClient 只做一個 Robot 就停止了
            # CommandCtrl = new EACtrl(); # 2019.04.30  Command 取走後, 應清為原始狀況  ?? 可以放 null 嗎 ??
            # # CommandCtrl = null;          
        finally:
            cls.__LockCommand.release()

        return eaCtrl

    @classmethod
    def getCommands(cls, account:str) -> EACtrl:
        eaCtrl: EACtrl = None

        account = account.strip()
        lock:Lock = None

        try:
            # if (MinerTalk.__LockEACtrl.__contains__(account)):
            if (account in cls.__LockEACtrl.keys()):
                lock = cls.__LockEACtrl.get(account)
                lock.acquire()
                eaCtrl = cls.__EACtrlList.pop(account)
            else:
                eaCtrl: EACtrl = None
        finally:
            if not (lock is None):
                lock.release()

        return eaCtrl