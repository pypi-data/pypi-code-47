
# -- Autogenerate documentation for event schemas ------------------

from notebook.utils import get_schema_files

# Create an events directory if it doesn't exist.
if not os.path.exists('events'):
    os.makedirs('events')

# Build a dictionary that describes the event schema table of contents.
# toc = {
#     schema_name : {
#         src: # file path to schema
#         dst: # file path to documentation
#         ver: # latest version of schema
#     }
# }
toc = {}

# Iterate over schema directories and generate documentation.
# Generates documentation for the latest version of each schema.
for file_path in get_schema_files():
    # Make path relative.
    file_path = os.path.relpath(file_path)
    # Break apart path to its pieces
    pieces = file_path.split(os.path.sep)
    # Schema version. Outputs as a string that looks like "v#"
    schema_ver = os.path.splitext(pieces[-1])[0]
    # Strip "v" and make version an integer.
    schema_int = int(schema_ver[1:])
    # Schema name.
    schema_name = pieces[-2]

    # Add this version file to schema_dir
    src = '../' + file_path
    dst = os.path.join('events', os.path.join(schema_name + '.rst'))

    if schema_name in toc:
        # If this is a later version, replace the old version.
        if schema_int > toc[schema_name]['ver']:
            toc[schema_name] = {
                'src': src,
                'dst': dst,
                'ver': schema_int
            }
    else:
        toc[schema_name] = {
            'src': src,
            'dst': dst,
            'ver': schema_int
        }

# Write schema documentation
for schema_name, x in toc.items():
    with open(dst, 'w') as f:
        f.write('.. jsonschema:: {}'.format(src))

# Build a table of contents for these schemas.
events_index = """
.. toctree::
   :maxdepth: 1
   :glob:
"""
with open(os.path.join('events', 'index.rst'), 'w') as f:
    f.write(events_index)
    for item in toc.keys():
        f.write('   {}'.format(item))