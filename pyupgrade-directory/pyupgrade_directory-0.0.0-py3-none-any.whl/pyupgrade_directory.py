import os
import subprocess
import sys

def _run(paths, args):
    ret = 0
    basecmd = (sys.executable, '-mpyupgrade', *args)
    baselen = len(' '.join(basecmd))
    curlen = baselen
    filenames = []

    def _do_run():
        nonlocal curlen, filenames, ret
        ret |= subprocess.call((*basecmd, *filenames))
        filenames = []
        curlen = baselen

    for path in paths:
        for root, _, fnames in os.walk(path):
            for fname in fnames:
                if fname.endswith('.py'):
                    newfile = os.path.join(root, fname)
                    filenames.append(newfile)
                    curlen += len(newfile) + 1
                    if curlen > 20000:
                        _do_run()
    if filenames:
        _do_run()
    return ret

def main():
    paths, args = [], []
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            paths.append(arg)
        else:
            args.append(arg)
    return _run(paths, args)

if __name__ == '__main__':
    exit(main())
