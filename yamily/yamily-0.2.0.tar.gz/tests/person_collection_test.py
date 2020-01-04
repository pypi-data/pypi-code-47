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

import datetime

from yamily import Person, PersonCollection


def test_add_person_again():
    collection = PersonCollection()
    alice1 = Person("alice")
    alice1.name = "Alice"
    collection.add_person(alice1)
    alice2 = Person("alice")
    alice2.birth_date = datetime.date(2019, 12, 23)
    alice2.death_date = datetime.date(1919, 12, 23)
    collection.add_person(alice2)
    assert len(list(collection)) == 1
    assert collection["alice"].name == "Alice"
    assert collection["alice"].birth_date == datetime.date(2019, 12, 23)
    assert collection["alice"].death_date == datetime.date(1919, 12, 23)


def test_add_person_unknown_parents():
    collection = PersonCollection()
    alice = Person("alice")
    alice.name = "Alice"
    alice.birth_date = datetime.date(2019, 12, 23)
    alice.mother = Person("mother")
    alice.father = Person("father")
    collection.add_person(alice)
    assert collection["alice"].birth_date == datetime.date(2019, 12, 23)
    assert collection["alice"] is alice
    assert collection["mother"] is alice.mother
    assert collection["father"] is alice.father


def test_add_person_known_parents():
    collection = PersonCollection()
    mother = Person("mother")
    mother.name = "Mum"
    collection.add_person(mother)
    collection.add_person(Person("father"))
    alice = Person("alice")
    alice.name = "Alice"
    alice.birth_date = datetime.date(2019, 12, 23)
    alice.mother = Person("mother")
    alice.father = Person("father")
    collection.add_person(alice)
    assert collection["alice"].birth_date == datetime.date(2019, 12, 23)
    assert collection["alice"] is alice
    assert collection["mother"] is mother
    assert collection["mother"] is alice.mother
    assert collection["alice"].mother.name == "Mum"
    assert collection["father"] is alice.father


def test_add_person_later_parents():
    collection = PersonCollection()
    alice = Person("alice")
    alice.name = "Alice"
    alice.birth_date = datetime.date(2019, 12, 23)
    alice.mother = Person("mother")
    alice.father = Person("father")
    collection.add_person(alice)
    assert collection["mother"].name is None
    assert collection["father"].name is None
    mother = Person("mother")
    mother.name = "Mum"
    stored_mother = collection.add_person(mother)
    father = Person("father")
    father.name = "Dad"
    stored_father = collection.add_person(father)
    assert collection["alice"].birth_date == datetime.date(2019, 12, 23)
    assert collection["alice"] is alice
    assert collection["mother"] is alice.mother
    assert collection["mother"] is stored_mother
    assert collection["alice"].mother.name == "Mum"
    assert collection["father"] is alice.father
    assert collection["father"] is stored_father
    assert collection["alice"].father.name == "Dad"
