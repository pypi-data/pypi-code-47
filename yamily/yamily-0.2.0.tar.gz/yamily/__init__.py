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

import collections
import datetime
import typing


class Person:

    """
    >>> alice = Person('alice')
    >>> alice.name = 'Alice Test'
    >>> alice.birth_date = datetime.date(1919, 12, 23)
    >>> alice.death_date = datetime.date(2019, 11, 1)
    >>> alice
    Person(alice, Alice Test, *1919-12-23, †2019-11-01)
    >>> str(alice)
    'Alice Test (*1919-12-23, †2019-11-01)'

    >>> bob = Person('bob')
    >>> bob.name = 'Bob Test'
    >>> alice.father = bob
    """

    def __init__(self, identifier: str):
        self.__identifier: str = identifier
        self.name: typing.Optional[str] = None
        self.birth_date: typing.Optional[datetime.date] = None
        self.death_date: typing.Optional[datetime.date] = None
        self.mother: typing.Optional["Person"] = None
        self.father: typing.Optional["Person"] = None

    @property
    def identifier(self) -> str:
        return self.__identifier

    def __hash__(self) -> int:
        return hash(self.__identifier)

    def __repr__(self) -> str:
        """
        >>> p = Person("max-mustermann")
        >>> repr(p)
        'Person(max-mustermann)'
        >>> p.name = "Hr. Mustermann"
        >>> repr(p)
        'Person(max-mustermann, Hr. Mustermann)'
        >>> p.name = "Max Mustermann"
        >>> repr(p)
        'Person(max-mustermann, Max Mustermann)'
        >>> p.birth_date = datetime.date(1876, 2, 1)
        >>> p.death_date = datetime.date(1976, 2, 1)
        >>> repr(p)
        'Person(max-mustermann, Max Mustermann, *1876-02-01, †1976-02-01)'
        """
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                filter(
                    None,
                    (
                        self.identifier,
                        self.name,
                        "*" + self.birth_date.isoformat()
                        if self.birth_date is not None
                        else None,
                        "†" + self.death_date.isoformat()
                        if self.death_date is not None
                        else None,
                    ),
                )
            ),
        )

    def __str__(self) -> str:
        """
        >>> p = Person("max-mustermann")
        >>> p.name = "Max Mustermann"
        >>> str(p)
        'Max Mustermann'
        >>> p.birth_date = datetime.date(1876, 2, 1)
        >>> str(p)
        'Max Mustermann (*1876-02-01)'
        >>> p.death_date = datetime.date(1976, 1, 2)
        >>> str(p)
        'Max Mustermann (*1876-02-01, †1976-01-02)'
        """
        attrs = []
        if self.birth_date is not None:
            attrs.append("*{}".format(self.birth_date.isoformat()))
        if self.death_date is not None:
            attrs.append("†{}".format(self.death_date.isoformat()))
        return (self.name or "unnamed") + (
            " ({})".format(", ".join(attrs)) if attrs else ""
        )

    def __eq__(self, other: "Person") -> bool:
        """
        >>> maxl = Person("max")
        >>> maxl.name = "Max Mustermann"
        >>> maxl == Person("max")
        True
        >>> erika = Person("erika")
        >>> erika.name = "Max Mustermann"
        >>> maxl == erika
        False
        """
        return self.identifier == other.identifier

    def merge(self, person: "Person") -> None:
        """
        >>> p1 = Person("max")
        >>> p1.name = "Max Mustermann"
        >>> str(p1)
        'Max Mustermann'
        >>> p2 = Person("max2")
        >>> p2.birth_date = datetime.date(1876, 2, 1)
        >>> p2.death_date = datetime.date(1976, 2, 1)
        >>> p2.mother = Person("mother")
        >>> p2.father = Person("father")
        >>> str(p2)
        'unnamed (*1876-02-01, †1976-02-01)'

        add attributes of p2 to p1:
        >>> p1.merge(p2)
        >>> str(p1)
        'Max Mustermann (*1876-02-01, †1976-02-01)'
        >>> p1.mother, p1.father
        (Person(mother), Person(father))

        p2 is unchanged:
        >>> str(p2)
        'unnamed (*1876-02-01, †1976-02-01)'
        """
        for attr in ["name", "birth_date", "death_date", "mother", "father"]:
            if getattr(person, attr) is not None:
                setattr(self, attr, getattr(person, attr))

    @property
    def parents(self) -> typing.Tuple["Person"]:
        """
        >>> p = Person("max")
        >>> p.parents
        ()
        >>> p.mother = Person("mum")
        >>> p.parents
        (Person(mum),)
        >>> p.father = Person("dad")
        >>> p.parents
        (Person(mum), Person(dad))
        >>> p.mother = None
        >>> p.parents
        (Person(dad),)
        """
        return tuple(filter(None, [self.mother, self.father]))


class PersonCollection:

    """
    >>> bob = Person('bob')
    >>> bob.name = 'Bob Test'
    >>> alice = Person('alice')
    >>> alice.name = 'Alice Test'
    >>> alice.father = bob
    >>> collection = PersonCollection()
    >>> collection.add_person(alice)
    Person(alice, Alice Test)
    >>> for person in collection:
    ...     print(person.name)
    Bob Test
    Alice Test
    """

    def __init__(self):
        self._persons = {}
        self.__children = collections.defaultdict(set)
        self.__it = None

    def __getitem__(self, identifier: str) -> Person:
        """
        >>> c = PersonCollection()
        >>> c.add_person(Person("alice"))
        Person(alice)
        >>> c["alice"]
        Person(alice)
        """
        return self._persons[identifier]

    def add_person(self, person: Person) -> Person:
        """
        >>> c = PersonCollection()
        >>> c.add_person(Person("alice"))
        Person(alice)
        >>> c.add_person(Person("bob"))
        Person(bob)
        >>> c["bob"]
        Person(bob)

        >>> bob = Person("bob")
        >>> bob.birth_date = datetime.date(2010, 2, 3)
        >>> bob.mother = Person("bob-mum")
        >>> bob.father = Person("bob-dad")
        >>> c.add_person(bob)
        Person(bob, *2010-02-03)
        >>> list(c)
        [Person(alice), Person(bob, *2010-02-03), Person(bob-mum), Person(bob-dad)]
        """
        if person.mother is not None:
            person.mother = self.add_person(person.mother)
            self.__children[person.mother.identifier].add(person)
        if person.father is not None:
            person.father = self.add_person(person.father)
            self.__children[person.father.identifier].add(person)
        if person.identifier not in self._persons:
            self._persons[person.identifier] = person
            return person
        existing_person = self._persons[person.identifier]
        existing_person.merge(person)
        return existing_person

    def get_children(self, parent: typing.Union[Person, str]) -> typing.Set[Person]:
        """
        >>> c = PersonCollection()

        >>> alice = Person('alice')
        >>> alice.father = Person('bob')
        >>> c.add_person(alice)
        Person(alice)
        >>> c.get_children(alice)
        set()
        >>> c.get_children('bob')
        {Person(alice)}

        >>> carol = Person('carol')
        >>> carol.father = c['bob']
        >>> c.add_person(carol)
        Person(carol)
        >>> sorted(c.get_children('bob'), key=lambda p: p.identifier)
        [Person(alice), Person(carol)]

        does not support change / removal of parents:
        >>> carol.father = Person('other-bob')
        >>> c.add_person(carol)
        Person(carol)
        >>> c.get_children('other-bob')
        {Person(carol)}
        >>> sorted(c.get_children('bob'), key=lambda p: p.identifier)
        [Person(alice), Person(carol)]
        """
        if isinstance(parent, str):
            return self.__children[parent]
        return self.get_children(parent.identifier)

    def get_coparents(self, parent: typing.Union[Person, str]) -> typing.Set[Person]:
        """
        >>> c = PersonCollection()

        >>> alice = Person('alice')
        >>> alice.father = Person('bob')
        >>> c.add_person(alice)
        Person(alice)
        >>> c.get_coparents('bob')
        set()

        >>> alice.mother = Person('carol')
        >>> c.add_person(alice)
        Person(alice)
        >>> c.get_coparents('bob')
        {Person(carol)}
        >>> c.get_coparents(c['carol'])
        {Person(bob)}
        """
        if isinstance(parent, Person):
            return self.get_coparents(parent.identifier)
        coparents = set()
        for child in self.get_children(parent):
            for coparent in child.parents:
                if coparent.identifier != parent:
                    coparents.add(coparent)
        return coparents

    def __iter__(self) -> "PersonCollection":
        """
        >>> c = PersonCollection()
        >>> for identifier in ['alice', 'bob', 'charlie']:
        ...     c.add_person(Person(identifier))
        Person(alice)
        Person(bob)
        Person(charlie)
        >>> list(c)
        [Person(alice), Person(bob), Person(charlie)]
        """
        self.__it = iter(self._persons.values())
        return self

    def __next__(self) -> Person:
        return next(self.__it)
