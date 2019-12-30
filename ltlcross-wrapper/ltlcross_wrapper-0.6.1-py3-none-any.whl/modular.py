# Copyright (c) 2019 Fanda Blahoudek
# This file is part of ltlcross_wrapper distributed under MIT License.

import csv
import math
import os
import os.path
import sys

from multiprocessing import Pool
import subprocess as sp

from ltlcross_wrapper.runner import LtlcrossRunner


def _renumber_formula(line, increase):
    """Increase formula id on the given ltlcross-log line

    Parameters
    ==========
    `line` — line from ltlcross log with formula to be translated.
    `increase` — number of which we should increase the formula id
    """
    splitted = line.split(":")
    splitted[1] = str(int(splitted[1]) + increase)
    return ":".join(splitted)


def id_to_str(i, pad_length=2):
    return str(i).zfill(pad_length)


class Modulizer():
    """Split a big ltlcross task into smaller ones that can
    be executed separately, run them in parallel, and merge
    the results into one final `.csv` file with results and
    one `.log` file.

    Expected use:
    >>> m = Modulizer(parameters)
    >>> m.run()

    A computation that was interupted can be resumed by:
    >>> m.resume()

    Delete previous results (final and intermediate), and run
    again, by:
    >>> m.recompute()

    Parameters
    ==========
     * `tools` : dict — dictionary with tools config passed to LtlcrossRunner
     * `formula_file` : str — path to file to split
     * `name` : name of the job
                used for default names of output files and tmp_dir
                'modular' by defualt.
     * `chunk_size` : int — number of formulas in one chunk (default 2)
     * `tmp_dir` : str — directory to perform (or continue) computations
     * `processes` : int — # of processes for running ltlcross in parallel
                     default 4
     * final output files (all are `{name}.ext` by default):
       - out_res_file (`.csv`, final results)
       - out_log_file (`.log`, merged logs)
       - out_bogus_file (`_bogus.ltl`, merged bogus formulae)
    """

    def __init__(self, tools, formula_file,
                 chunk_size=2, processes=4,
                 name="modular", tmp_dir=None,
                 out_res_file=None, out_log_file=None, out_bogus_file=None):
        self.tools = tools
        self.formula_file = formula_file

        self.chunk_size = chunk_size
        self.processes = processes

        # Set the tmp dirs
        self.tmp_dir = f"{name}.parts" if tmp_dir is None else tmp_dir
        if not os.path.isdir(self.tmp_dir):
            os.mkdir(self.tmp_dir)

        self.prefix = f"{self.tmp_dir}/{name}"

        # Set output files names
        self.out_res_file = f"{name}.csv" if \
            out_res_file is None else out_res_file
        self.out_log_file = f"{name}.log" if \
            out_log_file is None else out_log_file
        self.out_bogus_file = f"{name}_bogus.ltl" if \
            out_bogus_file is None else out_bogus_file

        # Get the count of chunks
        length = sum(1 for line in open(self.formula_file))
        self.chunks = math.ceil(length / self.chunk_size)

    def get_res_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.csv"

    def get_ltl_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.ltl"

    def get_log_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.log"

    def split_task(self):
        """Split the formulas for the given task into smaller files,
        each containing `chunk_size` formulas.

        The last part can contain less formulas.
        """
        in_f = open(self.formula_file, "r")

        ## Create all files but last (which can be shorter) ##
        for i in range(self.chunks - 1):
            out_f = open(self.get_ltl_name(i), "w")
            for j in range(self.chunk_size):
                line = in_f.readline()
                print(line, file=out_f, end='')
            out_f.close()

        ## Create the last file ##
        i = self.chunks - 1  # We start with 0
        out_f = open(self.get_ltl_name(i), "w")
        for line in in_f:
            print(line, file=out_f, end='')
        out_f.close()

        in_f.close()

    def run_part(self, part):
        """Run part number `part`"""
        res_file = self.get_res_name(part)
        form_file = self.get_ltl_name(part)
        r = LtlcrossRunner(self.tools, form_file, res_file)
        r.run_ltlcross()

    def merge_parts(self):
        """Use merger to merge intermediate results into final ones."""
        m = Merger(self.prefix, self.prefix,
                   self.chunks, self.chunk_size,
                   self.out_res_file, self.out_log_file,
                   self.out_bogus_file)
        m.merge_files()

    def run(self, parts=None, processes=None):
        if processes is None:
            processes=self.processes

        if parts is None:
            self.split_task()
            parts = range(self.chunks)

        with Pool(processes=processes) as pool:
            pool.map(self.run_part, parts, 1)

        self.merge_parts()

    def resume(self, **kwargs):
        """Resume previously started and interrupted computation.

        Detect which jobs (based on files in `tmp_dir`) need to be
        computed and runs the computation for them in parallel.

        Does nothing if everything is finished.

        **kwargs are given to subsequent call to `run`.
        """
        if os.path.isfile(self.out_res_file):
            return

        to_compute = [part for part in range(self.chunks) \
                      if not os.path.isfile(self.get_res_name(part))]

        print(f"Parts to finish:\n\t{to_compute}")

        self.run(parts=to_compute, **kwargs)

    def recompute(self, **kwargs):
        """Delete previous final and partial results and run again.

        **kwargs are given to subsequent call to `run`.
        """
        print("Deleting previous results & partial files")

        # Delete previous final results if they exist
        for f in [self.out_res_file, self.out_log_file, self.out_bogus_file]:
            if os.path.isfile(f):
                os.remove(f)

        # Delete the content of the tmp_dir
        for f in os.listdir(self.tmp_dir):
            os.remove(f"{self.tmp_dir}/{f}")

        self.run(**kwargs)


class Merger():
    """Merge `.csv`, `.log`, and `_bogus.ltl` files from partial runs
    of ltlcross into aggregated files.

    Expects the files to be named:
      * `{prefix}-ii.csv`, and
      * `{prefix}-ii.log`
      * `{prefix}-ii_bogus.ltl`

    Parameters:
    ===========
    * `prefix` — path prefix (including directories) to files to merge

    * `formula_prefix`: — path prefix to files with formulas used to compute
    intermediate results (needed to correct reunbering of formulas in `.log`
    files).

    * `chunks` — number of chunks to merge

    * `chunk_size` — number if formulas in one chunk

    * `csv_output` — path for the final results

      - will be overwritten by calling `merge_res_files()` and `merge_files()`
      - `{prefix}.csv` by default
    * `log_output` — path for the final results

      - will be overwritten by calling `merge_log_files()` and `merge_files()`
      - `{prefix}.log` by default

    * `bogus_output` — path for the final bogus-formulas file

      - will be overwritten by calling `merge_bogus()` and `merge_files()`
      - `{prefix}_bogus.ltl` by default
    """

    def __init__(self, prefix, formula_prefix,
                 chunks, chunk_size,
                 csv_output=None, log_output=None, bogus_output=None):
        self.prefix = prefix
        self.formula_prefix = formula_prefix
        self.chunks = chunks
        self.chunk_size = chunk_size

        if csv_output is None:
            self.output = f"{prefix}.csv"
        else:
            self.output = csv_output
        if log_output is None:
            self.log_output = f"{prefix}.log"
        else:
            self.log_output = log_output
        if bogus_output is None:
            self.bogus_output = f"{prefix}_bogus.ltl"
        else:
            self.bogus_output = bogus_output

        self.writer = None
        self.log_file_h = None
        csv.field_size_limit(sys.maxsize)

    ### CSV files ###
    def _print_res_header(self):
        """Write header of csv files based on given prefix.

        Uses the writer to print headers that are taken from
        the first file with given prefix:
        ```
        prefix-00.csv
        ```

        Parameters
        ==========
        `writer` : csv.writer to use
        `prefix` : str prefix of filenames to be merged
        """
        input_f = f"{self.prefix}-00.csv"
        reader = csv.reader(open(input_f, "r"))
        header_row = reader.__next__()
        self.writer.writerow(header_row)

    def _append_res_part(self, i):
        """Append rows from file `prefix-ii.csv` to writer.

        By `ii` we mean i padded to have two digits.
        """
        i_s = id_to_str(i)
        input_f = f"{self.prefix}-{i_s}.csv"
        reader = csv.reader(open(input_f, "r"))
        reader.__next__()
        self.writer.writerows(reader)

    def merge_res_files(self):
        """Merge files `prefix-00.csv` ... `prefix-chunks.csv`
        into file `prefix.csv`.
        """
        f = open(self.output, "w")
        self.writer = csv.writer(f)

        self._print_res_header()
        for i in range(self.chunks):
            self._append_res_part(i)

        f.close()

    ### LOGS ###
    def _append_log_part(self, i):
        """Apend one partial `.log` file into final log.

        Renumbers the formula ids accordingly.
        """
        increase = i * self.chunk_size
        i_s = id_to_str(i)
        formula_file = f"{self.formula_prefix}-{i_s}.ltl"
        f = open(f"{self.prefix}-{i_s}.log", "r")

        # Skip 3 lines with common info
        for i in range(3):
            f.__next__()

        for line in f:
            if line.startswith(formula_file):
                line = _renumber_formula(line, increase)
            print(line, end="", file=self.log_file_h)

        f.close()

    def merge_log_files(self):
        """Merge files `prefix-00.log` ... `prefix-chunks.log`
        into file `prefix.log`.
        """
        self.log_file_h = open(self.log_output, "w")

        # copy the first 3 lines from the 1st log file
        f = open(f"{self.prefix}-00.log", "r")
        for i in range(3):
            line = f.readline()
            self.log_file_h.writelines(line)
        f.close()

        # apppend the rest
        for i in range(self.chunks):
            self._append_log_part(i)
        self.log_file_h.close()

    ### bogus formulas ###
    def merge_bogus(self):
        """Merge files `prefix-00_bogus.ltl` ...
        into file `prefix_bogus.ltl`.
        """
        files = [f"{self.prefix}-{id_to_str(i)}_bogus.ltl" \
                 for i in range(self.chunks)]
        f_h = open(self.bogus_output, "w")
        sp.call(["cat"] + files, stdout=f_h)
        f_h.close()

    def merge_files(self):
        """Merge result, log, and bogus-formulas files."""
        self.merge_res_files()
        self.merge_log_files()
        self.merge_bogus()

    def delete_parts(self, types=[".log",".csv","_bogus.ltl"]):
        """Delete the partial results, log, and ltl files

        `types` — list of files to delete
        """
        for t in types:
            for i in range(self.chunks):
                i_s = id_to_str(i)
                input_f = f"{self.prefix}-{i_s}{t}"
                os.remove(input_f)