# License: MIT (expat)
#
# This script is heavily inspired by android-localization-helper
# by Jordan Jozwiak.
# 
# Copyright (c) 2018-2020 Julien Lepiller <julien@lepiller.eu>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#####

from .parser import entry, parser
from .languages import default_plural_from_english

class android(list):
    """The main class for android strings lib. An android translation uses
        two files: the origin file (usually containing the English strings) and
        the destination file (containing the translated strings). We also need
        to know the language of the destination to properly handle plurals in
        that language."""
    def __init__(self, origin, destination, lang):
        list.__init__(self)
        self.lang = lang
        self.origin = parser(origin)
        self.destination = parser(destination)
        keys = self.origin.getKeyValues()
        for k in keys:
            trans = self.destination.getById(k.id)
            txt = trans.orig
            if trans.type != k.type or not self.destination.hasId(k.id):
                if k.type == 'plurals':
                    txt = default_plural_from_english(k.orig, lang)
                else:
                    txt = k.orig
            comm = None
            if k.comment != None:
                comm = k.comment
            if trans.comment != None:
                comm = trans.comment
            self.append(entry(k.type, k.id, k.orig, txt, comm))

    def save(self):
        """Save the translation. This method only saves the destination. It
            always overwrites the destination file. When the destination file
            was not in sync with the origin file, it updates the destination
            file, even if no translation was modified. It will delete any ID
            that is not present in the origin file and add IDs present in the
            origin file but not in the destination file."""
        keyvalues = []
        for k in self:
            keyvalues.append(entry(k.type, k.id, k.dst, '', k.comment))
        self.destination.set(keyvalues)
        self.destination.save()

    def getValuesById(self, key):
        """Get a tuple from the key that corresponds to the original value
           associated with the key and the translated value."""
        return (self.origin.getById(key).orig, self.destination.getById(key).orig)

    def getById(self, key):
        """Get the entry that corresponds to key."""
        for k in self:
            if k.id == key:
                return k
        return None

