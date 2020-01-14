import collections

from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.span import Span


def test_repr__():
    span = Span(0, 9, 'entity')
    assert repr(span) == "Span(0, 9, 'entity', value=None, normal_value=None)"


def test_eq__():
    a = Span(0, 1, 'entity')
    b = Span(0, 1, 'entity')

    assert a == b

    c = Span(0, 2, 'entity')

    assert a != c


def test_hash__():
    a = Span(0, 1, 'entity')
    assert isinstance(a, collections.Hashable)


def test_init__():
    # TODO: check init checker
    pass


def test_bind():
    doc = Document("abc")
    doc.span_set.append(Span(start=0, end=1, entity="a"))

    result = doc.convert_to_md()
    expected = "[a](a) b c"

    assert result == expected

    span = doc.span_set[0]
    span.bind(doc)

    span.update_value("aaa")
    span.entity = "aaa"
    result = doc.convert_to_md()
    expected = "[a a a](aaa) b c"

    assert result == expected
