from typing import Union

from nidhoggr.bl import BaseUserRepo, BLConfig, BaseTextureRepo
from nidhoggr.errors.common import YggdrasilError
from nidhoggr.models.session import HasJoinedRequestLegacy, ProfileRequestLegacy, JoinedResponse
from nidhoggr.utils.decorator import typed
from nidhoggr.views import session


# noinspection PyPep8Naming
@typed
def hasJoined(req: HasJoinedRequestLegacy, users: BaseUserRepo) -> Union[JoinedResponse, YggdrasilError]:
    return session.has_joined.__wrapped__(req, users)


@typed
def profile(
    req: ProfileRequestLegacy,
    users: BaseUserRepo,
    config: BLConfig,
    textures: BaseTextureRepo
) -> Union[JoinedResponse, YggdrasilError]:
    return session.profile.__wrapped__(req, users, config, textures)


__all__ = {"hasJoined", "profile"}
