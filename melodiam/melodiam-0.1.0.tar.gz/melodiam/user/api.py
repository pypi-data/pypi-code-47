from typing import Optional

from httpx import AsyncClient

from ..model import User

URL_ME = "https://api.spotify.com/v1/me"


async def get_user(client: AsyncClient) -> Optional[User]:
    """
        Method to get current user information.
        Requires access token to be set in `client` Authorization header.
        Requires user-read-email scope for email field.
        Requires user-read-private scope for country and product fields.

        Documentation: https://developer.spotify.com/documentation/web-api/reference/users-profile/get-current-users-profile/

        Responses from Spotify Web API:
        - (Success) 200 OK with JSON like below:
            {
                "birthdate": "1937-06-01",
                "country": "SE",
                "display_name": "JM Wizzler",
                "email": "email@example.com",
                "external_urls": {
                    "spotify": "https://open.spotify.com/user/wizzler"
                },
                "followers": {
                    "href": null,
                    "total": 3829
                },
                "href": "https://api.spotify.com/v1/users/wizzler",
                "id": "wizzler",
                "images": [
                    {
                        "height": null,
                        "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-frc3/t1.0-1/1970403_10152215092574354_1798272330_n.jpg",
                        "width": null
                    }
                ],
                "product": "premium",
                "type": "user",
                "uri": "spotify:user:wizzler"
            }
        - (Fail) Everything else
    """
    response = await client.get(URL_ME)
    if response.status_code != 200:
        return None

    return User.from_json(response.text)
