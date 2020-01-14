import os
import sys
from unittest.mock import patch

from ctr.cli import main


def test_main():
    pwd = os.getcwd()
    with open("in1", "w") as fout:
        print("h1\th2", file=fout)
        print("1\t2", file=fout)

    with open("in2", "w") as fout:
        print("h1\th2", file=fout)
        print("3\t4", file=fout)

    testargs = [os.path.join(pwd, "outfile"),
                os.path.join(pwd, "in1"),
                os.path.join(pwd, "in2")]
    with patch.object(sys, "argv", testargs):
        main(sys.argv)

        with open("outfile") as f:
            line = f.readline().strip()
            assert line == "h1\th2"
            line = f.readline().strip()
            assert line == "1\t2"
            line = f.readline().strip()
            assert line == "3\t4"

    for af in testargs:
        os.system("rm " + af)
