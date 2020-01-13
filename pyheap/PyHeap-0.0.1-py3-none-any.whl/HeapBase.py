from abc import ABCMeta, abstractmethod, abstractproperty


class HeapBase(object):
    __metaclass__ = ABCMeta
    """Heap:

    Binary Tree with following properties:
    1) Parent is always less in value than children
    2) has height of log(N) (base 2)
    Has a heap that, by convention, has a initialization of [0]
    Also stores a current_size that is initialized at 0
    """

    def __init__(self, arr=None, isMin=True, key=None):
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
        if not arr:
            self.heap = [0]
        else:
            self.buildHeap(arr, key)

    def __str__(self):
        return self.tree()

    def tree(self):
        sHeap = list(map(lambda c: str(c), self.heap))
        longest = max(list(map(lambda y: len(y), sHeap)))
        n = len(self.heap)
        res = ""
        current_level = [1]
        gap = longest * ' '
        while current_level:
            res += gap.join(
                str(self.applyKey(self.heap[x])) for x in current_level) + "\n"
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
        return self.key(val)

    def ordering(self, v1, v2):
        """ordering operator for heap
        Depends on the value of {self.isMin}
        """
        if self.isMin:
            return v1 < v2
        return v1 > v2

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
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    @abstractmethod
    def restoreHeap(self, size):
        """
        restores min heap property (use only for insert)
        """
        pass

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
        pass

    @abstractmethod
    def deleteMin(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        pass

    @abstractmethod
    def deleteMax(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        Returns:
            [int] -- [value deleted from heap]
        """
        pass

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
        pass

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
        pass

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
        return

    @abstractmethod
    def buildHeap(self, array, key=None):
        """
        @brief      Builds a heap.

        @param      self   The object
        @param      array  The array

        @return     The heap.
        """
        self.key = key
        index = len(array) // 2
        self.current_size = len(array)
        self.heap = [0] + array
        while (index > 0):
            self.bubbleDown(index)
            index -= 1

    @abstractmethod
    def satisfyMinHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        pass

    @abstractmethod
    def satisfyMaxHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        pass

    @abstractmethod
    def HeapSort(self, reverse=True):
        """
        @brief      { function_description }

        @param      self     The object
        @param      reverse  If true sorted in descending order

        @return     { sorted array }
        """
        return

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
        pass


if __name__ == '__main__':
    """
    main block to execute tests
    """
    test = [1, 5, 3, 4, 6, 7, 5, 3]
    print(test)
    Heap = HeapBase()
    Heap.buildHeap(test)
    print(Heap.heap)
    sorted_arr = Heap.HeapSort()
    print(sorted_arr)
