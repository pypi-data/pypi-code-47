import shlex, subprocess


def to_cli(instruction, pipe=True):
    """
    Execute the 'instruction' in a shell. If 'pipe' is True, the results of this
    instruction is returned in the 'proc' object (proc.stdout or proc.stderr
    allows the user to access results). If 'pipe' is False, the result is printed
    on the current CLI.
    """
    instruction_ = ' '.join(shlex.split(instruction))
    if pipe:
        proc = subprocess.run(instruction_, stdout=subprocess.PIPE,
         stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    else:
        proc = subprocess.run(instruction_, universal_newlines=True, shell=True)
    return proc
