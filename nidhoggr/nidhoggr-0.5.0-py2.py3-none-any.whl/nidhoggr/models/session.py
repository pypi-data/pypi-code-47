from typing import Optional, Union, List

from pydantic import BaseModel

from nidhoggr.utils.transformer import YggdrasilRequestTransformer, JSONResponseTransformer, LegacyRequestTransformer


class UserProperty(BaseModel):
    name: str
    value: str

    class Config:
        allow_mutation = False
        ignore_extra = False

    def __hash__(self):
        return hash((self.name, self.value))

    def verify(self, *, key: bytes):
        return True

    @property
    def unsigned(self):
        return self


class SignedUserProperty(UserProperty):
    signature: Optional[str] = None

    class Config:
        allow_mutation = False
        ignore_extra = False

    def __hash__(self):
        return hash((self.name, self.value, self.signature))

    def verify(self, *, key: bytes):
        from nidhoggr.utils.crypto import verify_property
        return verify_property(public_key=key, prop=self)

    @property
    def unsigned(self):
        return UserProperty(name=self.name, value=self.value)


class JoinRequest(BaseModel, YggdrasilRequestTransformer):
    accessToken: str
    selectedProfile: str
    serverId: str

    class Config:
        allow_mutation = False


class HasJoinedRequestBase(BaseModel):
    username: str
    serverId: str
    ip: Optional[str]


class HasJoinedRequest(HasJoinedRequestBase, YggdrasilRequestTransformer):

    class Config:
        allow_mutation = False


class HasJoinedRequestLegacy(HasJoinedRequestBase, LegacyRequestTransformer):

    class Config:
        allow_mutation = False


class JoinedResponse(BaseModel, JSONResponseTransformer):
    id: str
    name: str
    properties: Union[List[UserProperty], List[SignedUserProperty]]

    class Config:
        allow_mutation = False


class ProfileRequestBase(BaseModel):
    id: str
    unsigned: bool = False

    class Config:
        allow_mutation = False


class ProfileRequest(ProfileRequestBase, YggdrasilRequestTransformer):

    class Config:
        allow_mutation = False


class ProfileRequestLegacy(ProfileRequestBase, LegacyRequestTransformer):

    class Config:
        allow_mutation = False
