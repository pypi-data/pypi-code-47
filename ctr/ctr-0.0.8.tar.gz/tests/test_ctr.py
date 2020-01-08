import sys, os
from ctr.cli import main
from unittest.mock import patch

def test_main():
    with open('in1', 'w') as fout:
        print('h1\th2', file=fout)
        print('1\t2', file=fout)

    with open('in2', 'w') as fout:
        print('h1\th2', file=fout)
        print('3\t4', file=fout)

    testargs = ['ctr', 'outfile', 'in1', 'in2']
    with patch.object(sys, 'argv', testargs):
        main(sys.argv)

        with open('outfile') as f:
            line = f.readline()
            assert line=='h1\th2'
            line = f.readline()
            assert line== '1\t2'
            line = f.readline()
            assert line== '3\t4'
    os.system('rm in1 in2')
