# MIT License
#
# Copyright (c) 2019 Hoa Nguyen
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


import shlex

def get_echo_command(msg):
    return "echo {}".format(shlex.quote(msg))

def get_cp_command(src, dst, flags=""):
    return "cp {} {} {}".format(flags, src, dst)

def get_cat_command(filename):
    return "cat {}".format(filename)

def get_mkdir_command(filename):
    return "mkdir -p {}".format(filename)

def get_tsort_command(filename):
    return "tsort {}".format(filename)

def redirect_stdout(cmd, filename, _type):
    redirection = ""
    if _type == "overwrite":
        redirection = ">"
    elif _type == "append":
        redirection = ">>"
    return " ".join([cmd, redirection, filename])