from typing import List, Optional

from httpx import AsyncClient

from ..model import CurrentlyPlaying, FullTrack
from ..utils.events import Event

URL_CURRENTLY_PLAYING = "https://api.spotify.com/v1/me/player/currently-playing"

#: Allowable error (2 seconds) in difference between
#: two Playback's timestamps difference and progresses diference.
ALLOWABLE_ERROR = 2 * 1000

#: How much time (30 seconds) should song be listened for
#: to end up in history
HISTORY_THRESHOLD = 30 * 1000


class Player:
    def __init__(self) -> None:
        self._song: Optional[CurrentlyPlaying] = None
        self._listened_for = 0
        self._repeats = 0
        self._history: List[FullTrack] = []

        # Player object Events
        self.on_reset = Event()
        self.on_song_update = Event()
        self.on_history_update = Event()
        self.on_playback_update = Event()

    @property
    def song(self) -> Optional[CurrentlyPlaying]:
        return self._song

    @property
    def timestamp(self) -> int:
        return 0 if self._song is None else self._song.timestamp

    @property
    def is_playing(self) -> bool:
        return True if self._song is None else self._song.is_playing

    @property
    def progress(self) -> int:
        return 0 if self._song is None else self._song.progress

    @property
    def duration(self) -> int:
        return 0 if self._song is None else self._song.duration

    @property
    def listened_for(self) -> int:
        return self._listened_for

    @property
    def repeats(self) -> int:
        return self._repeats

    @property
    def history(self) -> List[FullTrack]:
        return self._history

    def is_playback_changed(self, new: CurrentlyPlaying) -> bool:
        """
        What counts as changed playback:
            - If paused state was changed (unpaused to paused or vice versa)
            - If progress was changed in any direction
        """
        if self.is_playing != new.is_playing or self.progress != new.progress:
            return True

        return False

    def is_playback_manipulated(self, new: CurrentlyPlaying) -> bool:
        """
        What counts as playback manipulation:
            - If new progress is less than old one
            Example: progress was at 1:04, 5 seconds passed and now it is at 1:01

            - If new progress is moved past old at a mark that should not pass yet
            Example: progress was at 1:04, 5 seconds passed and it is at 1:15 now
        """
        time_passed = new.timestamp - self.timestamp
        progress_difference = new.progress - self.progress
        return time_passed + ALLOWABLE_ERROR < progress_difference < 0

    def is_repeat_happened(self, new: CurrentlyPlaying) -> bool:
        """
        What counts as repeat of a song:
            - If song was at the end (>=80%) and now at the start (<=20%)
        """
        return self.progress >= new.end_zone and self.progress <= new.start_zone

    async def update_song(self, new: CurrentlyPlaying) -> None:
        if self._song == new:
            await self.update_playback(new)
            return

        if (
            self._song is not None
            and self._song.item is not None
            and self._listened_for >= HISTORY_THRESHOLD
            and (len(self.history) == 0 or self.history[0] != self._song.item)
        ):
            self.history.insert(0, self._song.item)
            await self.on_history_update()

        self._song = new
        self._listened_for = 0
        self._repeats = 0
        await self.on_song_update()

    async def update_playback(self, new: CurrentlyPlaying) -> None:
        if not self.is_playback_changed(new):
            return

        progress_difference = new.progress - self.progress
        if self.is_playback_manipulated(new):
            progress_difference = 0
            if self.is_repeat_happened(new):
                self._repeats += 1
                progress_difference = (self.duration - self.progress) + new.progress

        self._listened_for += progress_difference
        await self.on_playback_update()

    async def reset(self) -> None:
        self._song = None
        self._history = []
        self.on_reset()


async def get_current_song(
    client: AsyncClient, current_song: Optional[CurrentlyPlaying] = None
) -> Optional[CurrentlyPlaying]:
    """
        Method to get currently plaing song.
        Requires access token to be set in `client` Authorization header.
        Requires user-read-currently-playing scope.

        Documentation: https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/

        Responses from Spotify Web API:
        - (Success) 204 NO CONTENT with no payload
        - (Success) 200 OK with JSON like below:
            {
                "context": {
                    "external_urls" : {
                        "spotify" : "http://open.spotify.com/user/spotify/playlist/49znshcYJROspEqBoHg3Sv"
                    },
                    "href" : "https://api.spotify.com/v1/users/spotify/playlists/49znshcYJROspEqBoHg3Sv",
                    "type" : "playlist",
                    "uri" : "spotify:user:spotify:playlist:49znshcYJROspEqBoHg3Sv"
                },
                "timestamp": 1490252122574,
                "progress_ms": 44272,
                "is_playing": true,
                "currently_playing_type": "track",
                "actions": {
                    "disallows": {
                        "resuming": true
                    }
                },
                "item": {
                    "album": {
                    "album_type": "album",
                    "external_urls": {
                        "spotify": "https://open.spotify.com/album/6TJmQnO44YE5BtTxH8pop1"
                    },
                    "href": "https://api.spotify.com/v1/albums/6TJmQnO44YE5BtTxH8pop1",
                    "id": "6TJmQnO44YE5BtTxH8pop1",
                    "images": [
                        {
                            "height": 640,
                            "url": "https://i.scdn.co/image/8e13218039f81b000553e25522a7f0d7a0600f2e",
                            "width": 629
                        },
                        {
                            "height": 300,
                            "url": "https://i.scdn.co/image/8c1e066b5d1045038437d92815d49987f519e44f",
                            "width": 295
                        },
                        {
                            "height": 64,
                            "url": "https://i.scdn.co/image/d49268a8fc0768084f4750cf1647709e89a27172",
                            "width": 63
                        }
                    ],
                    "name": "Hot Fuss",
                    "type": "album",
                    "uri": "spotify:album:6TJmQnO44YE5BtTxH8pop1"
                    },
                    "artists": [
                        {
                            "external_urls": {
                                "spotify": "https://open.spotify.com/artist/0C0XlULifJtAgn6ZNCW2eu"
                            },
                            "href": "https://api.spotify.com/v1/artists/0C0XlULifJtAgn6ZNCW2eu",
                            "id": "0C0XlULifJtAgn6ZNCW2eu",
                            "name": "The Killers",
                            "type": "artist",
                            "uri": "spotify:artist:0C0XlULifJtAgn6ZNCW2eu"
                        }
                    ],
                    "available_markets": [
                        "AD",
                        "AR",
                        "TW",
                        "UY"
                    ],
                    "disc_number": 1,
                    "duration_ms": 222075,
                    "explicit": false,
                    "external_ids": {
                        "isrc": "USIR20400274"
                    },
                    "external_urls": {
                        "spotify": "https://open.spotify.com/track/0eGsygTp906u18L0Oimnem"
                    },
                    "href": "https://api.spotify.com/v1/tracks/0eGsygTp906u18L0Oimnem",
                    "id": "0eGsygTp906u18L0Oimnem",
                    "name": "Mr. Brightside",
                    "popularity": 0,
                    "preview_url": "http://d318706lgtcm8e.cloudfront.net/mp3-preview/f454c8224828e21fa146af84916fd22cb89cedc6",
                    "track_number": 2,
                    "type": "track",
                    "uri": "spotify:track:0eGsygTp906u18L0Oimnem"
                }
            }
        - (Fail) Everything else
    """
    response = await client.get(URL_CURRENTLY_PLAYING)
    if response.status_code == 204 or response.status_code != 200:
        return None

    return CurrentlyPlaying.from_json(response.text, current_song)
