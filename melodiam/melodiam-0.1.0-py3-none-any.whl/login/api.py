from base64 import b64encode
from typing import Dict, Optional
from urllib.parse import parse_qsl, urlparse

from httpx import AsyncClient

from ..model import OAuthTokens
from ..utils.events import Event

URL_AUTHORIZE = "https://accounts.spotify.com/authorize"
URL_TOKEN = "https://accounts.spotify.com/api/token"


class OAuth:
    """
        All auth data from app's side that is required
        for Spotify Web API OAuth2.0 authentication process.
    """

    def __init__(
        self, client_id: str, client_secret: str, scope: str, redirect_uri: str
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.redirect_uri = redirect_uri

        self.tokens: Optional[OAuthTokens] = None
        self._client: Optional[AsyncClient] = None

        # Create Basic Auth header for making requests as app
        auth_value: str = b64encode(
            f"{client_id}:{client_secret}".encode("ascii")
        ).decode("ascii")
        self.headers = {"Authorization": f"Basic {auth_value}"}

        # Create URL that user should use to login to Spotify
        # and allow our app to access their data
        self.url = (
            f"{URL_AUTHORIZE}?client_id={client_id}&scope={scope}"
            f"&response_type=code&redirect_uri={redirect_uri}"
        )

        self.on_new_tokens = Event()
        self.on_refresh_tokens = Event()

    @property
    def client(self) -> AsyncClient:
        if not self._client:
            self._client = AsyncClient(timeout=0.5, headers=self.headers)

        return self._client

    @staticmethod
    def get_tokens_data(code: str, redirect_uri: str) -> dict:
        """
            Data with code from OAuth2.0 authentication
            that should be sent to get tokens.
        """
        return {
            "code": code,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }

    async def get_tokens(self, code: str) -> None:
        """
            Method to exchange code for tokens
            after successful OAuth2.0 authentication.

            Documentation: https://developer.spotify.com/documentation/general/guides/authorization-guide/

            Responses from Spotify Web API:
            - (Success) 200 OK with JSON like below:
                {
                    "access_token": "NgCXRK...MzYjw",
                    "token_type": "Bearer",
                    "scope": "user-read-private user-read-email",
                    "expires_in": 3600,
                    "refresh_token": "NgAagA...Um_SHo"
                }
            - (Fail) Everything else
        """
        async with self.client as client:
            response = await client.post(
                URL_TOKEN, data=OAuth.get_tokens_data(code, self.redirect_uri)
            )

        if response.status_code != 200:
            raise Exception(f"Wrong code ({code}) used to get tokens!")

        self.tokens = OAuthTokens.from_json(response.text)
        await self.on_new_tokens(tokens=self.tokens)

    @staticmethod
    def get_redirect_code_from_query(query_params: Dict[str, str]) -> str:
        """
            Processing query parameters passed to Redirect URI
            after OAuth2.0 authentication.
            Should return code that can be used to get tokens from Spotify.

            - Raises Exception if authentication error happened
            - Raises AttributeError if there is no `code` in query params
        """
        if "error" in query_params:
            raise Exception(
                f"Spotify OAuth2.0 failed! Spotify response: {query_params.get('error')}"
            )

        if not "code" in query_params:
            raise AttributeError(
                f"Query param `code` is missing in redirect URI! Query params: {query_params}"
            )

        return query_params["code"]

    @staticmethod
    def get_redirect_code_from_url(url: str) -> str:
        """
            Processing Redirect URI after OAuth2.0 authentication.
            Should return code that can be used to get tokens from Spotify.

            - Raises Exception if authentication error happened
            - Raises AttributeError if there is no `code` in URL's query params
        """
        query_params = dict(parse_qsl(urlparse(url).query))
        return OAuth.get_redirect_code_from_query(query_params)

    @staticmethod
    def refresh_tokens_data(refresh_token: str) -> dict:
        """
            Data with refresh_token from token API request
            that should be sent to refresh tokens.
        """
        return {"refresh_token": refresh_token, "grant_type": "authorization_code"}

    async def refresh_tokens(self) -> None:
        """
            Method to refresh tokens using refresh_token from previous OAuth2.0 request.

            Documentation: https://developer.spotify.com/documentation/general/guides/authorization-guide/

            Responses from Spotify Web API:
            - (Success) 200 OK with JSON like below:
                {
                    "access_token": "NgA6ZcYI...ixn8bUQ",
                    "token_type": "Bearer",
                    "scope": "user-read-private user-read-email",
                    "expires_in": 3600
                }
            - (Fail) Everything else
        """
        if not self.tokens:
            raise Exception("No tokens to refresh!")

        async with self.client as client:
            response = await client.post(
                URL_TOKEN, data=OAuth.refresh_tokens_data(self.tokens.refresh_token)
            )

        if response.status_code != 200:
            raise Exception(
                f"Wrong refresh token ({self.tokens.refresh_token}) used for refreshing access token!"
            )

        self.tokens = OAuthTokens.from_json(response.text, self.tokens.refresh_token)
        await self.on_refresh_tokens(tokens=self.tokens)
