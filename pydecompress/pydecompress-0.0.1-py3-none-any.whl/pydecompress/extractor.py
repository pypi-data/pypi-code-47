from pathlib import Path
import tarfile, zipfile

class Extractor:

    @staticmethod
    def extract(filepath, destination):
        fpath = Path(filepath)
        destpath = Path(destination)
        fsuffix = fpath.suffix.lower()

        if fsuffix=='.tar':
            tarfile.open(fpath, 'r').extractall(destpath)
        elif fsuffix == '.tgz' or fsuffix == '.gz':
            tarfile.open(fpath, 'r:gz').extractall(destpath)
        elif fsuffix == '.bz2':
            tarfile.open(fpath, 'r:bz').extractall(destpath)
        elif fsuffix == '.xz':
            tarfile.open(fpath, 'r:xz').extractall(destpath)
        elif zipfile.is_zipfile(fpath):
            zipfile.ZipFile(fpath, 'r').extractall(destpath)
        else:
            print(f'Unsupported extension "{fsuffix}".')
            exit(1)

        return destpath