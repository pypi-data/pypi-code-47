from pineapple_core.core.node import get_whole_scenario


def analyse_scenario(sequence):
    scenario = get_whole_scenario(sequence)
    all_contained_nodes = []
    if hasattr(sequence, "__sequence_steps"):
        all_contained_nodes += [
            node for step in sequence.__sequence_steps for node in step.nodes.values()
        ]
    if hasattr(sequence, "__failure_node_container"):
        all_contained_nodes += [
            node for node in sequence.__failure_node_container.nodes.values()
        ]
    if hasattr(sequence, "__global_nodes_container"):
        all_contained_nodes += [
            node for node in sequence.__global_nodes_container.nodes.values()
        ]
    all_contained_nodes.append(sequence)
    print("Running static analysis on the scenario")
    check_unreferenced_nodes(scenario, all_contained_nodes)
    check_for_dangling_inputs(scenario)
    for node in scenario:
        check_for_empty_inputs(node)
        check_for_naming_conventions(node)


def check_unreferenced_nodes(scenario, all_nodes):
    for node in all_nodes:
        if node not in scenario:
            print(
                f"[WARNING] Node {node} is not connected to any Node and can't be triggered"
            )
    for node in scenario:
        if node not in all_nodes:
            print(f"[WARNING] Usage of {node} outside of steps")


def count_references_of_node_in_flows(scenario, search_node):
    count = 0
    for node in scenario:
        for flow in node.flows:
            if flow.node == search_node:
                count += 1
    return count


def count_references_of_node_in_inputs(scenario, search_node):
    count = 0
    for node in scenario:
        for node_input in node.inputs:
            if node_input.connected_output and node_input.connected_output.node == search_node:
                count += 1
    return count


def check_for_dangling_inputs(scenario):
    for node in scenario:
        for node_input in node.inputs.values():
            connected_output = node_input.connected_output
            if (
                connected_output
                and connected_output.node
                and count_references_of_node_in_flows(scenario, connected_output.node)
                == 0
                and not connected_output.node.autotrigger
            ):
                print(
                    f"[WARNING] Node {connected_output.node} "
                    f"is never triggered nor autotriggerable (needed by {node})"
                )


def check_for_untriggerable_nodes(scenario):
    for node in scenario:
        if node.trigger_log["trigger"] != 0:
            pass
        elif node.autotrigger:
            if (
                count_references_of_node_in_inputs(scenario, node) == 0
                and count_references_of_node_in_flows(scenario, node) == 0
            ):
                print(
                    f"[WARNING] Node {node} is autotriggerable"
                    " but is not used as input or connected to any flow"
                )
        elif count_references_of_node_in_flows(scenario, node) == 0:
            print(
                f"[WARNING] Node {node} is not autotriggerable and is never connected to any flow"
            )


def check_for_naming_conventions(node):
    if str(node.id).endswith("_node"):
        print(f"[WARNING] A Node instance shouldn't end with _node (on {node.id})")


def check_for_empty_inputs(node):
    for node_input in node.inputs.values():
        if (
            node_input.value is None
            and node_input.connected_output is None
            and node_input.name != "self"
            and not node_input.optional
        ):
            print(f"[WARNING] Node '{node}' has empty NodeInput '{node_input}'")
