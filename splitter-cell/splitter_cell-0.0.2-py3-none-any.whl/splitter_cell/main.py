import re
import os
import click
import m3u8
from operator import itemgetter
from pathlib import Path
from crayons import green, red
from baranomi import Baranomi
import json
import faster_than_requests as requests




class FileIOHandling(object):
    def __init__(self, folder) -> None:
        _folder = self._check_is_absolute(folder)
        self.given_folder = Path(_folder)
        self.given_folder_absolute = self.given_folder.absolute()
        self.is_exist = self.given_folder_absolute.exists()

        self._glob = ""
        self._globs = []
        self._download_folder = Path().cwd()
        self._output_folder = Path().cwd()

    @property
    def glob(self):
        return self._glob
    
    @glob.setter
    def glob(self, _glob):
        self._glob = _glob

    @property
    def exists(self):
        return self.is_exist
    
    @property
    def glob_paths(self):
        return self._globs

    @glob_paths.setter
    def glob_paths(self, _globs):
        self._globs = _globs
    
    @property
    def sorted_globs(self):
        file_dict_arr = self.sort_by_number_dicts()
        if len(file_dict_arr) == 0:
            return []
        file_list = list(map(lambda x:  f"{x.get('parent', '.')}/{x.get('file_name')}", sorted(file_dict_arr, key=itemgetter('index'))))
        return file_list

    
    @property
    def download_folder(self):
        return self._download_folder

    @download_folder.setter
    def download_folder(self, down_folder:str):
        self._download_folder = Path(f"{down_folder}").mkdir(parents=True, exist_ok=True)
    
    @property
    def output_folder(self):
        return self._output_folder

    @output_folder.setter
    def output_folder(self, _output_folder):
        self._output_folder = Path(f"{_output_folder}").mkdir(parents=True, exist_ok=True)


    def _check_is_absolute(self, _folder):
        """ Checks if the folder is absolute or not. """
        if os.path.isabs(_folder):
            return _folder

        current_path = Path.cwd() / f'{_folder}'
        return current_path

    def search_glob(self):
        if self.exists == True:
            click.echo(green("File path exists"))
            current_glob_paths = list(self.given_folder_absolute.glob(self.glob))
            abs_glob_paths = [x.absolute() for x in current_glob_paths]
            self.glob_paths = abs_glob_paths
            return self.glob_paths
        return self.glob_paths
    

    def sort_by_number_dicts(self):
        file_dict_arr = []
        if len(self.glob_paths) == 0:
            return file_dict_arr
        for file in self.glob_paths:
            fname = file.name
            numbers = [int(s) for s in re.findall(r'\b\d+\b', fname)]
            if len(numbers) > 0:
                item = {
                    "file_name": fname,
                    "index": numbers[0],
                    "parent": file.parents[0]
                }
                file_dict_arr.append(item)
        return file_dict_arr
    

    def safe_save(self, output_name):
        file_list = self.sorted_globs
        if len(file_list) > 0:
            (
                Baranomi()
                .load_file_list_as_bytes(file_list)
                .join()
                .save(output_name)
            )

@click.group()
@click.option(
    '--download-folder', '-d',
    default='splitter/down',
    help='Set Download Folder',
)
@click.option(
    '--output-folder', '-o',
    default='splitter/out',
    help='Set where all outputs go.',
)
@click.option(
    '--config-file', '-c',
    type=click.Path(),
    default='~/.splitter.cfg',
    help='Set where all outputs go.',
)
@click.pass_context 
def main(ctx, download_folder, output_folder, config_file):

    filename = os.path.expanduser(config_file)
    if (not download_folder or not output_folder) and os.path.exists(filename):
        with open(filename) as cfg:
            ctx.obj = json.loads(cfg.read())
    else:
        ctx.obj = {
            "down_folder": download_folder,
            "out_folder": output_folder,
            'config_file': filename
        }


    Path(ctx.obj['down_folder']).mkdir(parents=True, exist_ok=True)
    Path(ctx.obj['out_folder']).mkdir(parents=True, exist_ok=True)

@main.command()
@click.pass_context
def config(ctx):
    """
    Store configuration values in a file, e.g. the API key for OpenWeatherMap.
    """
    config_file = ctx.obj['config_file']

    down_folder = click.prompt(
        "Please enter your download folder",
        default=ctx.obj.get('down_folder', '')
    )


    out_folder = click.prompt(
        "Please enter your download folder",
        default=ctx.obj.get('out_folder', '')
    )


    excellent = {
        "down_folder": down_folder,
        "out_folder": out_folder
    }


    with open(config_file, 'w') as cfg:
        cfg.write(json.dumps(excellent))

    down_path = Path(excellent['down_folder'])
    out_path = Path(excellent['out_folder'])
    down_path.mkdir(parents=True, exist_ok=True)
    out_path.mkdir(parents=True, exist_ok=True)


@main.command()
@click.option('--sub_folder', '-s', prompt='Which subfolder?', default="", help='Explain which subfolder you want to add')
@click.option('--url', '-u', prompt='Which url?', help='Add a url to download from')
@click.pass_context
def download(ctx, sub_folder:str, url:str):
    sub = (Path(ctx.obj['down_folder']) / sub_folder)
    sub.mkdir(parents=True, exist_ok=True)
    derp = requests.post(url, json.dumps({}))
    print(derp)
    # click.echo(sub)

@main.command()
@click.option('--folder', prompt='Which folder?', default="", help='The person to greet.')
@click.option('--glob', prompt='What glob command do you plan on using?', help='The files youre trying to join')
@click.option('--output', prompt='What output file name', help="The file output name")
def hello(folder, glob, output):
    """Get a folder we want to search in, then get the glob necessary to find all of the files we want to merge together."""
    file_io_handler = FileIOHandling(folder)
    file_io_handler.glob = glob
    file_io_handler.search_glob()
    file_io_handler.safe_save(output)

@main.command()
@click.option('--sub-folder', '-s', prompt='Which subfolder?', default="", help='Explain which subfolder you want to add')
@click.option('--file-name', '-f', prompt='Give a file name', help='Explain which subfolder you want to add')
@click.pass_context
def load(ctx, sub_folder:str, file_name:str):
    sub = (Path(ctx.obj['out_folder']) / sub_folder)

    _file = (sub / file_name)
    if not _file.exists():
        click.echo(red("File does not exist"))
    
    suffix = _file.suffixes
    joined_suffix = "".join(suffix)
    if joined_suffix == ".m3u8":
        opened = _file.open(mode="r")
        information = opened.read()
        m3u8_obj = m3u8.loads(information)
        for segment in m3u8_obj.segments:
            click.echo(segment)
    else:
        pass


if __name__ == '__main__':
    main()