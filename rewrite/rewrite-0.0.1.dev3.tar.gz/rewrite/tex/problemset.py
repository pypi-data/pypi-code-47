# Standard Library
from typing import Tuple

# Thrid Party
from pylatex import Enumerate, Package

# Local
from rewrite import problem
from rewrite import tex

class ProblemSet(Enumerate):
    """An enumerated environment for numbering problems"""

    _latex_name = 'enumerate'
    packages = [Package('enumitem')]
    content_separator = ' \n' # The % in `\end{pycode}%` causes a TeX error

    def __init__(self, body: Tuple[object], **kwargs) -> object:
        self._body = body
        self.problems = []
        super().__init__(**kwargs)

        for item in self.body:
            if isinstance(item, problem.Problem):
                tex_problem = tex.Problem(item)
                self.problems.append(tex_problem)
                self.add_item(tex_problem.content)
            else:
                self.append(item)

    @property
    def body(self):
        return self._body

    def __next__(self):
        # Call next() on each problem
        for problem in self.problems:
            next(problem)