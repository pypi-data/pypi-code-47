from docutils.nodes import NodeVisitor
from docutils.writers import Writer as BaseWriter


class ReportTranslator(NodeVisitor):
    """Reporting formatter translations
    """

    def __init__(self, document):
        super().__init__(document)
        self.body = []

    def _visit_any(self, node):
        """Register reports and pointer( filename + lineno) into output body.

        This is called when visited any node.
        """
        if "report" not in node:
            return
        report = node["report"]
        if len(report) <= 0:
            return
        self.body.append(
            [f"{node.source}:{node.line}-", [m.body for m in report._messages],]
        )

    def _depart_any(self, node):
        pass

    def __getattr__(self, name):
        if name.startswith("visit_"):
            return self._visit_any
        if name.startswith("depart_"):
            return self._depart_any
        return super().__getattr__(name)


class Writer(BaseWriter):
    """Custom writer to use ReportTranslator.
    """

    def translate(self):
        translator = ReportTranslator(self.document)
        self.document.walkabout(translator)
        self.output = ""
        for t in translator.body:
            self.output += f"{t[0]}\n1"
            self.output += "\n".join([f"\t{m}" for m in t[1]])
            self.output += "\n"
