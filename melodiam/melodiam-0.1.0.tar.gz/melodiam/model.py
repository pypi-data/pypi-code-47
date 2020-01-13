import json
from copy import copy
from enum import Enum
from time import time
from typing import Dict, List, Optional

from .datastructures import Serializable


class OAuthTokens(Serializable):
    """
        Tokens and timestamps for authorization purposes.
    """

    __slots__ = (
        "access_token",
        "token_type",
        "scope",
        "refresh_token",
        "expires_in",
        "expires_at",
    )

    def __init__(
        self,
        access_token: str,
        scope: str,
        refresh_token: str,
        expires_in: int,
        token_type: str = "Bearer",
        expires_at: float = 0,
    ) -> None:
        self.access_token = access_token
        self.token_type = token_type
        self.scope = scope
        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.expires_at = time() + self.expires_in if expires_at == 0 else expires_at

    @property
    def seconds_until_expiration(self) -> float:
        return self.expires_at - time()

    @property
    def is_valid(self) -> bool:
        return self.seconds_until_expiration > 0

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.access_token}"}

    @staticmethod
    def from_json(json_tokens: str, refresh_token: str = "") -> "OAuthTokens":
        tokens = json.loads(json_tokens)
        # When we request for refreshed access_token - we
        # don't get "refresh_token" in JSON response from API.
        if "refresh_token" not in tokens:
            tokens["refresh_token"] = refresh_token

        return OAuthTokens(**tokens)


class ContextType(Enum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"


class CurrentlyPlayingType(Enum):
    TRACK = "track"
    EPISODE = "episode"
    AD = "ad"
    UNKNOWN = "unknown"


class Actions(Serializable):
    __slots__ = "disallows"

    def __init__(self, disallows: Dict[str, bool]) -> None:
        self.disallows = disallows


class Restrictions(Serializable):
    __slots__ = "reason"

    def __init__(self, reason: str) -> None:
        self.reason = reason


class ExternalID(Serializable):
    __slots__ = ("isrc", "ean", "upc")

    def __init__(
        self,
        isrc: Optional[str] = None,
        ean: Optional[str] = None,
        upc: Optional[str] = None,
    ) -> None:
        self.isrc = isrc
        self.ean = ean
        self.upc = upc


class ExternalURL(Serializable):
    __slots__ = "spotify"

    def __init__(self, spotify: str) -> None:
        self.spotify = spotify


class Image(Serializable):
    __slots__ = ("url", "width", "height")

    def __init__(
        self, url: str, width: Optional[int] = None, height: Optional[int] = None
    ) -> None:
        self.url = url
        self.width = width
        self.height = height


class Context(Serializable):
    __slots__ = ("uri", "type", "href", "external_urls")

    def __init__(
        self,
        uri: str,
        type: ContextType,
        href: Optional[str] = None,
        external_urls: Optional[ExternalURL] = None,
    ) -> None:
        self.uri = uri
        self.href = href
        self.type = type
        self.external_urls = external_urls

    @staticmethod
    def from_dict(context: dict) -> "Context":
        context["type"] = ContextType(context["type"])
        if "external_urls" in context:
            context["external_urls"] = ExternalURL(**context["external_urls"])

        return Context(**context)


class SpotifyObject(Serializable):
    """
        Base class for most of the
        objects Spotify Web API returns.
    """

    __slots__ = ("id", "uri", "href", "external_urls", "type")

    def __init__(
        self, id: str, uri: str, href: str, external_urls: ExternalURL, type: str
    ) -> None:
        self.id = id
        self.uri = uri
        self.href = href
        self.type = type
        self.external_urls = external_urls

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False

        if not isinstance(other, (SpotifyObject, str)):
            raise TypeError("Wrong type to compare (not SpotifyObject or str)!")

        if isinstance(other, str):
            return self.id == other

        return self.id == other.id


class NamedSpotifyObject(SpotifyObject):
    """
        SpotifyObject with name attribute.
    """

    __slots__ = "name"

    def __init__(
        self,
        name: str,
        id: str,
        uri: str,
        href: str,
        external_urls: ExternalURL,
        type: str,
    ) -> None:
        super().__init__(id, uri, href, external_urls, type)
        self.name = name


class LinkedTrack(SpotifyObject):
    __slots__ = ()

    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        external_urls: ExternalURL,
        type: str = "track",
    ) -> None:
        super().__init__(id, uri, href, external_urls, type="track")

    @staticmethod
    def from_dict(linked_track: dict) -> "LinkedTrack":
        linked_track["external_urls"] = ExternalURL(**linked_track["external_urls"])
        return LinkedTrack(**linked_track)


class SimplifiedArtist(NamedSpotifyObject):
    # TODO
    def __init__(self, **kwargs: str) -> None:
        vars(self).update(kwargs)

    @staticmethod
    def from_dict(artist: dict) -> "SimplifiedArtist":
        return SimplifiedArtist(**artist)

    @staticmethod
    def from_json(artist_json: str) -> "SimplifiedArtist":
        artist = json.loads(artist_json)
        return SimplifiedArtist.from_dict(artist)


class SimplifiedAlbum(NamedSpotifyObject):
    __slots__ = (
        "album_type",
        "available_markets",
        "release_date",
        "release_date_precision",
        "artists",
        "images",
        "album_group",
        "restrictions",
    )

    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        name: str,
        external_urls: ExternalURL,
        album_type: str,
        artists: List[SimplifiedArtist],
        available_markets: List[str],
        images: List[Image],
        release_date: str,
        release_date_precision: str,
        album_group: Optional[str] = None,
        restrictions: Optional[Restrictions] = None,
        type: str = "album",
    ) -> None:
        super().__init__(id, uri, href, name, external_urls, type="album")
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.images = images
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.album_group = album_group

        # Only exist if Track Relinking applied
        self.restrictions = restrictions

    @staticmethod
    def from_dict(album: dict) -> "SimplifiedAlbum":
        album["artists"] = [
            SimplifiedArtist.from_dict(artist) for artist in album["artists"]
        ]
        album["external_urls"] = ExternalURL(**album["external_urls"])
        album["images"] = [Image(**image) for image in album["images"]]
        if "restrictions" in album:
            album["restrictions"] = Restrictions(**album["restrictions"])

        return SimplifiedAlbum(**album)

    @staticmethod
    def from_json(album_json: str) -> "SimplifiedAlbum":
        album = json.loads(album_json)
        return SimplifiedAlbum.from_dict(album)


class FullTrack(NamedSpotifyObject):
    __slots__ = (
        "available_markets",
        "disc_number",
        "duration_ms",
        "explicit",
        "popularity",
        "track_number",
        "is_local",
        "album",
        "artists",
        "external_ids",
        "preview_url",
        "is_playable",
        "linked_from",
        "restrictions",
    )

    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        name: str,
        external_urls: ExternalURL,
        album: SimplifiedAlbum,
        artists: List[SimplifiedArtist],
        available_markets: List[str],
        disc_number: int,
        duration_ms: int,
        explicit: bool,
        external_ids: ExternalID,
        popularity: int,
        track_number: int,
        is_local: bool,
        preview_url: Optional[str] = None,
        is_playable: Optional[bool] = None,
        linked_from: Optional[LinkedTrack] = None,
        restrictions: Optional[Restrictions] = None,
        type: str = "track",
    ) -> None:
        super().__init__(id, uri, href, name, external_urls, type="track")
        self.album = album
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.popularity = popularity
        self.track_number = track_number
        self.is_local = is_local
        self.preview_url = preview_url

        # Only exist if Track Relinking applied
        self.is_playable = is_playable
        self.linked_from = linked_from
        self.restrictions = restrictions

    @property
    def start_zone(self) -> float:
        return self.duration_ms * 0.2

    @property
    def end_zone(self) -> float:
        return self.duration_ms * 0.8

    @staticmethod
    def from_dict(track: dict) -> "FullTrack":
        track["external_urls"] = ExternalURL(**track["external_urls"])
        track["album"] = SimplifiedAlbum.from_dict(track["album"])
        track["artists"] = [
            SimplifiedArtist.from_dict(artist) for artist in track["artists"]
        ]
        track["external_ids"] = ExternalID(**track["external_ids"])

        # Only exist if Track Relinking applied
        if "linked_from" in track:
            track["linked_from"] = LinkedTrack.from_dict(track["linked_from"])
        if "restrictions" in track:
            track["restrictions"] = Restrictions(**track["restrictions"])

        return FullTrack(**track)

    @staticmethod
    def from_json(track_json: str) -> "FullTrack":
        track = json.loads(track_json)
        return FullTrack.from_dict(track)


class CurrentlyPlaying(Serializable):
    __slots__ = (
        "timestamp",
        "is_playing",
        "currently_playing_type",
        "actions",
        "context",
        "progress_ms",
        "item",
    )

    def __init__(
        self,
        timestamp: int,
        is_playing: bool,
        currently_playing_type: CurrentlyPlayingType,
        actions: Actions,
        context: Optional[Context] = None,
        progress_ms: Optional[int] = None,
        item: Optional[FullTrack] = None,
    ) -> None:
        self.timestamp = timestamp
        self.is_playing = is_playing
        self.currently_playing_type = currently_playing_type
        self.actions = actions
        self.context = context
        self.progress_ms = progress_ms
        self.item = item

    @property
    def progress(self) -> int:
        return 0 if self.progress_ms is None else self.progress_ms

    @property
    def duration(self) -> int:
        return 0 if self.item is None else self.item.duration_ms

    @property
    def start_zone(self) -> float:
        return 0 if self.item is None else self.item.start_zone

    @property
    def end_zone(self) -> float:
        return 0 if self.item is None else self.item.end_zone

    @staticmethod
    def from_json(
        currently_playing_json: str, current_song: Optional["CurrentlyPlaying"] = None
    ) -> "CurrentlyPlaying":
        currently_playing = json.loads(currently_playing_json)
        item = currently_playing["item"]

        # If song did not change - we only update playback
        if item is not None and current_song == item["id"]:
            current_song_copy = copy(current_song)
            current_song_copy.timestamp = currently_playing["timestamp"]
            current_song_copy.is_playing = not currently_playing["is_playing"]
            current_song_copy.progress_ms = currently_playing["progress_ms"]
            return current_song_copy

        currently_playing["currently_playing_type"] = CurrentlyPlayingType(
            currently_playing["currently_playing_type"]
        )
        currently_playing["actions"] = Actions(**currently_playing["actions"])
        currently_playing["context"] = Context.from_dict(currently_playing["context"])
        currently_playing["item"] = FullTrack.from_dict(item)

        return CurrentlyPlaying(**currently_playing)

    def __eq__(self, other: object) -> bool:
        if other is None:
            return False

        if not isinstance(other, (CurrentlyPlaying, str)):
            raise TypeError("Wrong type to compare (not CurrentlyPlaying or str)!")

        if isinstance(other, str):
            return self.item == other

        return self.item == other.item


class Followers(Serializable):
    __slots__ = ("total", "href")

    def __init__(self, total: int, href: Optional[str] = None) -> None:
        self.total = total
        self.href = href


class User(SpotifyObject):
    __slots__ = ("display_name", "followers", "images", "email", "country", "product")

    def __init__(
        self,
        id: str,
        uri: str,
        href: str,
        external_urls: ExternalURL,
        followers: Followers,
        images: List[Image],
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        country: Optional[str] = None,
        product: Optional[str] = None,
        type: str = "user",
    ) -> None:
        super().__init__(id, uri, href, external_urls, type="user")
        self.display_name = display_name
        self.followers = followers
        self.images = images

        # Only exist if scope user-read-email is granted
        self.email = email

        # Only exist if scope user-read-private is granted
        self.country = country
        self.product = product

    @staticmethod
    def from_json(user_json: str) -> "User":
        user = json.loads(user_json)
        user["external_urls"] = ExternalURL(**user["external_urls"])
        user["followers"] = Followers(**user["followers"])
        user["images"] = [Image(**image) for image in user["images"]]

        return User(**user)
