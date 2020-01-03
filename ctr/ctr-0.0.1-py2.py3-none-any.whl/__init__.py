__version__ = '0.0.1'
from snakemake import shell

def concat(file_list, output_file):
     f = file_list[0]
     shell('head -1 {f} > {output_file}')
     for afile in file_list:
         shell('tail -n +2 {afile} >> {output_file}')
