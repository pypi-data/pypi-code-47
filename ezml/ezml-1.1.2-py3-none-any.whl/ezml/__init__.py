"""
E-Z Meta-Laguage - Parser - Supported Python Version: >= 3.6


LICENSE:

Copyright <2020> <Chad Groom>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


DEV NOTES For Upcoming Revision(1.1.3):
- Adding a dump_file() function for writing to files.
- Adding error handling.
- Adding a type system for INT, FLOAT, STRING.
- Adding meta sub-tags.


VERSION CONTROL:

Version 1
/
Revison x.1.0
/
(1.1.2)

"""

#Parser
class EZML:
    def __init__(self, string):
        
        #Get String
        self.string = string

        #Define Main Tags
        __ml = ["<ezml>", "</ezml>"]
        __meta = ["<meta>", "</meta>"]
        
        #Parse EZML
        ezml_init = string.split(__ml[0])[1].split(__ml[1])[0]

        #Check EZML For Null String
        if len(ezml_init) < 1:
            ezml_init = None

        #EZML - RETRIEVABLE ### < Type: String
        self.ezml = ezml_init

        #Parse META
        meta_init = string.split(__meta[0])[1].split(__meta[0])[0]

        #Check META For Null String
        if len(meta_init) < 1:
            meta_init = None

        #Metadata - RETRIEVABLE ### < Type: String
        self.meta = meta_init

        #Parse VARIABLES
        var = {}
        var_explode = self.string.split('\n')
        for x in range(0, len(var_explode)):
            if "<var " in var_explode[x]:
                this_var = var_explode[x].split('<var ')[1].split('>')[0]
                var[this_var] = self.ezml.split(f"<var {this_var}>")[1].split(f"</{this_var}>")[0]

        #Variable Stack - RETRIEVABLE ### < Type: Dict
        self.var = var

            
class utils:
    def dump_file(fname):
        with open(str(fname),'r') as d:
            return d.read()
        
    version = "1.1.2"
    


 
