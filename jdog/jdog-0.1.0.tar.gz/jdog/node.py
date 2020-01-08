import random


class _GroupNode:
    """ Base class for nodes which groups other nodes together.

        :var str begin_token: char to print at the start of group
        :var str end_token: char to print at the end of group
        :var list nodes: Nodes to recursively included within group
    """
    def __init__(self, begin_token, end_token, nodes):
        self.begin_token = begin_token
        self.end_token = end_token
        self.nodes = nodes

    def exec(self):
        """Join nodes together between :attr:`begin_token` and :attr:`end_token`"""
        s = ','.join(str(n.exec()) for n in self.nodes)
        return f'{self.begin_token}{s}{self.end_token}'


class ObjectNode(_GroupNode):
    """
        Represents JSON-Object

        :var list properties: Properties to include within object.
    """
    def __init__(self, properties):
        super().__init__('{', '}', properties)


class ArrayNode(_GroupNode):
    """
        Represents JSON-Array

        :var list properties: Values to include within object.
    """
    def __init__(self, children):
        super().__init__('[', ']', children)


class FuncNode:
    """
        Node accepting function which will be executed later

        :var func f: Function to execute. Has no arguments.
    """
    def __init__(self, f):
        self.f = f

    def exec(self):
        """Executes :attr:`f`"""
        return self.f()


class RangeNode:
    """
        Node which repeatedly creates sub-nodes. Combination of property with array value.

        :var str name: Represents property name which will be generated.
        :var int l: How many times generation runs.
        :var Node child: Object to add to the generated array.
        :var int h: Optional. If specified, generation runs randomly between l (inlcusive) to h (exclusive).
    """
    def __init__(self, name, l, child, h=None):
        self.name = name
        self.low = int(l)
        self.high = int(h) if h else None
        self.child = child

    def exec(self):
        """
            :return: Range representation: JSON property named by :attr:`value` with array value.
            :rtype: str
        """
        children = []
        if self.high is None:
            for i in range(self.low):
                children.append(self.child)
        else:
            for i in range(random.randint(self.low, self.high - 1)):
                children.append(self.child)

        return f'"{self.name}": {ArrayNode(children).exec()}'


class PlaceholderNode:
    """
        Represents node with object

        :var object placeholder: :class:`~jdog.placeholder.placeholder.Placeholder` object to use.
    """
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def exec(self):
        """
            Executes placeholder

        :return: Value returned by placeholder
        """
        return self.placeholder.exec()


class PropertyNode:
    """
        Represent JSON property with name and value

        :var Node name: Property name
        :var Node child: Property value
    """
    def __init__(self, name, child):
        self.name = name
        self.child = child

    def exec(self):
        """
            Executes name node and child if present.
            :return: Property representation
        """
        if self.child:
            return f'{self.name.exec()}:{self.child.exec()}'
        else:
            return f'{self.name.exec()}:""'


class ScalarNode:
    """
        Represents scalar value - that is any number or any arbitrary string

        :var str|number value: Scalar value
    """
    def __init__(self, value):
        self.value = value

    def exec(self):
        """
            If value is string - return as JSON string value otherwise as is
            :return: Value enclosed as a string or as is
        """
        if isinstance(self.value, str):
            return f'"{self.value}"'
        else:
            return self.value
