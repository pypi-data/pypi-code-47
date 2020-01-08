import json

import necxxt.repositories
import necxxt.utils


def resolveDepency(name, version):
    return necxxt.repositories.resolveRepository(name, version)


def getResolvedDependencies(graph):
    resolved = []

    if graph.get("requires", False):
        dependencies = graph["dependencies"].keys()
        for dependency in dependencies:
            if "resolved" in dependencies[dependency]:
                resolved.append(dependency)

    return resolved


def areAllDependenciesResolved(graph):
    if graph.get("requires", False):
        dependencies = graph["dependencies"].keys()
        resolved_dependencies = 0
        for dependency in dependencies:
            if "resolved" in dependencies[dependency]:
                resolved_dependencies += 1

        return resolved_dependencies == len(dependencies)

    return False


def installDependencies():
    graph = {}

    module = necxxt.utils.readModule()

    graph["name"] = module["name"]
    graph["version"] = module["version"]
    graph["lockfileVersion"] = 1

    if not "dependencies" in module:
        return graph

    graph["requires"] = True
    graph["dependencies"] = {}

    dependencies = list(module["dependencies"].items())
    i = 0
    while i < len(dependencies):
        dependency, version = dependencies[i]
        if dependency not in graph["dependencies"]:
            graph["dependencies"][dependency] = {
                "version": version
            }

            resolved = resolveDepency(dependency, version)
            if resolved:
                graph["dependencies"][dependency]["resolved"] = str(resolved)
                resolved.install()

                m = resolved.readLocalModule()
                requires = m.get("dependencies")
                if requires:
                    graph["dependencies"][dependency]["requires"] = requires

                    for d, v in requires.items():
                        if not d in graph["dependencies"]:
                            dependencies.append((d, v,))

        i += 1

    with open("necxxt-lock.json", "w") as f:
        json.dump(graph, f, indent=4)

    return graph
