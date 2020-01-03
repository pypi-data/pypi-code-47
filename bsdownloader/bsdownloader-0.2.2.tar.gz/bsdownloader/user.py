from bs4 import BeautifulSoup
import os
import pickle
import time


class User:
    def __init__(self, name: str, url: str, score: float, cache_folder: str):
        self.name = name
        self.url = url
        self.cache_file = os.path.join(cache_folder, f"{url.split('/')[-1]}.user")
        self.score = score

    def __repr__(self):
        return f"([{self.name}] {self.score})"

    def load_songs(self, page_count: int, pfun, stop_event):
        from .http_get import scraper_get
        from .gui import GuiIter

        # try load from cache
        if os.path.isfile(self.cache_file):
            with open(self.cache_file, mode="rb") as f:
                player_cache = pickle.load(f)
                if abs(player_cache["score"] - self.score) < 5.0 and player_cache["pages"] == page_count:
                    player_songs = player_cache["songs"]
                    print(f"{self.name} loaded from cache")
                    return player_songs

        # load from network
        player_songs = []
        for i in GuiIter(range(1, page_count), pfun):
            player_page = scraper_get(f"{self.url}&page={i}")
            bs = BeautifulSoup(player_page, "html.parser")
            table = bs.select("table tbody tr")
            for part in table:
                song_id = part.find("img")["src"].split("/")[-1].split(".")[0]
                song_pp = float(part.find(class_="ppValue").text.replace(",", ""))
                player_songs.append((song_id, song_pp))
            if stop_event.is_set():  # check stop
                return player_songs

        # save to cache
        player_cache = {"score": self.score, "songs": player_songs, "pages": page_count}
        with open(self.cache_file, mode="wb") as f:
            pickle.dump(player_cache, f, protocol=pickle.HIGHEST_PROTOCOL)

        return player_songs
