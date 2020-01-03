import json
import os
import zipfile
import pickle
import time


class Song:
    filename_dict = {ord(i): None for i in '<>:"\\/|?*'}

    def __init__(self, song_hash: str, cache_folder: str):
        self.song_hash = song_hash
        self.cache_file = os.path.join(cache_folder, f"{song_hash}.song")
        self.zip_file = os.path.join(cache_folder, "zips", f"{song_hash}.zip")
        self.key = ""
        self.song_name = ""
        self.filename = ""
        self.uploader = ""
        self.song_url = ""
        self.song_pp = 0.0
        self.update_count = 0.0
        self.is_parsed = False

    def __repr__(self):
        return f"{self.song_name} [{self.song_hash}]"

    def __lt__(self, other):
        return self.song_pp < other.song_pp

    def update_pp(self, new_pp: float) -> None:
        self.update_count += 1.0
        self.song_pp += new_pp

    def update_song(self) -> None:
        # calc average pp
        self.song_pp /= self.update_count

        # try loading from cache
        if os.path.isfile(self.cache_file):
            with open(self.cache_file, mode="rb") as f:
                song_data = pickle.load(f)
            self.key = song_data["key"]
            self.song_name = song_data["song_name"]
            self.uploader = song_data["uploader"]
            self.filename = f"{self.key} ({self.song_name})".translate(self.filename_dict)
            self.song_url = song_data["song_url"]
            self.is_parsed = True
            print(f"Song [{self.key}] loaded from cache")
            return

        # try requesting
        song_json = try_request(self.song_hash)
        # parse json
        try:
            song_doc = json.loads(song_json)["docs"][0]
            self.key = song_doc["key"]
            self.song_name = song_doc["name"]
            self.uploader = song_doc["uploader"]["username"]
            self.filename = f"{self.key} ({self.song_name})".translate(self.filename_dict)
            self.song_url = f"https://beatsaver.com{song_doc['directDownload']}"
        except IndexError:
            print(f"Song {self.song_hash} not found")
            return
        except Exception as e:
            print(f"Failed to parse song {self.song_hash} error: {e}")
            return

        # set parsed flag
        self.is_parsed = True

        # save to cache
        with open(self.cache_file, mode="wb") as f:
            song_data = {
                "key": self.key,
                "song_name": self.song_name,
                "uploader": self.uploader,
                "song_url": self.song_url,
            }
            pickle.dump(song_data, f, protocol=pickle.HIGHEST_PROTOCOL)

    def download(self, game_path: str, p_fun):
        from .http_get import download_file

        # song folder
        bs_songs_path = os.path.join(game_path, "Beat Saber_Data", "CustomLevels")
        song_path = os.path.join(bs_songs_path, self.filename)

        # check if song already here
        if os.path.isdir(song_path):
            return

        # download zip
        is_done = download_file(self.song_url, self.zip_file, p_fun)
        if not is_done:
            print(f"Filed to download {self.song_name}")
            return

        # unpack zip
        os.makedirs(song_path, exist_ok=True)
        with zipfile.ZipFile(self.zip_file, mode="r") as z_file:
            z_file.extractall(song_path)

        # delete zip
        os.remove(self.zip_file)


def try_request(song: str) -> bytes:
    from .http_get import simple_get

    for i in range(10):
        try:
            song_json = simple_get(f"https://beatsaver.com/api/search/text/0?q={song}")
            if i > 0:
                print("Request successful")
            break
        except:
            print(f"Request failed {i+1} of 10")
            time.sleep(5.0)
    else:
        raise Exception(f"Failed to request {song}")
    return song_json
