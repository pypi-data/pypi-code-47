# Copyright (C) 2007-2020 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Appy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Appy. If not, see <http://www.gnu.org/licenses/>.

# ------------------------------------------------------------------------------
import time

from appy.px import Px
from appy.fields import Field

# ------------------------------------------------------------------------------
class Hour(Field):
    '''Field allowing to define an hour independently of a complete date'''

    pxView = pxCell = Px('''<x>:value</x>''')

    pxEdit = Px('''
     <x var="hPart=hPart | '%s_hour' % name;
             mPart=mPart | '%s_minute' % name;
             hours=range(0,24)">
      <select name=":hPart" id=":hPart">
       <option value="">-</option>
       <option for="hour in hours"
         var2="zHour=str(hour).zfill(2)" value=":zHour"
         selected=":field.isSelected(zobj, hPart, 'hour', \
                                     hour, rawValue)">:zHour</option>
      </select> : 
      <select var="minutes=range(0, 60, field.minutesPrecision)"
              name=":mPart" id=":mPart">
       <option value="">-</option>
       <option for="min in minutes"
         var2="zMin=str(min).zfill(2)" value=":zMin"
         selected=":field.isSelected(zobj, mPart, 'minute', \
                                     min, rawValue)">:zMin</option>
      </select>
     </x>''')

    hourParts = ('hour', 'minute')

    def __init__(self, validator=None, multiplicity=(0,1), default=None,
      defaultOnEdit=None, hourFormat=None, minutesPrecision=5, show=True,
      page='main', group=None, layouts=None, move=0, indexed=False,
      mustIndex=True, indexValue=None, searchable=False,
      specificReadPermission=False, specificWritePermission=False, width=None,
      height=None, maxChars=None, colspan=1, master=None, masterValue=None,
      focus=False, historized=False, mapping=None, generateLabel=None,
      label=None, sdefault=None, scolspan=1, swidth=None, sheight=None,
      persist=True, view=None, cell=None, edit=None, xml=None,
      translations=None):
        # If no p_hourFormat is specified, the application-wide tool.hourFormat
        # is used instead.
        self.hourFormat = hourFormat
        # If "minutesPrecision" is 5, only a multiple of 5 can be encoded. If
        # you want to let users choose any number from 0 to 59, set it to 1.
        self.minutesPrecision = minutesPrecision
        Field.__init__(self, validator, multiplicity, default, defaultOnEdit,
          show, page, group, layouts, move, indexed, mustIndex, indexValue,
          searchable, specificReadPermission, specificWritePermission, width,
          height, None, colspan, master, masterValue, focus, historized,
          mapping, generateLabel, label, sdefault, scolspan, swidth, sheight,
          persist, False, view, cell, edit, xml, translations)

    def getFormattedValue(self, obj, value, layoutType='view',
                          showChanges=False, language=None):
        if self.isEmptyValue(obj, value): return ''
        format = self.hourFormat or obj.getTool().appy().hourFormat
        hour, minute = [str(part).zfill(2) for part in value]
        return format.replace('%H', hour).replace('%M', minute)

    def getRequestValue(self, obj, requestName=None):
        request = obj.REQUEST
        name = requestName or self.name
        r = []
        empty = True
        for partName in self.hourParts:
            part = request.get('%s_%s' % (name, partName), '')
            if part: empty = False
            r.append(part)
        return not empty and ':'.join(r) or None

    def getRequestSuffix(self): return '_hour'

    def getStorableValue(self, obj, value, complete=False):
        if not self.isEmptyValue(obj, value):
            return tuple(map(int, value.split(':')))

    def validateValue(self, obj, value):
        '''Ensure p_value is complete: all parts must be there (minutes and
           seconds).'''
        if value.startswith(':') or value.endswith(':'):
            # A part is missing
            return obj.translate('field_required')

    def isSelected(self, obj, part, fieldPart, hourValue, dbValue):
        '''When displaying this field, must the particular p_hourValue be
           selected in the sub-field p_fieldPart corresponding to the hour
           p_part ?'''
        # Get the value we must compare (from request or from database)
        req = obj.REQUEST
        if req.has_key(part):
            compValue = req.get(part)
            if compValue.isdigit():
                compValue = int(compValue)
        else:
            compValue = dbValue
            if compValue:
                i = (fieldPart == 'minute') and 1 or 0
                compValue = dbValue[i]
        # Compare the value
        return compValue == hourValue

    # --------------------------------------------------------------------------
    # Class methods
    # --------------------------------------------------------------------------

    @classmethod
    def hourDifference(class_, h1, h2):
        '''Computes the number of hours between h1 and h2'''
        if h2 < h1:
            # h2 is the day after
            h2 += 24
        return h2 - h1

    @classmethod
    def getDuration(class_, start, end):
        '''Returns the duration, in minutes, of the interval [start, end]'''
        # Manage minutes
        minutes = end[1] - start[1]
        if minutes < 0:
            minutes += 60
            endHour = (end[0] == 0) and 23 or (end[0]-1)
        else:
            deltaHour = 0
            endHour = end[0]
        return ((class_.hourDifference(start[0], endHour))*60) + minutes

    @classmethod
    def formatDuration(class_, minutes, sep='h'):
        '''Returns a formatted version of this number of p_minutes'''
        modulo = minutes % 60
        hours = int(minutes / 60.0)
        r = '%d%s' % (hours, sep)
        if modulo:
            r += str(modulo).zfill(2)
        return r
# ------------------------------------------------------------------------------
