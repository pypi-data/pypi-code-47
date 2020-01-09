import inspect
import os

TEMPLATES_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    ),
    "templates",
)

_VALID_MATCHES = list(filter(lambda x: x.endswith(".rst"), os.listdir(TEMPLATES_DIR)))


def load(name):
    if not name.endswith(".rst"):
        name += ".rst"

    if name not in _VALID_MATCHES:
        raise ValueError("Unrecognised template: %s" % name)

    with open(os.path.join(TEMPLATES_DIR, name)) as f:
        contents = f.read()

    return contents


def _tab_indented_object_block(objects):
    block = "\n\t".join(objects)
    # return "\t" + block
    return block


def _header_break(name):
    return "".join(["=" for _ in range(len("``" + name + "``"))])


def make_subpkg_overview(name):
    header_break = _header_break(name)
    return load("subpkg_overview").format(header_break=header_break, name=name)


def make_classes_overview(dirname, classes):
    classes_block = _tab_indented_object_block(classes)
    return load("classes_overview").format(dirname=dirname, classes=classes_block)


def make_single_class_overview(name):
    return load("single_class_overview").format(name=name)


def make_functions_section(functions):
    functions_block = _tab_indented_object_block(functions)
    return load("functions_section").format(functions=functions_block)


def make_properties_section(properties):
    properties_block = _tab_indented_object_block(properties)
    return load("properties_section").format(properties=properties_block)


def make_methods_section(methods, constructor=None):
    methods_block = _tab_indented_object_block(methods)

    if constructor is not None:
        constructor_block = "\n\t%s" % constructor
    else:
        constructor_block = ""

    return load("methods_section").format(
        constructor=constructor_block, methods=methods_block
    )


def make_simplemod_header(
    name, modname, cls_name, cls_props, cls_methods, cls_init, functions
):
    header_break = _header_break(name)

    if cls_name is not None:
        class_overview = make_single_class_overview(cls_name)
    else:
        class_overview = ""

    if cls_props:
        prop_section = make_properties_section(cls_props)
    else:
        prop_section = ""

    if cls_methods:
        if cls_init is not None:
            constructor = "%s.%s" % (cls_name, cls_init)
        else:
            constructor = None

        meth_section = make_methods_section(cls_methods, constructor)
    else:
        meth_section = ""

    functions_section = make_functions_section(functions)

    return load("simplemod_header").format(
        header_break=header_break,
        name=name,
        module_name=modname,
        class_overview=class_overview,
        class_properties=prop_section,
        class_methods=meth_section,
        functions=functions_section,
    )


def make_singleclass_header(name, modname, cls_name, cls_props, cls_methods, cls_init):
    header_break = _header_break(name)

    class_overview = make_single_class_overview(cls_name)

    if cls_props:
        prop_section = make_properties_section(cls_props)
    else:
        prop_section = ""

    if cls_methods:
        if cls_init is not None:
            constructor = "%s.%s" % (cls_name, cls_init)
        else:
            constructor = None

        meth_section = make_methods_section(cls_methods, constructor)
    else:
        meth_section = ""

    return load("singleclass_header").format(
        header_break=header_break,
        name=name,
        module_name=modname,
        class_overview=class_overview,
        class_properties=prop_section,
        class_methods=meth_section,
    )


def make_multiclass_header(name, modname, classes_dirname, classes, functions):
    header_break = _header_break(name)

    classes_overview = make_classes_overview(classes_dirname, classes)

    functions_section = make_functions_section(functions)

    return load("multiclass_header").format(
        header_break=header_break,
        name=name,
        module_name=modname,
        classes_overview=classes_overview,
        functions=functions_section,
    )
