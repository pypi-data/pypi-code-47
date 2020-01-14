from tokenizer_tools.tagset.offset.analysis.express_pattern import ExpressPattern
from tokenizer_tools.tagset.offset.corpus import Corpus
from tokenizer_tools.tagset.offset.document import Document
from tokenizer_tools.tagset.offset.span import Span
from tokenizer_tools.tagset.offset.span_set import SpanSet


def test_express_pattern(datadir):
    corpus = Corpus.read_from_file(datadir / "corpus.conllx")

    express_pattern = ExpressPattern(corpus)
    result = express_pattern.compute()

    expected = {
        ("<PERSON>", "在", "<GPE>", "的", "<ORG>", "读", "书", "。"): [
            Document(
                text=[
                    "王",
                    "小",
                    "明",
                    "在",
                    "北",
                    "京",
                    "的",
                    "清",
                    "华",
                    "大",
                    "学",
                    "读",
                    "书",
                    "。",
                ],
                span_set=SpanSet(
                    [
                        Span(0, 3, "PERSON", value=None, normal_value=None),
                        Span(4, 6, "GPE", value=None, normal_value=None),
                        Span(7, 11, "ORG", value=None, normal_value=None),
                    ]
                ),
                id="1",
                label=None,
                extra_attr={},
            ),
            Document(
                text=[
                    "王",
                    "小",
                    "明",
                    "在",
                    "台",
                    "北",
                    "新",
                    "竹",
                    "的",
                    "清",
                    "华",
                    "大",
                    "学",
                    "读",
                    "书",
                    "。",
                ],
                span_set=SpanSet(
                    [
                        Span(0, 3, "PERSON", value=None, normal_value=None),
                        Span(4, 8, "GPE", value=None, normal_value=None),
                        Span(9, 13, "ORG", value=None, normal_value=None),
                    ]
                ),
                id="3",
                label=None,
                extra_attr={},
            ),
        ],
        ("来", "一", "首", "<歌手名>", "的", "歌", "。"): [
            Document(
                text=["来", "一", "首", "蓝", "泽", "雨", "的", "歌", "。"],
                span_set=SpanSet([Span(3, 6, "歌手名", value=None, normal_value=None)]),
                id="2",
                label=None,
                extra_attr={},
            )
        ],
    }

    assert result == expected
