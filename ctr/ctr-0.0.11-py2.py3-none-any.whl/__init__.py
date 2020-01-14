__version__ = "__version__ = '0.0.11'"
from snakemake import shell


def concat(file_list, output_file):
    shell("head -1 {file_list[0]} > {output_file}")
    for afile in file_list:
        shell("tail -n +2 {afile} >> {output_file}")
