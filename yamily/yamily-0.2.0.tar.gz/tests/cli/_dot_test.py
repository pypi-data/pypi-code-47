# yamify - define family trees in YAML
#
# Copyright (C) 2020 Fabian Peter Hammerle <fabian@hammerle.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
from unittest.mock import patch

from yamily._cli import _dot


@patch("sys.argv", ["", "persons"])
def test__dot_recurse_dir(capsys):
    _dot()
    out, err = capsys.readouterr()
    assert not err
    assert out == pathlib.Path("persons").joinpath("digraph.dot").read_text()


@patch("sys.argv", ["", "--comment", "some text", "persons/erika-mustermann.yml"])
def test__dot_comment(capsys):
    _dot()
    out, err = capsys.readouterr()
    assert not err
    expected_out = r"""digraph yamily {
	subgraph "cluster_erika-mustermann" {
		rank=same style=invisible
		"erika-mustermann" [label="Erika Mustermann\n*1957-08-12" shape=box]
	}
	subgraph cluster_comment {
		style=invisible
		comment [label="some text" shape=none]
	}
}
"""
    assert out == expected_out
