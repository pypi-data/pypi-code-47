#!/usr/bin/env python3
"""Takes an osm file as an input, applies the visibility graph on it and saves the output in the working directory

Usage:
    app.py  --map=Filepath


Options:
-h --help     Show help.
map           The Openstreetmap in oml format to apply the visibility graph on
"""

from docopt import docopt
import sys
import os.path
import os, subprocess

# Errors
from xml.etree.ElementTree import ParseError

from ReaderWriter.Reader import Reader
from ReaderWriter.Writer import Writer
from VisibilityGraph.VisibilityGraph import VisibilityGraph


class App():
    """ Controller for other classes & entry point"""

    def open_output(self, path):
        """Opens the output folder"""
        if sys.platform == "win32":
            os.startfile(path)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
    @staticmethod
    def main():
        """ Chains function calls to read, apply visbility graph and write new file

            1. Parse the command line argument for map
            2. Initialize Reader Object and read the filepath from 1
            3. Initialize VisbilityGraph and create ways for the OpenSpaces from 2
            4. Initialize Writer and write old data + new ways to a new file
        """
        args = docopt(__doc__)
        filepath = args["--map"]

        #Read & parse osm
        try:
            openspaces = Reader().parse_xml(filepath)
        except ParseError: #TODO: What kind of exception do we get back?
            sys.stderr.write("Error parsing input file. It might be invalid.\n")
            sys.exit()
        except FileNotFoundError:
            sys.stderr.write("The file could not be found. Please check the path.\n")
            sys.exit()
        except TypeError as e:
            print(e)
            sys.stderr.write("Invalid argument\n")
            sys.exit()

        if openspaces:
            print(f"Read in osm file and extracted {len(openspaces)} Openspaces")
            # Apply visibility graph
            try:
                openspace_list = list(openspaces.values())
                new_ways =  VisibilityGraph(openspace_list).create()
                print(f"Created {len(new_ways)} new ways")
            except Exception as e:
                print(e)
                sys.exit()

            #Write the output
            try:
                file_with_extension = os.path.basename(filepath)
                filename = file_with_extension.split(".")[-2] # remove file extension
                dirpath = os.path.dirname(filepath)
                new_filename = f"{filename}-vg.osm"
                new_path = os.path.join(dirpath, new_filename)
                Writer(new_ways).write(filepath, new_path)
                print(f"Succesfully wrote the enriched osm to {dirpath}")
                try:
                    self.open_output(dirpath)
                except Exception:
                    print("Could not open the output folder.")
            except Exception as e:
                print(e)
                sys.exit()

        else:
            print(f"""There haven't been any Openspaces in the input""")
            # TODO: Erklärung, was man tun soll (welche Daten)


if __name__ == '__main__':
    App().main()
