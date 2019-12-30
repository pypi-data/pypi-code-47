from multimetric.cls.base import MetricBase


class MetricBaseComments(MetricBase):
    _needles = [
        "Token.Comment",
        "Token.Comment.Hashbang",
        "Token.Comment.Multiline",
        "Token.Comment.Single",
        "Token.Comment.Special",
        "Token.Literal.String.Doc"
    ]

    _specific = {
        "Python": [
            "Token.Comment.Preproc"
        ]
    }

    METRIC_COMMENT_RATIO = "comment_ratio"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.__overall = 0
        self.__comments = 0

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        _n = MetricBaseComments._needles
        if language in MetricBaseComments._specific:
            _n += MetricBaseComments._specific[language]
        for x in tokens:
            self.__overall += len(str(x[1]))
            if str(x[0]) in _n:
                self.__comments += len(str(x[1]))

    def get_results(self):
        if self.__overall == 0:
            # sanity
            self.__overall = 1
        self._metrics[MetricBaseComments.METRIC_COMMENT_RATIO] = self.__comments * \
            100.0 / float(self.__overall)
        return self._metrics
