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

import json
import argparse
import os
import subprocess
import shutil
import utils

import unix
from html_utils import get_build_html_commands

def parse_args():
    argparser = argparse.ArgumentParser(description = "Build the site.")
    argparser.add_argument("CONFIG", type = str,
                           help = "path to the JSON file containing the site's configurations")
    argparser.add_argument("INPUT", type = str,
                           help = "path to the input folder")
    argparser.add_argument("OUTPUT", type = str,
                           help = "path to the output folder")
    return argparser.parse_args()

def build(jsonFile, src, dst):
    data = None
    BUILD_FOLDER = "build"

    with open(jsonFile, "r") as f:
        data = json.load(f)

    pages = data["structure"]
    build_info = {}
    build_info["src"] = src
    build_info["dst"] = dst
    build_info["build_folder"] = BUILD_FOLDER
    build_info["pages"] = pages

    # build the dependency graph
    dep_graph_file_name = "depgraph"
    with open(dep_graph_file_name, "w") as f:
        for page_name, page_details in pages.items():
            if page_details["type"] == "page":
                # add an edge to itself to add the node to the output
                f.write("{} {}\n".format(page_name, page_name))
                if not utils.is_external_source(page_details["head"]):
                    f.write("{} {}\n".format(page_details["head"], page_name))
                for source_type, source_name in page_details["body"].items():
                    if not utils.is_external_source(source_name):
                        f.write("{} {}\n".format(source_name, page_name))

    # Topological sort, use Unix's coreutils tsort
    # A dependency graph is a DAG, so it has a topological order
    # The topological order is the building order
    # https://stackoverflow.com/a/95246
    # pipe the STDOUT to the p object, while STDERR will be displayed on command line
    proc = subprocess.run(unix.get_tsort_command(dep_graph_file_name).split(),
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    building_order = proc.stdout.decode('utf-8')
    building_order = building_order.split()

    # glue the pages together
    commands = []
    commands.append(unix.get_mkdir_command(build_info["build_folder"]))
    # move the non-pages to the build folder
    for page_name, page_details in pages.items():
        if not page_details["type"] == "other" and not page_details["type"] == "page":
            commands.append(unix.get_cp_command(os.path.join(src, page_details["source"]),
                                                os.path.join(build_info["build_folder"], page_name),
                                                "-f"))
    # move and build the pages
    for page_name in building_order:
        page_details = pages[page_name]
        if page_details["type"] == "page":
            commands.append(get_build_html_commands(page_name, page_details,
                                page_details["layout"], pages[page_details["layout"]], build_info))

    # put the pages to corresponding folders
    for page_name, page_details in pages.items():
        if utils.is_none(page_details["output"]):
            continue
        output_path = os.path.join(dst, page_details["output"])
        commands.append(unix.get_mkdir_command(os.path.dirname(output_path)))
        if not page_details["type"] == "other":
            commands.append(unix.get_cp_command(os.path.join(BUILD_FOLDER, page_name), os.path.join(dst, page_details["output"])))
        else:
            sources = page_details["source"]
            if type(sources) == str:
                source_path = os.path.join(src, sources)
                output_path = os.path.join(dst, page_details["output"])
                commands.append(unix.get_cp_command(source_path, output_path, "-r"))
            elif type(sources) == dict:
                for source_name, source in sources.items():
                    source_path = os.path.join(src, source)
                    output_path = os.path.join(dst, page_details["output"])
                    commands.append(unix.get_cp_command(source_path, output_path, "-r"))
    commands = ";".join(commands)
    proc = subprocess.run(commands, shell = True)
        
    # clean up
    commands = ["rm -f depgraph", "rm -rf build/"]
    commands = ";".join(commands)
    proc = subprocess.run(commands, shell = True)


if __name__ == "__main__":
    args = parse_args()
    build(args.CONFIG, args.INPUT, args.OUTPUT)
