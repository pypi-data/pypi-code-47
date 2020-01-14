from types import TracebackType
from typing import Any, Callable, Optional, Type

from httpx import AsyncClient, exceptions

from .login import OAuth
from .model import CurrentlyPlaying, OAuthTokens, User
from .player import get_current_song
from .user import get_user
from .utils.log import LOGGER


def requires_tokens(function: Callable) -> Callable:
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        API: "SpotifyWebAPI" = args[0]
        if API.client is None or API.oauth is None:
            raise Exception(
                "Initialize SpotifyWebAPI object! Example: `with API(oauth) as API:`"
            )

        if API.oauth.tokens is None:
            raise Exception("Tokens not found on OAuth used by SpotifyWebAPI!")

        # In headers.setter dict is converted to Headers
        API.client.headers = API.oauth.tokens.headers  # type: ignore[assignment]
        return await function(*args, **kwargs)

    return wrapper


class SpotifyWebAPI:
    def __init__(
        self, oauth: Optional[OAuth] = None, suppress_errors: bool = False
    ) -> None:
        self.oauth: Optional[OAuth] = oauth
        self.suppress_errors = suppress_errors
        self.client: Optional[AsyncClient] = None

    def __call__(self, oauth: Optional[OAuth] = None) -> "SpotifyWebAPI":
        self.oauth = oauth or self.oauth
        if not self.client:
            self.client = AsyncClient(timeout=0.5)

        return self

    def __enter__(self) -> "SpotifyWebAPI":
        if self.oauth is None or self.client is None:
            raise ValueError(
                "Initialize SpotifyWebAPI object! Example: `with API(oauth) as API:`"
            )

        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> bool:
        if exc_type == exceptions.TimeoutException:
            LOGGER.error("Request timed out!", exc_info=True)
            return self.suppress_errors

        if exc_type in (TypeError, KeyError):
            LOGGER.error("JSON parsing error!", exc_info=True)
            return self.suppress_errors

        return self.suppress_errors

    @requires_tokens
    async def get_user(self) -> Optional[User]:
        # Decorator @requires_tokens makes sure self.client is not None
        return await get_user(self.client)  # type: ignore[arg-type]

    @requires_tokens
    async def get_current_song(
        self, current_song: Optional[CurrentlyPlaying]
    ) -> Optional[CurrentlyPlaying]:
        return await get_current_song(
            # Decorator @requires_tokens makes sure self.client is not None
            self.client,  # type: ignore[arg-type]
            current_song,
        )
