from setuptools import setup

setup(
	name = "soundloader",
	version = "0.1",
	description = "Downloads songs, albums or playlists through soundcloud link",
	license = "CC BY-NC-SA 4.0",
	author = "An0nimia",
	author_email = "An0nimia@protonmail.com",
	url = "https://github.com/An0nimia/soundloader",
	packages = ["soundloader"],
	install_requires = ["bs4", "mutagen", "requests", "tqdm"]
)