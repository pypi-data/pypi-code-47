import pytest

from nidhoggr.bl import User, BLConfig
from nidhoggr.errors.auth import InvalidProfile
from nidhoggr.errors.common import BadPayload
from nidhoggr.models.session import UserProperty, SignedUserProperty, JoinedResponse
from ..conftest import cast

with_sign = pytest.mark.parametrize(
    ["unsigned"],
    [(True,), (False,)],
    ids=["unsigned", "signed"]
)


def test_empty_credentials(profile):
    assert cast[BadPayload](profile({}))


@with_sign
def test_nonexistent_user(unsigned: bool, profile):
    assert cast[InvalidProfile](profile({"id": "anything", "unsigned": unsigned}))


@with_sign
def test_profile_simple(user: User, unsigned: bool, profile):
    response = profile({"id": user.uuid, "unsigned": unsigned})
    result = cast[JoinedResponse](response)
    assert result is not None
    assert result.id == user.uuid
    assert result.name == user.login


@with_sign
def test_properties(config: BLConfig, new_user: User, unsigned: bool, profile):
    response = profile({"id": new_user.uuid})
    result = cast[JoinedResponse](response)
    assert result is not None
    assert all(
        type(p) is unsigned and UserProperty or SignedUserProperty
        for p
        in result.properties
    )
    assert all(p.verify(key=config.key_pair.public) for p in result.properties)
    assert set(p.unsigned for p in result.properties) >= set(new_user.properties)


@with_sign
def test_texture_exists(user: User, unsigned: bool, profile):
    response = profile({"id": user.uuid, "unsigned": unsigned})
    result = cast[JoinedResponse](response)
    assert result is not None
    texture_prop = ([p for p in result.properties if p.name == "textures"] or [None])[0]
    assert isinstance(texture_prop, UserProperty)


@with_sign
def test_texture_attached(user: User, unsigned: bool, profile):
    response = profile({"id": user.uuid, "unsigned": unsigned})
    result = cast[JoinedResponse](response)
    assert result is not None
    diff = set(p.unsigned for p in result.properties) - set(user.properties)
    assert len(diff) == 1
    assert diff.pop().name == "textures"
