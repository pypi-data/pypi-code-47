import collections


class Ordered(collections.MutableSequence):
    def __init__(self, lst=[], key=None, reverse=False):
        if type(lst) != list:
            raise TypeError("Only list can be provided as argument.")

        self._container = lst

        if reverse:
            self._cmp = lambda a, b: a >= b
        else:
            self._cmp = lambda a, b: a <= b

        if key:
            self._key = key
        else:
            self._key = lambda a: a

        self._container.sort(key=key, reverse=reverse)

    def __repr__(self):
        return f"[{', '.join([str(item) for item in self._container])}]"

    def __getitem__(self, index):
        self._container.__getitem__(index)

    def __setitem__(self, index, value):
        if index >= len(self._container):
            index = len(self._container) - 1

        if (
            index > 0
            and self._cmp(self._key(self._container[index - 1]), self._key(value))
            and self._key(self._container[index - 1]) != self._key(value)
        ):
            raise IndexError(
                f"Can not insert smaller value after element with bigger value. {self._container[index-1]} > {value}"
            )
        if (
            index < len(self._container) - 2
            and self._cmp(self._key(self._container[index + 1]), self._key(value))
            and self._key(self._container[index - 1]) != self._key(value)
        ):
            raise IndexError(
                f"Can not insert bigger value before element with smaller value. {self._container[index+1]} < {value}"
            )

        self._container.__setitem__(index, value)

    def __delitem__(self, index):
        self._container.__delitem__(index)

    def __len__(self):
        return self._container.__len__()

    def extend(self, lst):
        if type(lst) != list:
            raise TypeError("Only list can be provided as argument.")

        for value in lst:
            self._container.append(value)

    def index(self, value):
        return self._bin_search(0, len(self._container), value)

    def last_index(self, value):
        idx = self._bin_search(0, len(self._container), value)
        if idx == -1:
            return idx

        while self._key(self._container[idx]) == self.key(value):
            idx = idx + 1
        return idx - 1

    def all_indecies(self, value):
        first_index = self.index(value)
        if first_index == -1:
            return []

        last_index = self.last_index(value)

        return first_index, last_index

    def insert(self, index, value):
        if index >= len(self._container):
            index = len(self._container) - 1

        if self._cmp(self._key(value), self._key(self._container[index])):
            self._container.insert(index, value)
        else:
            raise IndexError(
                f"Can not insert bigger value before element with smaller value. {self._container[index]} < {value}"
            )

    def __iter__(self):
        return self._container.__iter__()

    def append(self, value):
        if len(self._container) and self._cmp(
            self._key(value), self._key(self._container[0])
        ):
            self._container.insert(0, value)
        elif len(self._container) and self._cmp(
            self._key(self._container[-1]), self._key(value)
        ):
            self._container.append(value)
        else:
            idx = self._bin_search_index(0, len(self._container), value)
            self._container.insert(idx, value)

    def __eq__(self, other):
        if type(other) == list:
            return self._container.__eq__(other)

        if type(other) != Ordered:
            raise TypeError(
                f"Can not compare object of type orderedpy.Ordered with {type(other)}"
            )
        return self._container.__eq__(other._container)

    def __le__(self, other):
        if type(other) == list:
            return self._container.__le__(other)

        if type(other) != Ordered:
            raise TypeError(
                f"Can not compare object of type orderedpy.Ordered with {type(other)}"
            )
        return self._container.__le__(other._container)

    def __ge__(self, other):
        if type(other) == list:
            return self._container.__ge__(other)

        if type(other) != Ordered:
            raise TypeError(
                f"Can not compare object of type orderedpy.Ordered with {type(other)}"
            )
        return self._container.__ge__(other._container)

    def _bin_search_index(self, lhs, rhs, value):
        if lhs < rhs:
            mid = (lhs + rhs) // 2

            if self._cmp(
                self._key(self._container[mid]), self._key(value)
            ) and self._cmp(self._key(value), self._key(self._container[mid + 1])):
                return mid
            elif self._cmp(
                self._key(self._container[mid]), self._key(value)
            ) and self._cmp(self._key(self._container[mid + 1]), self._key(value)):
                return self._bin_search_index(mid + 1, rhs, value)
            else:
                return self._bin_search_index(lhs, mid - 1, value)
        return 0

    def _bin_search(self, lhs, rhs, value):

        if lhs < rhs:
            mid = (lhs + rhs) // 2
            if self._key(self._container[mid]) == self._key(value):
                return mid
            elif self._cmp(self._key(self._container[mid]), self._key(value)):
                return self._bin_search(mid + 1, rhs, value)
            else:
                return self._bin_search(lhs, mid - 1, value)
        return -1
