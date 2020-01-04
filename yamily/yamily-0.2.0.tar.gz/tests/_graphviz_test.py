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
from yamily._graphviz import digraph


def test_digraph_person_details():
    collection = PersonCollection()
    person = Person("bob")
    person.name = "Bob Test"
    person.birth_date = datetime.date(1923, 4, 5)
    person.death_date = datetime.date(2012, 3, 4)
    collection.add_person(person)
    graph = digraph(collection)
    expected_graph = r"""digraph yamily {
	subgraph cluster_bob {
		rank=same style=invisible
		bob [label="Bob Test\n*1923-04-05\n†2012-03-04" shape=box]
	}
}"""
    assert graph.source == expected_graph


def test_digraph_single_family():
    collection = PersonCollection()
    child = Person("child")
    child.father = Person("father")
    child.mother = Person("mother")
    collection.add_person(child)
    graph = digraph(collection)
    expected_graph = """digraph yamily {
	subgraph cluster_mother {
		rank=same style=invisible
		mother [label=mother shape=box]
		"relation-father-mother" [shape=point width=0]
		father -> "relation-father-mother" [arrowhead=none constraint=False]
		mother -> "relation-father-mother" [arrowhead=none constraint=False]
		father [label=father shape=box]
	}
	subgraph cluster_child {
		rank=same style=invisible
		child [label=child shape=box]
	}
	"relation-father-mother" -> child
}"""
    assert graph.source == expected_graph


def test_digraph_grandparents():
    collection = PersonCollection()
    father = Person("father")
    father.father = Person("grandfather")
    father.mother = Person("grandmother")
    child_a = Person("child-a")
    child_a.father = father
    child_a.mother = Person("mother")
    collection.add_person(child_a)
    child_b = Person("child-b")
    child_b.father = father
    child_b.mother = Person("mother")
    collection.add_person(child_b)
    graph = digraph(collection)
    expected_graph = """digraph yamily {
	subgraph cluster_mother {
		rank=same style=invisible
		mother [label=mother shape=box]
		"relation-father-mother" [shape=point width=0]
		father -> "relation-father-mother" [arrowhead=none constraint=False]
		mother -> "relation-father-mother" [arrowhead=none constraint=False]
		father [label=father shape=box]
	}
	subgraph cluster_grandmother {
		rank=same style=invisible
		grandmother [label=grandmother shape=box]
		"relation-grandfather-grandmother" [shape=point width=0]
		grandfather -> "relation-grandfather-grandmother" [arrowhead=none constraint=False]
		grandmother -> "relation-grandfather-grandmother" [arrowhead=none constraint=False]
		grandfather [label=grandfather shape=box]
	}
	subgraph "cluster_child-a" {
		rank=same style=invisible
		"child-a" [label="child-a" shape=box]
	}
	subgraph "cluster_child-b" {
		rank=same style=invisible
		"child-b" [label="child-b" shape=box]
	}
	"relation-grandfather-grandmother" -> father
	"relation-father-mother" -> "child-a"
	"relation-father-mother" -> "child-b"
}"""
    assert graph.source == expected_graph
