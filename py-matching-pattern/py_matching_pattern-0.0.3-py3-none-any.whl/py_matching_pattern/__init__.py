
from threading import Lock
from copy import deepcopy
from uuid import uuid4,UUID
from typing import Sequence, TypeVar, Generic, Any, Dict,  Mapping, Union, List, Optional

class InvalidKeySize(Exception):
    pass

class InvalidKeyCount(Exception):
    pass

class InvalidNodeInternalException(Exception):
    pass

class KeyNotFound(Exception):
    pass

K = TypeVar('K')
V = TypeVar('V')

class PatternMatchStore(Generic[K,V]):

    __default: UUID

    __db: Mapping[Any,Any]
    __lock: Lock
    __stage: Dict[Any,Any]
    __keysize: int
    __raise_notfound: bool

    def __init__(self,keysize: int=1,raise_notfound: bool=False) -> None:
        if keysize < 1:
            raise InvalidKeySize

        self.__db = {}
        self.__lock = Lock()
        self.__stage = {}
        self.__keysize=keysize
        self.__raise_notfound = raise_notfound

        self.default=uuid4()

    def put(self,keys: Sequence[K], value: V) -> None:
        if(len(keys)<self.__keysize):
            raise InvalidKeyCount

        node=self.__stage
        for n in range(self.__keysize):
            key=keys[n]
            if n == self.__keysize - 1:
                node[key]=value
            else:
                if key not in node:
                    node[key]={}
                node=node[key]
                
    def clean(self) -> None:
        self.__stage={}

    def commit(self) -> None:
        dbcopy=deepcopy(self.__stage)
        self.__lock.acquire(blocking=True,timeout=-1)
        self.__db=dbcopy
        self.__lock.release()
    
    def get(self, keys: Sequence[K]) -> Union[V,None,Any]:
        if(len(keys)<self.__keysize):
            raise InvalidKeyCount

        self.__lock.acquire(blocking=True,timeout=-1)
        value = self.__get(keys=keys)
        self.__lock.release()

        if value is None and self.__raise_notfound:
            raise KeyNotFound

        return value

    def __default_filled(self,keys: Sequence[K], key_mask: str) -> Sequence[Union[K,UUID]]:
        # TODO: there is a better solution
        new_keys: List[Union[K,UUID]] =[]
        for n in range(self.__keysize):
            mask = key_mask[n]
            if mask == "1":
                new_keys.append(keys[n])
            else:
                new_keys.append(self.default)
        
        return new_keys

    def __get(self,keys: Sequence[K]) -> Union[V,None,Any]:
        int_limit = pow(2,self.__keysize)
        current=1
        
        while current <= int_limit:
            key_mask: str = format(int_limit - current,f"0{self.__keysize}b") # eg 010101
            current_keys: Sequence[Union[K,UUID]] = self.__default_filled(keys=keys,key_mask=key_mask) # zeros are default

            node=self.__db

            for n in range(self.__keysize):
                key=current_keys[n]

                if key in node:
                    if n+1 == self.__keysize:
                        v= node[key]
                        return v
                    node=node[key]
                    continue
                else:
                    current = current + 1
                    break

        return None
