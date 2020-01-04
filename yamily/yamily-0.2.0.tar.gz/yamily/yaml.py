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

import datetime  # pylint: disable=unused-import; doctest

import yaml

from yamily import Person


class Loader(yaml.SafeLoader):

    # pylint: disable=too-many-ancestors

    """
    >>> alice_yaml = '''
    ... !person
    ... identifier: alice
    ... name: Alice Test
    ... birth_date: 1876-02-01
    ... death_date: 1976-01-02
    ... mother: mum
    ... father: dad
    ... '''
    >>> alice = yaml.load(alice_yaml, Loader=Loader)
    >>> alice
    Person(alice, Alice Test, *1876-02-01, †1976-01-02)
    >>> alice.mother
    Person(mum)
    >>> alice.father
    Person(dad)

    >>> alice_yaml = '''
    ... !person
    ... identifier: alice
    ... name: Alice Test
    ... birth_date: 1976-02-01
    ... mother: !person
    ...   identifier: mum
    ... father: !person
    ...   identifier: dad
    ...   name: Dad Test
    ... '''
    >>> alice = yaml.load(alice_yaml, Loader=Loader)
    >>> alice
    Person(alice, Alice Test, *1976-02-01)
    >>> alice.mother
    Person(mum)
    >>> alice.father
    Person(dad, Dad Test)
    """

    def __init__(self, stream):
        super().__init__(stream)
        self.add_constructor("!person", self._construct_person)

    @staticmethod
    def _construct_person(loader: "Loader", node: yaml.nodes.MappingNode) -> Person:
        (person_attrs,) = loader.construct_yaml_map(node)
        person = Person(person_attrs["identifier"])
        if "name" in person_attrs:
            person.name = person_attrs["name"]
        if "birth_date" in person_attrs:
            person.birth_date = person_attrs["birth_date"]
        if "death_date" in person_attrs:
            person.death_date = person_attrs["death_date"]
        if "mother" in person_attrs:
            if isinstance(person_attrs["mother"], Person):
                person.mother = person_attrs["mother"]
            else:
                person.mother = Person(person_attrs["mother"])
        if "father" in person_attrs:
            if isinstance(person_attrs["father"], Person):
                person.father = person_attrs["father"]
            else:
                person.father = Person(person_attrs["father"])
        return person


class Dumper(yaml.SafeDumper):

    """
    >>> p = Person('alice')
    >>> p.name = 'Alice'
    >>> p.birth_date = datetime.date(1976, 2, 1)
    >>> p.death_date = datetime.date(2043, 1, 17)
    >>> print(yaml.dump(p, Dumper=Dumper))
    !person
    birth_date: 1976-02-01
    death_date: 2043-01-17
    identifier: alice
    name: Alice
    <BLANKLINE>

    >>> p = Person('bob')
    >>> p.mother = Person('bob-mum')
    >>> p.father = Person('bob-father')
    >>> print(yaml.dump(p, Dumper=Dumper))
    !person
    father: !person
      identifier: bob-father
    identifier: bob
    mother: !person
      identifier: bob-mum
    <BLANKLINE>
    """

    # pylint: disable=too-many-ancestors

    def __init__(self, stream, **kwargs):
        super().__init__(stream, **kwargs)
        self.add_representer(Person, self._represent_person)

    @staticmethod
    def _represent_person(dumper: "_Dumper", person: Person) -> yaml.nodes.MappingNode:
        person_attrs = {"identifier": person.identifier}
        if person.name is not None:
            person_attrs["name"] = person.name
        if person.birth_date is not None:
            person_attrs["birth_date"] = person.birth_date
        if person.death_date is not None:
            person_attrs["death_date"] = person.death_date
        if person.mother is not None:
            person_attrs["mother"] = person.mother
        if person.father is not None:
            person_attrs["father"] = person.father
        return dumper.represent_mapping("!person", person_attrs)
