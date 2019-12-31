from nidhoggr.bl import BaseUserRepo
from nidhoggr.errors.common import BadPayload, BadRequest
from nidhoggr.models.auth import Profile, UserInstance, RefreshResponse
from ..conftest import cast


def test_empty_credentials(user, refresh):
    assert cast[BadPayload](refresh({}))
    assert cast[BadPayload](refresh({"accessToken": user.access}))
    assert cast[BadPayload](refresh({"clientToken": user.client}))


def test_nonexistent_token_pair(refresh):
    response = refresh({
        "accessToken": "anything",
        "clientToken": "anything"
    })
    assert response.status_code == 400
    assert cast[BadRequest](response)


def test_access_token_refreshed(users: BaseUserRepo, user, refresh):
    response = refresh({
        "accessToken": user.access,
        "clientToken": user.client
    })
    assert response.status_code == 200
    result = cast[RefreshResponse](response)
    assert result is not None
    assert result.accessToken != user.access
    fresh = users.get_user(uuid=user.uuid)
    assert fresh.access == result.accessToken


def test_client_token_mirrored_back(user, refresh):
    response = refresh({
        "accessToken": user.access,
        "clientToken": user.client
    })
    assert response.status_code == 200
    result = cast[RefreshResponse](response)
    assert result is not None
    assert result.clientToken == user.client


def test_selected_profile(user, refresh):
    response = refresh({
        "accessToken": user.access,
        "clientToken": user.client
    })
    assert response.status_code == 200
    result = cast[RefreshResponse](response)
    assert result is not None
    assert isinstance(result.selectedProfile, Profile)


def test_user_instance_request(user, refresh):
    response = refresh({
        "accessToken": user.access,
        "clientToken": user.client,
        "requestUser": True
    })
    assert response.status_code == 200
    result = cast[RefreshResponse](response)
    assert result is not None
    assert isinstance(result.user, UserInstance)
