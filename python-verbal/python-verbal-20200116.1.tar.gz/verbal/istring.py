from __future__ import absolute_import

import string
import json
import sys
import re
from datetime import *

RegExPattern = type(re.compile(''))

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        # TODO make something that writes directly?
        if isinstance(obj, (datetime, date, time)):
            return obj.isoformat()
        if isinstance(obj, RegExPattern):
            return '/' + obj.pattern + '/'
        else:
            return repr(obj)        

class InterpolatedFormatter(string.Formatter):    
    def __init__(self, frame=None):
        self.frame = frame or sys._getframe(1)
                
    def get_value(self, key, args, kwargs):
        if isinstance(key, (int, long)):
            return args[key]
        elif key in kwargs:
            return kwargs[key]
        elif key in self.frame.f_locals:
            return self.frame.f_locals[key]
        elif key in self.frame.f_globals:
            return self.frame.f_globals[key]
        else:
            return None
        
    def convert_field(self, value, conversion):
        if conversion == 'l':
            return ', '.join(map(str, value))
        if conversion == 'd':
            return ', '.join( [ str(k)+ ': '+str(v) for k, v in value.iteritems() ] )
        if conversion == 'p':
            import pprint
            return pprint.pformat(value)
        if conversion == 'j':
            return json.dumps(value, skipkeys=True, indent=2, cls=JsonEncoder)
        if conversion == 'y':
            import yaml
            return yaml.safe_dump(value)
        if conversion == 'T':
            import pandas
            return pandas.DataFrame.from_records(value).to_string()
        return super(InterpolatedFormatter, self).convert_field(value, conversion)
        
class istr(str):
    def __new__(typ, x, *args, **kwargs):
        return str.__new__(typ, x)

    def __init__(self, x, _frame=None, *args, **kwargs):
        super(istr, self).__init__(x)
        self.frame = _frame or sys._getframe(1)
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        # capture the fields used int he interpolation,
        # make them available to the logger? 
        return InterpolatedFormatter(frame=self.frame).format(
            super(istr, self).__str__(), *self.args, **self.kwargs)

    def __format__(self, format_spec):
        return str(self) % format_spec

