import sys
import typing
from . import types
from . import ops
from . import path
from . import context
from . import props
from . import utils
from . import app

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''
