# @Time    : 2018/12/17 20:46
# @Author  : Niyoufa
from collections import deque, OrderedDict


class _AttributeHolder(object):
    """Abstract base class that provides __repr__.

    The __repr__ method returns a string in the format::
        ClassName(attr=name, attr=name, ...)
    The attributes are determined either by a class-level attribute,
    '_kwarg_names', or by inspecting the instance __dict__.
    """

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        star_args = {}
        for arg in self._get_args():
            arg_strings.append(repr(arg))
        for name, value in self._get_kwargs():
            if name.isidentifier():
                arg_strings.append('%s=%r' % (name, value))
            else:
                star_args[name] = value
        if star_args:
            arg_strings.append('**%s' % repr(star_args))
        return '%s(%s)' % (type_name, ', '.join(arg_strings))

    def _get_kwargs(self):
        return sorted(self.__dict__.items())

    def _get_args(self):
        return []


class Context(_AttributeHolder):
    """Simple object for storing attributes.

    Implements equality by attribute names and values, and provides a simple
    string representation.
    """

    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def init_from_dict(self, data):
        if self.__dict__:
            raise TypeError("object has init")
        if not isinstance(data, dict):
            raise TypeError("data must be dict")
        for k, v in data.items():
            setattr(self, k, v)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item, None)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __eq__(self, other):
        if not isinstance(other, Context):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__

    def pop(self, k):
        return self.__dict__.pop(k)


class Graph(object):

    def __init__(self, vertices, edges, start_vertex):
        self.vertices = vertices
        self.edges = edges
        self.start_vertex = start_vertex
        self.vertex_dict = {}
        for vertex in self.vertices:
            vertex["in_degree"] = 0
            vertex["out_degree"] = 0
            self.vertex_dict[vertex["_id"]] = vertex
        self.edge_dict = {}
        for edge in self.edges:
            self.edge_dict[edge["_id"]] = edge

        # 邻接表
        self.neighbor_table = self.get_neighbor_table()
        # 邻接矩阵
        self.adjacency_matrix = self.get_adjacency_matrix()

    def get_neighbor_table(self):
        """
        获取图的邻接表
        :return:
        """
        neighbor_table = {}
        for vertex in self.vertices:
            neighbor_table[vertex["_id"]] = []

        for edge in self.edges:
            neighbor_table[edge["_from"]].append(self.vertex_dict[edge["_to"]]["_id"])
            if "in_degree" in self.vertex_dict[edge["_to"]]:
                self.vertex_dict[edge["_to"]]["in_degree"] += 1
            else:
                self.vertex_dict[edge["_to"]]["in_degree"] = 1
            if "out_degree" in self.vertex_dict[edge["_to"]]:
                self.vertex_dict[edge["_from"]]["out_degree"] += 1
            else:
                self.vertex_dict[edge["_from"]]["out_degree"] = 1

        return neighbor_table

    def display_neighbor_table(self):
        for k, v in self.neighbor_table.items():
            node = self.vertex_dict.get(k)
            print(node["name"], node)
            print("{} {}".format(k, node["name"]),
                  ["{} {}".format(node_id, self.vertex_dict.get(node_id)["name"]) for node_id in v ])

    def get_adjacency_matrix(self):
        """
        获取图的邻接矩阵
        :return:
        """
        pass

    def bfs(self, node=None):
        """
        条件广度优先搜索
        """
        # parents 记录所有可达节点与对应的父节点，这里是一个字典，我们将其 可达节点 作为 key，而将其 父节点 作为 value
        # query_queue 是用来存放待探索节点的 to-do 列表，这里是一个 FIFO
        node = node or self.start_vertex["_id"]
        parents, query_queue = OrderedDict({node: None}), deque([node])

        while query_queue:
            # 总是从 FIFO 的左侧弹出待探索的节点
            q_node = query_queue.popleft()
            for neighbor in self.neighbor_table[q_node]:
                neighbor_id = neighbor["_id"]
                if neighbor_id in parents:
                    continue

                # 记录探索到的邻居节点及其父节点
                parents[neighbor_id] = q_node

                # 将其邻居节点推入 to-do 列表
                query_queue.append(neighbor_id)
        print("->".join(parents.keys()))
        return parents
