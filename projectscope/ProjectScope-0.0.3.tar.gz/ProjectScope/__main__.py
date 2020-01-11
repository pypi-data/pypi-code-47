import sys
import os
import sqlite3

if(1 == len(sys.argv) or "-h" == sys.argv[1] or '--help' == sys.argv[1] ):
    print("""
    
    *****************
    *
    * Project Scope
    *
    *****************
    
    Welcome to the Project Scope management tool

    This tool is created to help manage the semantic connections in a project. The idea
    is that there are many kinds of data required by a project, and sometimes the organization
    of ideas cannot be effectively conveyed with a hierarchical file system. Therefore this
    tool was written to allow the flexibility in how information is linked together.

    Supported commands:
    1. ProjectScope Initialize - create a new project in the current directory
    2. ProjectScope Viewer - Open a 3D project visualizer application
    """)
    sys.exit(0)

if( "Viewer" == sys.argv[1] ):
    #Launch the viewer utility
    viewer_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ProjectScopeViewer.py")
    cmd = "python " + viewer_path
    os.system(cmd)

if( "Initialize" == sys.argv[1] ):
    #Initialize the current working directory with the required project
    # files
    if( not os.path.isfile(".projectscope") ):
        conn = sqlite3.connect(".projectscope")
        conn.close()
    else:
        print("Project file '.projectscope' already exists in this directory. Please remove it before initializing.")

