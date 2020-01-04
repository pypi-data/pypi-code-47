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

from unittest.mock import patch

import pytest
from yamily._cli import _list


@patch("sys.argv", ["", "non/existing/file.yml"])
def test__read_non_existing():
    with pytest.raises(FileNotFoundError):
        _list()


@patch("sys.argv", ["", "persons/erika-mustermann.yml"])
def test__list_single_simple(capsys):
    _list()
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "- !person\n"
        "  birth_date: 1957-08-12\n"
        "  identifier: erika-mustermann\n"
        "  name: Erika Mustermann\n"
    )


@patch("sys.argv", ["", "persons/max-mustermann.yml"])
def test__list_single_parents(capsys):
    _list()
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "- &id001 !person\n"
        "  identifier: erika-mustermann\n"
        "- !person\n"
        "  birth_date: 1976-02-01\n"
        "  father: &id002 !person\n"
        "    identifier: thomas-mustermann\n"
        "  identifier: max-mustermann\n"
        "  mother: *id001\n"
        "  name: Max Mustermann\n"
        "- *id002\n"
    )


@patch("sys.argv", ["", "persons/max-mustermann.yml", "persons/erika-mustermann.yml"])
def test__list_multiple(capsys):
    _list()
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "- &id001 !person\n"
        "  birth_date: 1957-08-12\n"
        "  identifier: erika-mustermann\n"
        "  name: Erika Mustermann\n"
        "- !person\n"
        "  birth_date: 1976-02-01\n"
        "  father: &id002 !person\n"
        "    identifier: thomas-mustermann\n"
        "  identifier: max-mustermann\n"
        "  mother: *id001\n"
        "  name: Max Mustermann\n"
        "- *id002\n"
    )


@patch("sys.argv", ["", "persons"])
def test__list_recurse_dir(capsys):
    _list()
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "- !person\n"
        "  father: &id001 !person\n"
        "    identifier: alice-father\n"
        "    mother: &id002 !person\n"
        "      identifier: alice-grandmother\n"
        "      name: Grandma Test\n"
        "  identifier: alice\n"
        "  mother: &id003 !person\n"
        "    identifier: alice-mother\n"
        "    name: Mum Test\n"
        "  name: Alice Test\n"
        "- *id001\n"
        "- *id002\n"
        "- *id003\n"
        "- &id004 !person\n"
        "  birth_date: 1957-08-12\n"
        "  identifier: erika-mustermann\n"
        "  name: Erika Mustermann\n"
        "- !person\n"
        "  birth_date: 1976-02-01\n"
        "  father: &id005 !person\n"
        "    identifier: thomas-mustermann\n"
        "  identifier: max-mustermann\n"
        "  mother: *id004\n"
        "  name: Max Mustermann\n"
        "- *id005\n"
    )
