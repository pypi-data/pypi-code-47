from abc import ABCMeta, abstractmethod, abstractproperty


def either(v1, v2):
    return lambda op: op(v1) or op(v2)


class HeapBase(object):
    __metaclass__ = ABCMeta
    """Heap:

    Binary Tree with following properties:
    1) Parent is always less in value than children
    2) has height of log(N) (base 2)
    Has a heap that, by convention, has a initialization of [0]
    Also stores a current_size that is initialized at 0
    """

    def __init__(self, isMin=True, key=None):
        """constructor for heap

        Initializes the heap with [0] and the current_size at 0
        Also initializes the key() function for accessing the value for
        which the heap is built

        Keyword Arguments:
            key {function reference} -- functions accesses the value for
            which the heap is built. If it's None, then it looks at the
            array value itself. If the array holds objects with values inside,
            the function should access those values
            within the object (default: {None})
        """
        super().__init__()  # for multi-inheritance
        self.current_size = 0
        self.key = key
        self.isMin = isMin
        self.heap = [0]

    def __str__(self):
        return self.tree()

    def __len__(self):
        return len(self.heap) - 1

    def __iter__(self):
        heapCopy = self.heap[:]
        currSize = self.current_size
        while len(self.heap) > 1:
            yield self.deleteMin()
        self.heap = heapCopy
        self.current_size = currSize

    def tree(self):
        n = len(self.heap)
        res = ""
        if n > 1:
            sHeap = list(map(lambda c: str(c), self.heap))
            longest = max(list(map(lambda y: len(y), sHeap)))
            current_level = [1]
            gap = longest * ' '
            while current_level:
                res += gap.join(str(self.heap[x])
                                for x in current_level) + "\n"
                next_level = []
                for node in current_level:
                    if 2 * node < n:
                        next_level.append(2 * node)
                    if 2 * node + 1 < n:
                        next_level.append(2 * node + 1)
                current_level = next_level
        return res

    @abstractproperty
    def key(self):
        """key getter

        Decorators:
            abstractproperty
        """
        return "should never see this"

    @key.setter
    def key(self, key):
        """Setter for key function

        Implemented in subclasses

        Decorators:
            key.setter

        Arguments:
            key {function} -- function that gives the basis for building heap
        """
        return

    def applyKey(self, val):
        try:
            return self.key(val)
        except ValueError as e:
            print(e)

    def ordering(self, v1, v2):
        """ordering operator for heap
        Depends on the value of {self.isMin}
        """
        if self.isMin:
            return v1 < v2
        return v1 > v2

    @abstractmethod
    def swapOrientation(self):
        pass

    @abstractmethod
    def insert(self, value):
        """[inserts a value into the heap]

        [appends at the end and then restores the
        heap property by comaring parent and child]

        Arguments:
            value {int/object} -- [value/object to be inserted in heap array]
        """
        pass

    @abstractmethod
    def swap(self, i1, i2):
        """[swaps the elements of the heap]

        [at indices i1 and i2]

        Arguments:
            i1 {int} -- [index of first element]
            i2 {int} -- [index of second element]
        """
        n = len(self.heap)
        if max(i1, i2) >= n or either(i1, i2)(lambda x: x < 0):
            raise IndexError("Indices cannot be greater that len(heap) or <0")
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    @abstractmethod
    def restoreHeap(self, size):
        """
        restores min heap property (use only for insert)
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def bubbleUp(self, index):
        """[Used for deleting arbitrary value]

        [
        When deleting, we swap last valuewith the value being deleted.
        Use this to bring the largest(smallest) to the top. The next function
        would then restore its rightful place in the heap
        ]

        Arguments:
            index {int} -- [index where you want the value bubbled up]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def getMin(self):
        raise NotImplementedError("Method has not been implemented")
    @abstractmethod
    def deleteMin(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def deleteMax(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def bubbleDown(self, i):
        """[restores min heap property by 'bubbling down' larger elements]

        [
        Compares the smallest child to the current parent until
        the parent is the smallest
        There is a recursive version below also
        ]

        Arguments:
            i {int} -- [index to start bubbling down]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def getSmallestChild(self, i):
        """[gets the smallest child of the parent node]

        [
        The function where this function is actually called
        makes sure that 2*i < current_size so this function only considers
        the case until 2*i + 1 <  current_size.
        Basically compares the parent with child nodes and finds the
        smallest one of the three
        ]

        Arguments:
            i {int} -- [index of parent node]

        Returns:
            number -- [index of smallest of the three -> could be parent]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def getLargestChild(self, i):
        """[gets the smallest child of the parent node]

        [
        The function where this function is actually called i makes sure
        that 2*i < current_size so this function only considers the case
        until 2*i + 1 <  current_size.
        Basically compares the parent with child nodes and finds the smallest
        one of the three
        ]

        Arguments:
            i {int} -- [index of parent node]

        Returns:
            number -- [index of smallest of the three -> could be parent]
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def buildHeap(self, array, key=None):
        """
        @brief      Builds a heap.

        @param      self   The object
        @param      array  The array

        @return     The heap.
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def satisfyMinHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def satisfyMaxHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        raise NotImplementedError("Method has not been implemented")

    @abstractmethod
    def HeapSort(self, reverse=True):
        """
        @brief      { function_description }

        @param      self     The object
        @param      reverse  If true sorted in descending order

        @return     { sorted array }
        """
        # return None instead of an error as this method should not
        # be necessary
        return None

    @abstractmethod
    def reconstructHeap(self, key):
        """Reconstructs the heap by changing the key for which the heap is
        built

        Decorators:
            abstractmethod

        Arguments:
            key {function} --
            [function that returns a value that is the basis for how the heap
            is built]
        """
        raise NotImplementedError("Method has not been implemented")
