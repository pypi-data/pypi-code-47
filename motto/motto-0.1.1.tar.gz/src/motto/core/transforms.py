"""Core custom transforms for docutils
"""
from docutils import nodes
from docutils.transforms import Transform
from janome.tokenizer import Tokenizer
from . import Report, SkillParams, SkillProc, TokenRepository


class TokenizeTransform(Transform):
    """Content tokenize transform.

    At paragraph and title, tokenize internal content and bind as attribute.
    """

    default_priority = 90  # Used before other transforms of motto

    def apply(self):
        tokenizer = Tokenizer()  # TODO: Performance issue
        for node in self.document.traverse(nodes.paragraph):
            source = node.astext()
            node["tokens"] = TokenRepository(tokenizer.tokenize(source))


class InitializeReportTransform(Transform):
    """
    """

    default_priority = 91  # Used soon after Tokeninze

    def apply(self):
        for node in self.document.traverse(nodes.paragraph):
            node["report"] = Report()


class SkillTransform(Transform):
    """Skill applying transform.
    """

    default_priority = 400

    def __init__(
        self, skill_proc: SkillProc, skill_params: SkillParams, document, startnode=None
    ):
        super().__init__(document, startnode=startnode)
        self._skill_proc: SkillProc = skill_proc
        self._skill_params: SkillParams = skill_params

    # TODO: Add test with stub
    def apply(self):
        for node in self.document.traverse(nodes.paragraph):
            if "tokens" not in node or "report" not in node:
                continue
            tokens: TokenRepository = node["tokens"]
            report: Report = node["report"]
            msg = self._skill_proc(tokens, self._skill_params)
            if msg:
                report.add(msg)
