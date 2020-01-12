import os
import sys
import inspect
import sqlite3
import posixpath
import importlib

global project_filepath


def get_caller_filepath():
    # Get the filenames in the stack
    frame = inspect.stack()[1]
    filenames = [stack.filename for stack in inspect.stack()]

    # Scan through the stack, rolling backwards until we find a
    # file name that isn't the same as this file, and isn't starting
    # with '<' as this indicates a library.
    for filename in filenames:
        if(filename != __file__ and not filename.startswith("<")):
            return os.path.abspath(filename)
    return None


# Try and find the .projectscope file relative to the CWD. Check the folders
# one-by-one to see if there is a projectscope file.
project_filepath = None
starting_path = os.path.dirname(get_caller_filepath())
while True:
    filepath = os.path.join(starting_path, ".projectscope")
    if(os.path.isfile(filepath)):
        # Found the project file
        project_filepath = filepath
        break
    else:
        new_start_path = os.path.abspath(os.path.join(starting_path, ".."))
        if(new_start_path == starting_path):
            # Cannot search any deeper, bail out now
            break
        starting_path = new_start_path


def load_project(filepath):
    """Method to override the project filepath"""
    global project_filepath
    project_filepath = filepath


def get_filepath(originating_node_path, logical_path):
    global project_filepath

    # Logical paths are of the format link/link/.../link/node, so we
    # have to follow the links until we hit a node, then we can get
    # the nodes path. Start from the current node (of which we know
    # the file path), and then follow links until we get to the
    # target node.

    # Get the node_id for the originating node
    orig_rel_path = os.path.relpath(originating_node_path, os.path.dirname(project_filepath))
    if os.name == "nt":
        orig_rel_path = orig_rel_path.replace(os.pathsep, posixpath.sep)
    conn = sqlite3.connect(project_filepath)
    c = conn.execute('''SELECT id FROM nodes WHERE path = ?''', (orig_rel_path,))
    data = c.fetchall()
    if(None == data or len(data) != 1):
        print("Encountered an issue finding the originating file {} in the database!".format(orig_rel_path))
        return None

    originating_node_id = data[0][0]

    links = logical_path.split('/')[:-1]
    node = logical_path.split('/')[-1]

    if(0 == len(links)):
        # Possibly the link is unnamed. In that case there is an implicit link connecting
        # the two nodes. In this case, fetch all of the unnamed links connected to the
        # originating node and find a node with the name we're searching for
        params = (originating_node_id, originating_node_id, originating_node_id,
                  originating_node_id, originating_node_id, originating_node_id, node)
        c = conn.execute('''SELECT path FROM nodes
                            INNER JOIN
                            (
                            SELECT links.node_id1 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id1 != ? AND links.name = ""
                            UNION
                            SELECT links.node_id2 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id2 != ? AND links.name = ""
                            ) AS d
                            ON d.node_id = nodes.id
                            WHERE nodes.name = ?''',
                         params)
        data = c.fetchall()

        if(data is None or len(data) != 1):
            print("Ambiguous link/node combination!")
            return None

        # Convert the relative unix file path to something absolute and
        # to the liking of this OS
        file_rel_unix_path = data[0][0]
        if os.name == "nt":
            file_rel_unix_path = file_rel_unix_path.replace(posixpath.sep, os.sep)
        abs_path = os.path.abspath(file_rel_unix_path)
        return abs_path

    # We have some links to follow
    node_id = originating_node_id
    for link_name in links:
        params = (node_id,
                  node_id,
                  node_id,
                  link_name,
                  node_id,
                  node_id,
                  node_id,
                  link_name)
        c = conn.execute('''SELECT links.node_id1 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id1 != ? AND links.name = ?
                            UNION
                            SELECT links.node_id2 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id2 != ? AND links.name = ?''',
                         params)
        data = c.fetchall()
        if(data is None or len(data) != 1):
            print("Problem following link!")
            return None

        # Move to the next node, and iterate as many times as required to follow all links
        node_id = data[0][0]

    c = conn.execute('''SELECT path FROM nodes WHERE id = ?''', (node_id,))
    data = c.fetchone()
    if(data is None or len(data) != 1):
        print("Problem getting node path!")
        return None

    # Convert the relative unix file path to something absolute and
    # to the liking of this OS
    file_rel_unix_path = data[0]
    if os.name == "nt":
        file_rel_unix_path = file_rel_unix_path.replace(posixpath.sep, os.sep)
    abs_path = os.path.join(os.path.dirname(project_filepath), file_rel_unix_path)

    return abs_path


def load(import_string):

    if("import" not in import_string):
        print("Nothing to import! (params={})".str(import_string))
        return

    import_params = import_string.split(" ")
    import_dict = {'as': None, 'import': None, 'from': None}
    import_dict['import'] = import_params[import_params.index('import') + 1]
    if('as' in import_params):
        import_dict['as'] = import_params[import_params.index('as') + 1]
    if('from' in import_params):
        import_dict['from'] = import_params[import_params.index('from') + 1]

    # Now we want to get the real filepath where the module lives. The 'from'
    # logical path should be used if supplied, otherwise just use the import
    # specifier.
    logical_path = import_dict['import']
    if(None != import_dict['from']):
        logical_path = import_dict['from']

    # Now we have something that might be a mix of logical ('/' type path) and
    # a python path ('.' type path). We just want the logical part, so strip
    # off the python path if supplied.
    python_sep_idx = logical_path.find('.')
    if(-1 != python_sep_idx):
        # There is a python path as a part of this string. Strip it off now.
        logical_path = logical_path[:python_sep_idx]

    # Translate the logical path to a physical one
    filepath = get_filepath(get_caller_filepath(), logical_path)
    if(None == filepath):

        # Can't find the module!
        print("Cannot import: '{}'".format(import_string))
        return

    # Add the path to the module to the sys-path. This lets us
    # easily import the module. After we are done we will pop
    # this path if it wasn't already on the sys-path.
    folder_path = os.path.dirname(filepath)
    pop_folder_path = False
    if(folder_path not in sys.path):
        sys.path.append(folder_path)
        pop_folder_path = True

    # Now we have set up the folder path to allow us to access
    # the python module(s). From here we use the dot operators
    # and from/import paths to finish the rest of the import.
    # build up the full python path we will have to import now,
    # starting after the phyiscal address determined above.
    import_list = import_dict['import'].split("/")[-1].split(".")

    if(None != import_dict['as']):

        # The 'as' specifier is interesting, it seems to have the
        # effect of moving all but the last import in the 'import'
        # specifier to the 'from' specifier effectively. Do that
        # effect here
        if(len(import_list) > 1):
            if(None == import_dict['from']):
                import_dict['from'] = ".".join(import_list[:-1])
            else:
                import_dict['from'] += "." + ".".join(import_list[:-1])
        import_list = [import_list[-1]]
    import_list_orig = import_list[:]

    from_path = None
    if(None == import_dict['from']):

        # Take care to adjust the first parameter which needs
        # a logical/physical translation
        import_list[0] = os.path.basename(filepath)
        if(import_list[0].endswith(".py")):
            import_list[0] = import_list[0][:-3]

    else:

        # We are using a from specifier.
        from_list = import_dict['from'].split(".")
        from_list[0] = os.path.basename(filepath)
        if(from_list[0].endswith(".py")):
            from_list[0] = from_list[0][:-3]
        from_path = ".".join(from_list)

    # Now load the 'import' part of the statement
    if('*' != import_dict['import']):

        # We have a straight forward import. The 'from'
        # section is our 'package', and then we want to
        # import each of the modules along the 'import' path.
        for i in range(len(import_list)):
            if(None != from_path):
                import_path = "." + ".".join(import_list[0:i+1])
            else:
                import_path = ".".join(import_list[0:i+1])

            res = importlib.import_module(import_path, from_path)

            if(import_dict['as'] is not None):
                # There will only be one import, and we know the name
                inspect.stack()[1][0].f_globals[import_dict['as']] = res
            else:
                # There may be many imports, and we need to restore the
                # original name in the [0] location of the name
                name_path = ".".join(import_list_orig[0:i+1])
                inspect.stack()[1][0].f_globals[name_path] = res

    # Now remember to remove the path from the sys-path
    if(pop_folder_path):
        sys.path.pop(sys.path.index(folder_path))

    return


def get_node_path(logical_path):
    global project_filepath

    # Logical paths are of the format link/link/.../link/node, so we
    # have to follow the links until we hit a node, then we can get
    # the nodes path. Start from the current node (of which we know
    # the file path), and then follow links until we get to the
    # target node.

    originating_node_path = get_caller_filepath()

    # Get the node_id for the originating node
    orig_rel_path = os.path.relpath(originating_node_path, os.path.dirname(project_filepath))
    if os.name == "nt":
        orig_rel_path = orig_rel_path.replace(os.pathsep, posixpath.sep)
    conn = sqlite3.connect(project_filepath)
    c = conn.execute('''SELECT id FROM nodes WHERE path = ?''', (orig_rel_path,))
    data = c.fetchall()
    if(None == data or len(data) != 1):
        print("Encountered an issue finding the originating file {} in the database!".format(orig_rel_path))
        return None

    originating_node_id = data[0][0]

    links = logical_path.split('/')[:-1]
    node = logical_path.split('/')[-1]

    if(0 == len(links)):
        # Possibly the link is unnamed. In that case there is an implicit link connecting
        # the two nodes. In this case, fetch all of the unnamed links connected to the
        # originating node and find a node with the name we're searching for
        params = (originating_node_id, originating_node_id, originating_node_id,
                  originating_node_id, originating_node_id, originating_node_id, node)
        c = conn.execute('''SELECT path FROM nodes
                            INNER JOIN
                            (
                            SELECT links.node_id1 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id1 != ? AND links.name = ""
                            UNION
                            SELECT links.node_id2 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id2 != ? AND links.name = ""
                            ) AS d
                            ON d.node_id = nodes.id
                            WHERE nodes.name = ?''',
                         params)
        data = c.fetchall()

        if(data is None or len(data) != 1):
            print("Ambiguous link/node combination!")
            return None

        # Return the path!
        return data[0][0]

    # We have some links to follow
    node_id = originating_node_id
    for link_name in links:
        params = (node_id,
                  node_id,
                  node_id,
                  link_name,
                  node_id,
                  node_id,
                  node_id,
                  link_name)
        c = conn.execute('''SELECT links.node_id1 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id1 != ? AND links.name = ?
                            UNION
                            SELECT links.node_id2 as node_id
                            FROM links
                            INNER JOIN (SELECT id FROM links WHERE node_id1 = ? or node_id2 = ?) AS c
                            ON c.id = links.id
                            WHERE links.node_id2 != ? AND links.name = ?''',
                         params)
        data = c.fetchall()
        if(data is None or len(data) != 1):
            print("Problem following link!")
            return None

        # Move to the next node, and iterate as many times as required to follow all links
        node_id = data[0][0]

    c = conn.execute('''SELECT path FROM nodes WHERE id = ?''', (node_id,))
    data = c.fetchone()
    if(data is None or len(data) != 1):
        print("Problem getting node path!")
        return None

    # Return the path!
    return data[0]
