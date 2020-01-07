"""Small package that run better looking unittests"""

"""
For ColorTextTestResult, as it is inspired (a lot) by https://github.com/meshy/colour-runner:

Copyright (c) 2014 Charlie Denton

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import importlib
import time
import unittest
import sys

import blessings
import pygments
from pygments.formatters import Terminal256Formatter
from pygments.lexers.python import Python3TracebackLexer

SUITES_DIR = "test/suite"

terminal = blessings.Terminal()
colors = {
    "error": terminal.bold_red,
    "expected": terminal.bold_blue,
    "fail": terminal.bold_red,
    "skip": str,
    "success": terminal.bold_green,
    "title": terminal.bold_blue,
    "unexpected": terminal.bold_red,
}


class ColorTextTestResult(unittest.TestResult):
    """A test result class that prints color formatted text"""

    formatter = Terminal256Formatter()
    lexer = Python3TracebackLexer()
    separator1 = "=" * 70
    separator2 = "-" * 70
    indent = " " * 4

    _current_test_class = None

    def __init__(self, stream, descriptions, verbosity):
        super(ColorTextTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getShortDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return self.indent + doc_first_line
        return self.indent + test._testMethodName

    def getLongDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return "\n".join((str(test), doc_first_line))
        return str(test)

    def getClassDescription(self, test):
        test_class = test.__class__
        doc = test_class.__doc__
        if self.descriptions and doc:
            return doc.strip().split("\n")[0].strip()
        return test_class.__name__ + ":"

    def startTest(self, test):
        super(ColorTextTestResult, self).startTest(test)
        if self.showAll:
            if self._current_test_class != test.__class__:
                self._current_test_class = test.__class__
                title = self.getClassDescription(test)
                self.stream.writeln("\n" + colors["title"](title))
            self.stream.write(self.getShortDescription(test))
            self.stream.write(" ... ")
            self.stream.flush()

    def printResult(self, short, extended, colour_key=None):
        colour = colors[colour_key]
        if self.showAll:
            self.stream.writeln(colour(extended))
        elif self.dots:
            self.stream.write(colour(short))
            self.stream.flush()

    def addSuccess(self, test):
        super(ColorTextTestResult, self).addSuccess(test)
        self.printResult(".", "OK", "success")

    def addError(self, test, err):
        super(ColorTextTestResult, self).addError(test, err)
        self.printResult("E", "ERROR", "error")

    def addFailure(self, test, err):
        super(ColorTextTestResult, self).addFailure(test, err)
        self.printResult("F", "FAIL", "fail")

    def addSkip(self, test, reason):
        super(ColorTextTestResult, self).addSkip(test, reason)
        self.printResult("s", "skipped {0!r}".format(reason), "skip")

    def addExpectedFailure(self, test, err):
        super(ColorTextTestResult, self).addExpectedFailure(test, err)
        self.printResult("x", "expected failure", "expected")

    def addUnexpectedSuccess(self, test):
        super(ColorTextTestResult, self).addUnexpectedSuccess(test)
        self.printResult("u", "unexpected success", "unexpected")

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.writeln()
        self.printErrorList("ERROR", self.errors)
        self.printErrorList("FAIL", self.failures)

    def printErrorList(self, flavour, errors):
        colour = colors[flavour.lower()]

        for test, err in errors:
            self.stream.writeln(self.separator1)
            title = "%s: %s" % (flavour, self.getLongDescription(test))
            self.stream.writeln(colour(title))
            self.stream.writeln(self.separator2)
            self.stream.writeln(pygments.highlight(err, self.lexer, self.formatter))


class ColorTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return ColorTextTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        self.stream.writeln(result.separator2)
        run = result.testsRun
        self.stream.writeln(
            colors["title"](
                "Ran %d test%s in %.3fs" % (run, run != 1 and "s" or "", timeTaken)
            )
        )
        self.stream.writeln()
        if not result.wasSuccessful():
            self.stream.write(colors["unexpected"]("FAILED") + " (")
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                self.stream.write(colors["fail"]("failures=%d" % failed))
            if errored:
                if failed:
                    self.stream.write(", ")
                self.stream.write(colors["error"]("errors=%d" % errored))
            self.stream.writeln(")")
        else:
            self.stream.writeln(colors["success"]("OK"))
        return result


def get_suites_to_run():
    """Gets the list of all suites in the suite folder"""
    sys.path.insert(0, os.getcwd())  # needed when using binary
    suites = []
    for root, _, files in os.walk(SUITES_DIR):
        for filename in files:
            if not filename.startswith("_") and filename.endswith(".py"):
                module_name = root.replace("/", ".") + "." + filename[:-3]
                try:
                    module_file = importlib.import_module(module_name)
                    suite = module_file.suite()
                    suites.append(suite)
                    print("Suite from " + filename + " loaded.")
                except AttributeError:
                    sys.stderr.write(
                        "The suite from "
                        + filename
                        + " could not be added to the suites list.\n"
                    )
    return suites


def run():
    """Runs all the unittests in the suite folder"""
    suite = unittest.TestSuite()
    suites_to_tun = get_suites_to_run()
    for suite_to_run in suites_to_tun:
        suite.addTests(suite_to_run)
    runner = ColorTextTestRunner(verbosity=2)
    runner.run(suite)
