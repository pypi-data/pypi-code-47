from imperium.helpers import exists, matches, date, date_modify
from imperium.exceptions import UnsupportedFunctionException
import parser, re

AUTHORIZED_FUNCTIONS = { 
    'exists': True,
    'matches': True,
    'date': True,
    'date_modify': True
}

class Expression:

    def evaluate(self, expression, subject, source=None):
        self.expression = expression
        self.subject = subject

        matched = re.findall("([a-zA-Z_{1}][a-zA-Z0-9_]+)\s?\(", expression)
        for match in matched:
            if match not in AUTHORIZED_FUNCTIONS:
                raise UnsupportedFunctionException('[error] Unsupported function "{}"'.format(match))

        expression = expression.replace('$subject', 'subject')
        expression = expression.replace('$source', 'source')
        expr = parser.expr(expression)

        return eval(expr.compile(''))