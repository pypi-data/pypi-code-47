"""Generate a Tk from upon a Gui schema.

A GUI schema is a JSON-Schema dictionnary,
with tags require and existifs added to declare explicit cyclic depenencies
"""
from tkinter import Tk
from opentea.gui_forms.root_widget import OTRoot
from opentea.noob.validation import validate_opentea_schema

#CALLING_DIR = "NONE"

def main_otinker(schema, calling_dir=None, start_mainloop=True):
    """Startup the gui generation.

    Inputs :
    --------
    schema : dictionary compatible with json-schema
    calling_dir : directory from which otinker was called
    test_only : only for testing

    Outputs :
    ---------
    a tkinter GUI
    """
    #global CALLING_DIR
    #CALLING_DIR = calling_dir
    validate_opentea_schema(schema)
    tksession = Tk()

    OTRoot(schema, tksession, calling_dir, start_mainloop=start_mainloop)
    