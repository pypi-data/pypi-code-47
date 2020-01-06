import pandas as pd 
import swifter # ==0.289
import os, sys, io
import subprocess as sp

# def called_function(row: pd.Series, command: str, TARGET_DIR: str):
#     if 'noisy' in row['full_path']:
#         os.system(f"mv {row['full_path']} {TARGET_DIR1}")
#     else:
#         os.system(f"mv {row['full_path']} {TARGET_DIR2}")

def execute(command: str, filt_cond: str):
    '''
    Runs a python `command` on filenames that pass -f 
    filt_cond: filter all files in in this directory and below by this expression.
    command: E.g.
    `dt py 'f"mv {x} real_A/ "' -f "real_A"`
    '''
    all_files = os.listdir('.')
    # from IPython.core.interactiveshell import InteractiveShell

    proc = str(sp.check_output('find $PWD/* -type f', shell=True))[2:] 
    # , capture_output=True, shell=True)
    df = pd.DataFrame(str(proc).split('\\n')[:-1] )
    df.columns = ['full_path']

    level_paths = df.full_path.str.split('/',expand=True)
    df = pd.concat([df, level_paths], axis=1)

    target_files = pd.Series(filter(lambda x: filt_cond in x, df.full_path.values))
    # mv_fcn = lambda x: os.system(f"mv {x} {command}/{x.replace('/','_')}")
    target_fcn = lambda x: os.system(eval(command))
    target_files.swifter.apply(lambda x: target_fcn(x))