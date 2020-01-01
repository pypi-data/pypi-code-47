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

import os
import utils
import unix

def get_build_html_commands(page_name, page_details, layout_name, layout_details, build_info):
    src = build_info["src"]
    dst = build_info["dst"]
    pages = build_info["pages"]
    build_folder = build_info["build_folder"]
    
    page_output_dir_path = os.path.join(dst, os.path.dirname(page_details["output"]))
    layout_output_dir_path = os.path.join(dst, layout_details["output"])
    layout_relative_path_to_page = utils.get_relative_path(layout_output_dir_path, page_output_dir_path)

    page_build_path = os.path.join(build_folder, page_name)

    append_to_page = lambda msg: unix.redirect_stdout(unix.get_echo_command(msg), page_build_path, "append")
    append_from_file = lambda filename: unix.redirect_stdout(unix.get_cat_command(filename), page_build_path, "append")

    commands = []
    commands.append(unix.redirect_stdout(unix.get_echo_command(""), page_build_path, "overwrite"))
    commands.append(append_to_page("<!DOCTYPE html>"))

    # <head>
    commands.append(append_to_page("<head>"))
    commands.append(append_from_file(utils.get_source_file(page_details["head"], build_info)))
    commands.append(append_to_page("<link rel=\"stylesheet\" href=\"{}\">".format(layout_relative_path_to_page)))
    commands.append(append_to_page("</head>"))
    
    # <body>
    commands.append(append_to_page("<body>"))
    commands.append(append_to_page("<div class=\"{}\">".format(layout_name)))
    for grid_name, source in page_details["body"].items():
        commands.append(append_to_page("<div id=\"{}\">".format(grid_name)))
        commands.append(append_from_file(utils.get_source_file(source, build_info)))
        commands.append(append_to_page("</div>"))

    commands.append(append_to_page("</div>"))
    commands.append(append_to_page("</body>"))


    return ";".join(commands)