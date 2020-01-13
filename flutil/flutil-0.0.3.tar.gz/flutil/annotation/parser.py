from typing import List
from . import Annotation
import os.path


class Parser:
    @staticmethod
    def parse_single(annot_file: str) -> List[Annotation]:
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        raise NotImplementedError

    @classmethod
    def parse(cls, annot_files: List[str]) -> List[List[Annotation]]:
        """Return lists of Annotation objects (a list per annotation file).

        :param List[str] annot_files: the paths of the annotation files
        :returns: a list per annotation file
        :rtype: List[List[Annotation]]
        """
        return [cls.parse_single(f) for f in annot_files]

    @staticmethod
    def annots_to_file_contents(annotations: List[Annotation]) -> str:
        """Return the file contents that correspond to a list of annotations.

        :param List[Annotation] annotations: the annotations
        :returns: the file contents that correspond to a list of annotations.
        """
        raise NotImplementedError

    @classmethod
    def write_single(cls, annotations: List[Annotation], out_file: str,
                     overwrite=False):
        """Write annotations to the given file.

        :param List[Annotation] annotations: the annotations to write
        :param str out_file: the destination file
        :param bool overwrite: if True, overwrite a file if it exists. If
        False, raise a ``ValueError`` if an existing file is encountered.
        Default: False.
        """
        if not overwrite and os.path.exists(out_file):
            raise ValueError(f'File exists: {out_file}')

        with open(out_file, 'w') as f:
            f.write(cls.annots_to_file_contents(annotations))

    @classmethod
    def write(cls, annotations: List[List[Annotation]], out_files: List[str],
              overwrite=False):
        """Write annotations to the given files.

        :param List[Annotation] annotations: the annotations to write
        :param str out_file: the destination files, in the same order as the
        annotations
        :param bool overwrite: if True, overwrite a file if it exists. If
        False, raise a ``ValueError`` if an existing file is encountered.
        Default: False.
        """
        for (out_file, file_annots) in zip(out_files, annotations):
            cls.write_single(file_annots, out_file, overwrite)
