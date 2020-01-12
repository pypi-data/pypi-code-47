from .term import Term
from .course import Course, Section
from .assessment import Assessment
from .problem import Problem
from .schedule import generate_schedules
from . import mathlib

#############################
# DELETE BELOW AFTER REFACTORING


# DELETE ABOVE AFTER REFACTORING
#############################





#from . import course, assessment, problemset, section, mathlib
#from course import Course
#from assessment import Assessment
#from newquestion import NewQuestion
#from .lib import timer
# Replace examsage.Course with rescheduler.Course and rescheduler.Term
#from .course import Course
#from .term import Term
#from .schedule import generate_schedules
#from .assessment import Assessment
#from .headfoot import HeadFoot
#from .problemset import ProblemSet
#from .body import Body
#from .instructions import Instructions
#from .ztable import Ztable
#from .finitetiles import FiniteTiles
#from .newpagemessage import NewPageMessage
#from .problem import Problem
#from .pyvars import PyVars
#from .macros import Macros

import pathlib

name = "rewrite"
__version__ = '0.0.1.dev1' # for Sphinx
ROOT = pathlib.Path(__file__).parent
PROBLEMS_PATH = pathlib.Path(r'/home/user/questions')
IMAGE_PATH = ROOT / 'Images'


# Overload the pylatex.utils._latex_item_to_string method to allow
# for a Document to be appended to a Document

import pylatex
import pylatex.base_classes
import pylatex.utils

# Add support for appending documents to a document
# Add support for multiple versions of the same problem
def _latex_item_to_string(item, *, escape=False, as_content=False):
    """Use the render method when possible, otherwise uses str.
    Args
    ----
    item: object
        An object that needs to be converted to a string
    escape: bool
        Flag that indicates if escaping is needed
    as_content: bool
        Indicates whether the item should be dumped using
        `~.LatexObject.dumps_as_content`
    Returns
    -------
    NoEscape
        Latex
    """

    if isinstance(item, Problem):
        return item.dumps_content()
    elif isinstance(item, pylatex.Document):
        return item.dumps_content()
    elif isinstance(item, pylatex.base_classes.LatexObject):
        if as_content:
            return item.dumps_as_content()
        else:
            return item.dumps()
    elif not isinstance(item, str):
        item = str(item)

    if escape:
        item = pylatex.utils.escape_latex(item)

    return item

pylatex.utils._latex_item_to_string = _latex_item_to_string
