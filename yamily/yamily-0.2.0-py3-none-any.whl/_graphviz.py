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

import typing

import graphviz

from yamily import Person, PersonCollection


def _add_person_node(graph: graphviz.dot.Digraph, person: Person) -> None:
    label = person.name or person.identifier
    if person.birth_date is not None:
        label += r"\n*{}".format(person.birth_date.isoformat())
    if person.death_date is not None:
        label += r"\n†{}".format(person.death_date.isoformat())
    graph.node(person.identifier, label=label, shape="box")


def _add_parent_node(graph: graphviz.dot.Digraph, parents: typing.Set[Person]) -> str:
    parent_node_name = "relation-{}-{}".format(
        parents[0].identifier, parents[1].identifier
    )
    graph.node(parent_node_name, shape="point", width="0")
    for parent in parents:
        graph.edge(
            parent.identifier, parent_node_name, constraint="False", arrowhead="none",
        )
    return parent_node_name


def digraph(collection: PersonCollection) -> graphviz.dot.Digraph:
    """
    >>> bob = Person('bob')
    >>> bob.father = Person('frank')

    >>> carol = Person('carol')
    >>> carol.mother = Person('grace')

    >>> alice = Person('alice')
    >>> alice.mother = carol
    >>> alice.father = bob

    >>> collection = PersonCollection()
    >>> collection.add_person(alice)
    Person(alice)
    >>> graph = digraph(collection)
    >>> graph.render("/tmp/tree.dot")
    '/tmp/tree.dot.pdf'
    """
    graph = graphviz.Digraph("yamily")
    nodes: typing.Set[Person] = set()
    parent_node_names: typing.Dict[typing.Tuple[Person, Person], str] = dict()
    for person in collection:
        if person in nodes:
            continue
        # https://graphviz.gitlab.io/_pages/Gallery/directed/cluster.html
        with graph.subgraph(name="cluster_" + person.identifier) as subgraph:
            subgraph.attr(rank="same", style="invisible")
            _add_person_node(subgraph, person)
            nodes.add(person)
            for coparent in collection.get_coparents(person):
                parents = tuple(sorted((person, coparent), key=lambda p: p.identifier))
                parent_node_name = _add_parent_node(subgraph, parents)
                parent_node_names[parents] = parent_node_name
                parent_node_names[tuple(parents[::-1])] = parent_node_name
                _add_person_node(subgraph, coparent)
                nodes.add(coparent)
    for child in collection:
        if child.mother is not None and child.father is not None:
            parents = sorted(child.parents, key=lambda p: p.identifier)
            parent_node_name = parent_node_names[tuple(parents)]
            graph.edge(parent_node_name, child.identifier)
        elif child.mother is not None:
            graph.edge(child.mother.identifier, child.identifier)
        elif child.father is not None:
            graph.edge(child.father.identifier, child.identifier)
    return graph
