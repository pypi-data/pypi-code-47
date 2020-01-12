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

import xml.etree.ElementTree as ET
import os

# http://effbot.org/zone/element-pi.htm
# Allows to parse comments
class AndroidParser(ET.TreeBuilder):
    def __init__(self):
        ET.TreeBuilder.__init__(self)
        self.start("document", {})
    
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)

    def close(self):
        self.end("document")
        return ET.TreeBuilder.close(self)

# in-place prettyprint formatter
# http://effbot.org/zone/element-lib.htm#prettyprint
def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

class entry(object):
    """Represents an entry in the strings file.
        Each entry has a type (string, …), an ID and a content, divided in
        the orig content, the dst content and comments."""
    def __init__(self, type, id, orig, dst, comment=None):
        self.type = type
        self.id = id
        self.orig = orig
        self.dst = dst
        self.comment = comment

    def __str__(self):
        return "<entry type:" + self.type + ", id: "+self.id+", original: \"" + str(self.orig) + \
                "\", translation: \"" + str(self.dst) + "\", comment: \"" + str(self.comment) + "\">"

class parser(object):
    """Read file, a path to a strings.xml file and parse it.
        Android translation files are separated in two files: a source
        file (usually english) and a destination file (othe languages).
        Each file contains entries with a id and a value. This class parses
        the file and recovers id and strings, independent of whether the file
        is a source or a destination.
    """
    def __init__(self, file):
        self.file = file
        if(os.path.isfile(file)):
            self.content = ET.parse(file, parser=ET.XMLParser(target=AndroidParser()))
            self.keyvalues = self.getKeyValues()
        else:
            raise Exception('File not found')

    def getKeys(self):
        """Return all the IDs available in the file."""
        root = self.content.getroot()
        keys = []
        comment = ''
        for child in root:
            # ignore strings that can't be translated
            if child.get('translatable', default='true') == 'false':
                continue
            # ignore comments
            if not isinstance(child.tag, str):
                continue
            # ignore providers
            if (child.get('name').startswith('provider.')):
                continue
            keys.append((child.tag, child.get('name')))
        return keys

    def getKeyValues(self):
        """Returns all the entries contained in the file, as a list of Entries.
            Each entry has its content filled in the orig field. The dst field
            is empty."""
        root = self.content.getroot()
        comment = None
        # Content is wrapped around a "document" tag, so we need to open it.
        # It could contain more than one child if there are comments though,
        # so read them.
        for child in root:
            if not isinstance(child.tag, str):
                comment = child.text
                continue
            if child.tag == "resources":
                root = child
                break
        values = []
        for child in root:
            # ignore strings that can't be translated
            if child.get('translatable', default='true') == 'false':
                continue
            if not isinstance(child.tag, str):
                comment = child.text
                continue
            # ignore providers
            if (not child.get('name') is None) and (child.get('name').startswith('provider.')):
                continue
            value = []
            if child.tag == "string":
                value = child.text
            elif child.tag == "string-array":
                for c in child:
                    value.append(c.text)
            elif child.tag == "plurals":
                value = {}
                for c in child:
                    value[c.get('quantity')] = c.text
            else:
                # unrecognized tag
                continue
            values.append(
                entry(child.tag, child.get('name'), value, '', comment))
            if comment != None:
                comment = None
        return values

    def getById(self, id):
        """Return the entry whose id is given as a paramater. The orig field
            contains the value of the entry, while the dst field is empty,
            regardless of whether this is a source or a destination file."""
        for k in self.keyvalues:
            if k.id == id:
                return k
        return entry('string', id, '', '')

    def hasId(self, id):
        """Return whether the entry whose id is given as a parameter exists."""
        for k in self.keyvalues:
            if k.id == id:
                return True
        return False

    def set(self, keyvalues):
        """Completely replace the list of entries."""
        self.keyvalues = keyvalues

    def save(self):
        """Save the content o the object to the original file. This method
            overwrites the original file, so use with care."""
        root = ET.Element('resources')
        tree = ET.ElementTree(root)
        for data in self.keyvalues:
            if data.comment != None:
                c = ET.Comment(data.comment)
                root.append(c)
            v = ET.SubElement(root, data.type)
            v.set('name', data.id)
            if data.type == "string-array":
                for val in data.orig:
                    item = ET.SubElement(v, 'item')
                    item.text = val
            elif data.type == "plurals":
                for plural in data.orig:
                    item = ET.SubElement(v, 'item')
                    item.set('quantity', plural)
                    item.text = data.orig[plural]
            else:
                v.text = data.orig
        indent(root)
        tree.write(self.file, "UTF-8")
