# This class is used to create a pythoon representation of nested sets,
# a data structure used in relational databases which has fast reads and slow
# inserts. This allows custom functions to be called on the nodes.

class NestedSet(object):
    """
    This is a nested set that is used to model nested sets of relational
    databases. The callback here is a function that one can perform on nodes as the
    nested set is created. This can apply a function to the nodes that are strictly
    between a parent node.
    """
    def __init__(self, callback=None):
        self.callback = callback
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __traverse(self, node, func):
        # traverses the nested set and performs a func on the node
        if not node:
            return
        if node.is_leaf:
            func(node)
            return
        self.__traverse(node.left_node, func)
        func(node)
        self.__traverse(node.middle_node, func)
        self.__traverse(node.right_node, func)

    def add(self, node_data):
        # add root node if it doesn't exist
        node = Node(**node_data)
        if not self.root:
            self.root = node
            return

        # add a node to the set
        def add_node(curr_node, parent, node_to_be_added, path):
            if not curr_node:
                setattr(parent, path, node_to_be_added)
            elif node_to_be_added.left > curr_node.left and node_to_be_added.right < curr_node.right:
                # case 1: it's in between, so we perform the callback (update counts) and continue to insert
                if self.callback:
                    self.callback(curr_node, node_to_be_added)
                add_node(curr_node.middle_node, curr_node, node_to_be_added, 'middle_node')
            elif node_to_be_added.left > curr_node.right:
                # case 2: strictly greater
                add_node(curr_node.right_node, curr_node, node_to_be_added, 'right_node')
            elif node_to_be_added.right < curr_node.left:
                # case 3: strictly less
                add_node(curr_node.left_node, curr_node, node_to_be_added, 'left_node')
            else:
                # this should never happen
                raise ValueError('The left and right are messed up')

        add_node(self.root, None, node, None)
        self.size += 1

    def as_list(self):
        # returns the nested set, in order, as a list
        results = []
        self.__traverse(self.root, lambda node: results.append(dict(node)))
        return results

    def print_ns(self):
        # prints the entire nested set, starting from root
        self.__traverse(self.root, print)


class Node(object):
    '''
    Represents one "set" or "node" in a nested set. These nodes have
    the following properties:
        - left - an integer representing its position_left
        - right - an integer representing its position_right
        - value - can be any python data type or object.

    The pointers to other nodes are left_node, middle_node and right_node.
    This is what creates the actual nested set structure.
    '''
    attributes = ['left', 'right', 'value']

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        self.left_node = None
        self.middle_node = None
        self.right_node = None

    def __repr__(self):
        return 'Left: {0}, Right: {1}, Value: {2}'.format(self.left, self.right, self.value)

    def __iter__(self):
        for prop in self.attributes:
            yield (prop, getattr(self, prop, None))

    @property
    def is_leaf(self):
        return not self.left_node and not self.right_node and not self.middle_node
