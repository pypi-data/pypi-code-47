from bs4 import BeautifulSoup
from typing import List
import json
import os
import threading

from .http_get import scraper_get
from .user import User
from .song import Song
from .image import b64image
from .config import get_folder


def clear_cache():
    import shutil

    cache_folder = os.path.join(get_folder(), "cache")
    shutil.rmtree(cache_folder)


class WorkerThread(threading.Thread):
    def __init__(self, gui, config):
        threading.Thread.__init__(self)
        self.gui = gui
        self.config = config
        self._stop_event = threading.Event()
        self.working = False

    def stop(self):
        self.working = False
        self._stop_event.set()

    def run(self) -> None:
        from .gui import GuiIter

        self.working = True
        self._stop_event.clear()
        # create cache & zips folders
        cache_folder = os.path.join(get_folder(), "cache")
        os.makedirs(os.path.join(cache_folder, "zips"), exist_ok=True)

        # get main page
        self.gui.set_label("Loading main page...")
        main_page = scraper_get("https://scoresaber.com/global")

        # parse main page
        bs = BeautifulSoup(main_page, "html.parser")
        table = bs.select("table tbody tr")

        # make player list
        players = []
        # process main page
        for part in table:
            player = part.find(class_="player")
            score = float(part.find(class_="ppValue").text.replace(",", ""))
            name = player.span.text
            p_url = "https://scoresaber.com" + player.a["href"]
            players.append(User(name, p_url, score, cache_folder))

        if len(players) != 50:
            raise Exception("Failed to parse player list")

        # make song dict
        songs = dict()

        # process players songs
        page_count = self.config.count // 8 + 1
        for player in GuiIter(players, self.gui.set_progress1, p_from=0, p_to=33):
            self.gui.set_label(f"Processing player: {player.name}...")
            p_songs = player.load_songs(page_count, self.gui.set_progress2, self._stop_event)
            for s_hash, pp in p_songs:
                if s_hash not in songs:
                    songs[s_hash] = Song(s_hash, cache_folder)
                songs[s_hash].update_pp(pp)
            if self._stop_event.is_set():  # check stop
                return
        print(f"Total {len(songs)} songs")

        # get song download urls
        self.gui.set_label(f"Getting song info...")
        self.gui.set_progress2(100)
        for s_hash in GuiIter(songs, self.gui.set_progress1, p_from=33, p_to=66):
            songs[s_hash].update_song()
            self.gui.set_label(f"Getting song info: {songs[s_hash].song_name}...")
            if self._stop_event.is_set():  # check stop
                return

        # filter song dict
        songs = list(filter(lambda s: s.is_parsed, songs.values()))[: self.config.count]
        print(f"After filtering {len(songs)} songs")

        # download songs
        for song in GuiIter(songs, self.gui.set_progress1, p_from=66, p_to=99):
            self.gui.set_label(f"Downloading {song.song_name}...")
            song.download(self.config.path, self.gui.set_progress2)
            if self._stop_event.is_set():  # check stop
                return

        # save playlist
        self.gui.set_label(f"Creating playlist...")
        playlist_folder = os.path.join(self.config.path, "Playlists")
        os.makedirs(playlist_folder, exist_ok=True)
        playlist_file = os.path.join(playlist_folder, "top.bplist")
        playlist = make_playlist(songs)
        with open(playlist_file, "w") as f:
            f.write(playlist)

        self.gui.set_progress1(100)
        self.gui.set_label(f"Done!")
        self.working = False
        self.gui.on_done()


def make_playlist(songs: List[Song]) -> str:
    # sort songs - hi_pp -> low_pp
    songs.sort(reverse=True)
    # make playlist
    playlist = {
        "playlistTitle": "Top PP songs",
        "playlistAuthor": "Norne",
        "image": b64image(),
        "songs": [{"key": s.key, "hash": s.song_hash, "songName": s.song_name, "uploader": s.uploader} for s in songs],
    }
    return json.dumps(playlist)
