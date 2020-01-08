#                                                       /`-
# _                                  _   _             /####`-
# | |                                | | (_)           /########`-
# | |_ _ __ __ _ _ __  ___  ___ _ __ | |_ _ ___       /###########`-
# | __| '__/ _` | '_ \/ __|/ _ \ '_ \| __| / __|   ____ -###########/
# | |_| | | (_| | | | \__ \  __/ | | | |_| \__ \  |    | `-#######/
# \__|_|  \__,_|_| |_|___/\___|_| |_|\__|_|___/  |____|    `- # /
#
# Copyright (c) 2019 transentis labs GmbH

import xmltodict
from collections import OrderedDict
from copy import deepcopy

try:
    from ...parsers.smile.grammar import SMILEVisitor, grammar
    from ...plugins import sanitizeName
    from ...plugins import makeExpressionAbsolute
except:
    from parsers.smile.grammar import SMILEVisitor, grammar
    from plugins import sanitizeName, makeExpressionAbsolute


def extract_connects(model_name, connects_raw):

    connects = {}
    if type(connects_raw) == OrderedDict:
        to_ = connects_raw["@to"] if not "." in connects_raw["@to"] else model_name + "." + connects_raw["@to"]
        from_ = connects_raw["@from"] if not "." in connects_raw["@from"] else model_name + "." + connects_raw["@from"]

        return {sanitizeName(to_.lower()): sanitizeName(from_.lower())}

    elif type(connects_raw) == list:
        for connect in connects_raw:
            to_ = connect["@to"] if not "." in connect["@to"] else model_name + "." + connect["@to"]
            from_ = connect["@from"] if not "." in connect["@from"] else model_name + "." + connect["@from"]
            connects[(sanitizeName(to_.lower()) )] =  sanitizeName(from_)

    return connects


def make_name_absolute(model_name, name):
    seperator = "."
    if "." not in name:
        return model_name + seperator + name
    else:
        return name





def parse_entity(entity, model_name):
    gf = []
    event_poster = []  # if not "event_poster" in entity.keys() else entity["event_poster"]

    if "gf" in entity.keys():

        gf_ = entity["gf"]
        ypoints = [float(x) for x in gf_["ypts"].split(",")]
        xpoints = []
        if not "xpts" in gf_.keys():

            minX = float(gf_["xscale"]["@min"])
            maxX = float(gf_["xscale"]["@max"])

            for k in range(0, len(ypoints)):
                xpoints += [minX + k * (maxX - minX) / (len(ypoints) - 1)]

        else:
            xpoints = [float(x) for x in gf["xpts"].split(",")]

        gf = list(zip(xpoints, ypoints))

    non_negative = True if "non_negative" in entity.keys() else False
    inflows = []
    outflows = []
    doc = None if not "doc" in entity.keys() else entity["doc"]

    if "inflow" in entity.keys():
        inflows += [sanitizeName(make_name_absolute(model_name, entity["inflow"]))] if type(
            entity["inflow"]) is str else [sanitizeName(make_name_absolute(model_name, x)) for x in entity["inflow"]]

    if "outflow" in entity.keys():
        outflows += [sanitizeName(make_name_absolute(model_name, entity["outflow"]))] if type(
            entity["outflow"]) is str else [sanitizeName(make_name_absolute(model_name, x)) for x in entity["outflow"]]

    if "@name" in entity.keys():
        if not "." in entity["@name"]:
            entity["@name"] = model_name + "." + entity["@name"].lower()

    connects = {} if not "connect" in entity.keys() else extract_connects(model_name, entity["connect"])
    name = "" if not "@name" in entity.keys() else sanitizeName(entity["@name"])

    access = "" if not "@access" in entity.keys() else entity["@access"]
    equation = [] if not "eqn" in entity.keys() else entity["eqn"]

    dimensions = []
    labels = []


    if "dimensions" in entity.keys():

        dims = entity["dimensions"]["dim"] if type(entity["dimensions"]["dim"]) is list else [entity["dimensions"]["dim"]]
        if dims and "element" in entity.keys():

            for elem in entity["element"]:
                label = tuple([sanitizeName(x) for x in elem["@subscript"].split(",")])
                labels += [label]


        for dim in dims:
            dimensions+= [sanitizeName(dim["@name"])]

    ## Parse Equations again if we find out there are arrayed Equations!
    if len(labels) > 0:
        equation = []
        for elem in entity["element"]:
            equation += [elem["eqn"]]

    return {"name": name, "access": access, "equation": [equation] if type(equation) is str else equation, "connects": connects, "non_negative": non_negative,
            "inflow": inflows, "outflow": outflows, "doc": doc, "gf": gf, "event_poster": event_poster,"dimensions": dimensions,"labels":labels}


def get_entities(entity_type, model):
    entities = []

    model_name = "" if not "@name" in model.keys() else model["@name"]

    if entity_type in model["variables"].keys():

        if type(model["variables"][entity_type]) == OrderedDict:  # One entity in Model
            entity = model["variables"][entity_type]
            entities += [parse_entity(entity, model_name)]

        elif type(model["variables"][entity_type]) == list:
            for entity in model["variables"][entity_type]:  # For each entity
                entities += [parse_entity(entity, model_name)]

    return entities


def parse_xmile(filename):
    with open(filename, "r") as infile:
        xml_string = infile.read()
        document = xmltodict.parse(xml_string)

    ## Specs
    specs = document["xmile"]["sim_specs"]
    header = document["xmile"]["header"]

    ## DT
    try:
        if "@reciprocal" in specs["dt"].keys() and specs["dt"]["@reciprocal"].lower() == 'true': ## Reciprocal values
            specs["dt"] = 1 / int(specs["dt"]["#text"])
        else: ## Not reciprocal
            specs["dt"] = specs["dt"]["#text"]
    except:
        pass

    specs["method"] = deepcopy(specs["@method"])
    specs["units"] = deepcopy(specs["@time_units"])
    specs.pop("@method")
    try:
        dimensions = document["xmile"]["dimensions"]
    except:
        dimensions = {}

    IR = {
        "dimensions": {},
        "models": {},  # document["xmile"]["model"],
        "specs": dict(specs),
        "name": header["name"], "assignments": {}
    }

    ## DIMENSIONS
    if "dim" in dimensions.keys():
        dims = dimensions["dim"] if type(dimensions["dim"]) is list else [dimensions["dim"]]

        for dim in dims:
            size =  None if not "@size" in dim.keys() else int(dim["@size"])
            name = sanitizeName(dim["@name"])
            labels = None

            if not size:
                labels = [sanitizeName(elem["@name"]) for elem in dim["elem"]]
            else:
                labels = [str((i+1)) for i in range(0,size)]

            IR["dimensions"][sanitizeName(dim["@name"])] = {
                "size": size,
                "name": name, "labels": labels, "variables": []}



    ## ENTITIES
    visitor = SMILEVisitor()
    table = []

    models = document["xmile"]["model"] if type(document["xmile"]["model"]) is list else [document["xmile"]["model"]]

    for model in models:
        name = "" if not "@name" in model.keys() else model["@name"]
        variables = {} if not "variables" in model.keys() else model["variables"]
        entities = {}

        for entity_type in variables.keys():
            entities[entity_type] = get_entities(entity_type, model)

            '''
            Parse all arrayed variables
            '''
            if entity_type.lower() in ["stock","aux","array","flow"]:
                for entity in entities[entity_type]:
                    if entity["dimensions"]:
                        variable = entity["name"]
                        dimensions = [entity["dimensions"] ] if not type(entity["dimensions"]) is list else entity["dimensions"]
                        for dim in dimensions:
                            IR["dimensions"][dim]["variables"] += [{"model":name,"name":variable}]


        IR["models"][name] = {"name": name, "entities": entities}

        for key, value in entities.items():
            for elem in value:
                connects = elem["connects"]

                IR["assignments"].update({k:v for k,v in connects.items()})


        table += [[name, 0 if not "stock" in entities.keys() else len(entities["stock"]),
                   0 if not "aux" in entities.keys() else len(entities["aux"]),
                   0 if not "flow" in entities.keys() else len(entities["flow"])]]

    ### PARSE EQUATIONS
    for name, model in IR["models"].items():
        for entity_type, entity in model["entities"].items():
            for elem in entity:

                try:
                    elem["equation_parsed"] = [makeExpressionAbsolute(name,visitor.visit(grammar.parse(x)),connects=IR["assignments"]) for x in elem["equation"]]
                except Exception as e:
                    print("Error parsing: {}".format(elem["equation"]))
                    raise e

                # Handle Non-Negative
                if elem["non_negative"]:
                    if type(elem["equation_parsed"]) is float:
                        elem["equation_parsed"] = max(0, elem["equation_parsed"])
                    else:
                        elem["equation_parsed"] = {"name": 'max', "type": 'call',
                                                   "args": [0, deepcopy(elem["equation_parsed"])]}

    return IR
