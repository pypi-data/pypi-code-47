# Copyright (C) 2018-2020 F. Cuvelier
# License: GNU GPL version 3
__version__='0.2.1' # automaticaly written by setpackages.py script
__packages__={'fc-tools': '0.0.24'} # automaticaly written by setpackages.py script

from . import simplicial

# from . import demos
#import benchs
from .utils import feval,getMesh

from . import demos
from . import benchs

def gitinfo():
  return {'name': 'fc-meshtools', 'tag': '0.2.1', 'commit': 'ec087ad15b223964e1d6d068a5f8c7219763216e', 'date': '2020-01-05', 'time': '07-07-00', 'status': '0'} # automatically updated
  if len(inf)>0: 
    return inf
  # Only for developpers
  import fc_tools,os
  from . import __path__
  D=os.path.realpath(os.path.join(__path__[0],os.path.pardir))
  if os.path.basename(D)=='src':
    D=os.path.realpath(os.path.join(D,os.path.pardir))
  return fc_tools.git.get_info(D)


