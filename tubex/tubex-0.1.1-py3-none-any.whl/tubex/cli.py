import click
import eyed3
import youtube_dl

from pathlib import Path
from functools import partial
from dataclasses import dataclass
from typing import Dict
from multiprocessing.dummy import Pool as ThreadPool


@dataclass(frozen=True)
class TagInfo:
    album: str = ""
    artist: str = ""


class TubeLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        click.echo(msg)


class Config:
    def __init__(self):
        self.outdir = None
        self.opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "logger": TubeLogger(),
            "restrictfilenames": True,
            "ignoreerrors": True,
        }


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--outdir")
@pass_config
def cli(config, outdir):
    if outdir is None:
        outdir = Path.cwd() / "tubex_out"
    config.outdir = str(Path(outdir))
    config.opts["outtmpl"] = f"{config.outdir}/%(title)s.%(ext)s"


def download_mp3(ydl: youtube_dl.YoutubeDL, tag_info: TagInfo, download_info: Dict):
    title = download_info["title"]
    pathname = Path(ydl.prepare_filename(download_info))
    filename = Path(pathname.name).stem
    mp3_pathname = f"{pathname.parent / filename}.mp3"
    if Path(mp3_pathname).exists():
        click.echo(f"Already exist: {pathname!s}")
        return
    download_url = download_info["webpage_url"]
    click.echo(f"Downloading {filename}...")
    ydl.download([download_url])
    click.echo(f"Tagging mp3 {filename}.mp3")
    song = eyed3.load(mp3_pathname).tag
    song.title = title
    song.album = tag_info.album
    song.artist = tag_info.artist
    song.save()


@cli.command()
@click.option("--album", default="", required=False)
@click.option("--artist", default="", required=False)
@click.argument("tube_url")
@pass_config
def download(config, tube_url, album, artist):
    click.echo(f"Output directory: {config.outdir}")
    with youtube_dl.YoutubeDL(config.opts) as ydl:
        click.echo(f"Extracting info...")
        download_info = ydl.extract_info(tube_url, download=False)
        if "entries" in download_info:
            download_infos = download_info["entries"]
        else:
            download_infos = [download_info]
        download_infos = [d for d in download_infos if d != None]
        tag_info = TagInfo(album=album, artist=artist)
        mp3_downloader = partial(download_mp3, ydl, tag_info)
        pool = ThreadPool(4)
        pool.map(mp3_downloader, download_infos)
        pool.close()
        pool.join()
        exit(0)
