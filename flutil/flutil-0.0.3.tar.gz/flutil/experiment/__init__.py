import pickle
from pathlib import Path
from tqdm import tqdm
from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor as Executor
from itertools import product
from copy import deepcopy
import shutil
import pandas as pd
import logging
import nbconvert
import subprocess
import os
import sys
import warnings
from typing import Iterable, List
from numpy import nan  # To avoid errors with eval() when result is NaN


def run(nb: Path, base_conf: dict, out_dir: Path, extra_files: list = [],
        rm_out=False, n_jobs=None):
    """Run (in parallel) different experiments configured by `base_conf`.

    The notebook uses a config file to set certain parameters of an experiment.
    The config file passed here generally describes all the experiments that
    need to be done by listing all values of interest for certain parameters.
    This function creates pickle config files that contain a **single** value
    for each parameter. It creates a config file for all possible combinations
    of parameter values described by the general config file passed to this
    function. The config files will be put into separate subdirectories
    together with a copy of the notebook such that the notebook can be run
    as-is in that subdirectory. As such, each experiment can be easily
    reproduced by simply running the notebook in the respective subdirectory.

    :param Path nb: path to the notebook
    :param dict base_conf: the config dict configuring different settings for
    the experiments. The values of the configured variables should be in the
    third level of the dict. The first level describes a general namespace that
    variables belong to, the second level contains the variable names and the
    third level contains the variable values. If the value of a variable needs
    to be varied for the sake of experiment, that variable needs to be a list
    of the values of interest. A different experiment will be created for each
    possible combination of values for all the variables. If a single value is
    itself a list, it should be wrapped inside an extra list.
    :param Path out_dir: the parent directory of all the generated experiment
    results
    :param list extra_files: list of files that should be copied to experiment
    subdirectories in order for the config file to point to existing files
    :param bool rm_out: remove the output dir if it already exists
    :param int n_jobs: the number of jobs to run in parallel
    """
    sys.path.append(nb.parent.absolute())
    # Create python script from notebook
    py, _ = nbconvert.exporters.export(nbconvert.PythonExporter, str(nb))
    pyscript = (nb.parent / f'{nb.stem}_nbconv.py')
    pyscript.write_text(py)

    if out_dir.exists():
        if rm_out:
            shutil.rmtree(out_dir)
        else:
            raise ValueError(f'{str(out_dir)} is an existing directory. '
                             'Please remove or rename.')

    n_confs = sum(1 for _ in all_confs(base_conf))

    if n_jobs == 1:
        for i, conf in tqdm(enumerate(all_confs(base_conf)), total=n_confs):
            do_experiment(conf,
                          pyscript,
                          out_dir / ('trial_' + f'{i}'.rjust(len(f'{n_confs}'),
                                                             '0')),
                          extra_files)
    else:
        with Executor(max_workers=n_jobs) as pool:
            logging.info('Submitting processes...')
            futures = [pool.submit(
                do_experiment,
                conf, pyscript,
                out_dir / ('trial_' + f'{i}'.rjust(len(f'{n_confs}'), '0')),
                extra_files)
                       for i, conf in tqdm(enumerate(all_confs(base_conf)),
                                           total=n_confs)]

            logging.info('Waiting for processes to complete...')
            for f in tqdm(as_completed(futures), total=n_confs):
                pass


def do_experiment(conf: dict, pyscript: Path,
                  out_subdir: Path, extra_files: list):
    """Perform the experiment configured by a conf dict.

    The script copies a pickled version of the `conf` dict to the `out_subdir`
    and runs the `pyscript`.

    :param dict conf: the dict configuring the experiment
    :param Path pycript: the script that performs the experiment
    :paran Path out_subdir: the directory to run the experiment in
    :param list extra_files: list of files that should be copied to experiment
    subdirectories in order for the config file to point to existing files
    """
    if not out_subdir.exists():
        out_subdir.mkdir(parents=True)

    # Copy necessary files into subdir
    for f in extra_files:
        if f.is_dir():
            shutil.copytree(f, out_subdir / f.name, copy_function=os.link)
        else:
            os.link(f, out_subdir / f.name)

    # Copy the pickled config into subdir
    new_conf_pkl = out_subdir / 'conf.pkl'
    pickle.dump(conf, new_conf_pkl.open('wb'))

    # Copy the script into subdir
    new_pyscript = out_subdir / pyscript.name
    try:
        os.link(pyscript, new_pyscript)
    except OSError:
        shutil.copy(pyscript, new_pyscript)

    # Run the python script
    subprocess.run([sys.executable, new_pyscript.name],
                   cwd=out_subdir,
                   check=True)


def all_confs(base_conf: dict):
    """Generator that returns all versions of the config dict.

    :param dict base_conf: configuration dict where a lists in the third level
    describe a variable that should vary over different experiments.
    """
    changing_vals = {(k1, k2): v2
                     for k1, v1 in base_conf.items()
                     for k2, v2 in v1.items()
                     if type(v2) == list}

    for prod in product(*[changing_vals[k] for k in changing_vals.keys()]):
        conf_copy = deepcopy(base_conf)
        for j, (k1, k2) in enumerate(changing_vals.keys()):
            conf_copy[k1][k2] = prod[j]
        yield conf_copy


def get_experiment_df(confs: List[Path]):
    """Return a `DataFrame` that summarizes a set of config files.

    :param List[Path] confs: the JSON config files of an experiment set. These
    should have the same keys.
    """
    warnings.warn('JSON-based config files are deprecated. '
                  'Use a Python script that generates the base_conf '
                  'dict instead.',
                  DeprecationWarning)
    confs = [{'conf': {'file': str(c)},
              **pickle.load(c.open('rb'))} for c in confs]
    if len(confs) == 0:
        logging.error('The given list of confs is empty')
        return
    reform = [{(outerkey, innerkey): value
               for outerkey, innerdict in outerdict.items()
               for innerkey, value in innerdict.items()}
              for outerdict in confs]
    reform2 = {k: [innerdict[k] for innerdict in reform]
               for k in reform[0].keys()}
    df = pd.DataFrame(reform2)
    df.columns = ['_'.join(col[::1]).strip() for col in df.columns.values]
    return df


def get_results_df(result_dirs: Iterable, result_names: List[str]):
    """Return a `DataFrame` that contains the experiment results.

    :param Iterable result_dirs: an iterable with the paths containg results
    :param List[str] result_names: the file names (only the name, not the full
    path) that contain a result and may or may not be in each of the
    `result_dirs`
    """
    def read_contents(path):
        try:
            return eval(path.read_text())
        except NameError:
            return path.read_text()

    return pd.DataFrame([
        {
            'path': result_dir,
            **{str(result_name): read_contents(result_dir / result_name)
               for result_name in result_names
               if (result_dir / result_name).exists()}
         }
        for result_dir in result_dirs
    ])
