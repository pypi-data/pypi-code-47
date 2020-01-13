from HeapBase import HeapBase


class Heap(HeapBase):
    """Min Heap:

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
            which the heap is built. If it's None, then it looks at the array
            value itself. If the array holds objects with values inside, the
            function should access those values within the object
            (default: {None})
        """
        super().__init__(isMin, key)  # for multi-inheritance

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if key is None:
            self._key = lambda x: x  # identity function
        else:
            self._key = key

    def insert(self, value):
        """[inserts a value into the heap]

        [appends at the end and then restores the heap
        property by comaring parent and child]

        Arguments:
            value {int/object} -- [value/object to be inserted in heap array]
        """
        self.heap.append(value)
        self.current_size += 1
        self.restoreHeap(self.current_size)

    def deleteVal(self, val):
        """deletes an arbitrary value in heap (if it's there)

        Swaps the last value in heap with the value to be deleted
        Pops the heap and reduces its size
        If the value now in the place of the deleted value has a value less
        than its parent, bubble the index up, else bubbleDown

        Arguments:
            val {int} -- value to be deleted
        """

        index = -1
        for i in range(1, self.current_size + 1):
            if self.key(self.heap[i]) == val:
                index = i
                break

        if index < 0:
            return
        try:
            if index != self.current_size + 1:
                self.swap(index, self.current_size)
                self.current_size -= 1
                self.heap.pop()
                if self.heap[index] < self.heap[index // 2]:
                    self.bubbleUp(index)
                else:
                    self.bubbleDown(index)
            else:
                self.current_size -= 1
                self.heap.pop()

        except NameError as e:
            print("Value not in heap, NameError:", e)

    def restoreHeap(self, size):
        """
        restores min heap property (use only for insert)
        """
        while (size // 2 > 0):
            if self.ordering(
                    self.key(self.heap[size]), self.key(self.heap[size // 2])):
                self.swap(size, size // 2)
                size = size // 2
            else:
                break

    def bubbleUp(self, index):
        """[Used for deleting arbitrary value]

        [
        When deleting, we swap last value (one of the biggest in min heap)
        with the value being deleted.
        Use this to bring the largest to the top. The next function would then
        restore its rightful place in the heap
        ]

        Arguments:
            index {int} -- [index where you want the value bubbled up]
        """
        while index // 2 > 0:
            if self.ordering(
                    self.key(self.heap[index]), self.key(
                        self.heap[index // 2])):
                self.swap(index, index // 2)
                index = index // 2
            else:
                break

    def deleteMin(self):
        """[deletes minimum element from the heap -> the root]

        [replaces it with the last element, then restores heap property]

        NOTE: if a max heap, obviously deletes and returns max element

        Returns:
            [int] -- [value deleted from heap]
        """
        return_val = self.key(self.heap[1])
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.bubbleDown(1)
        return return_val

    def bubbleDown(self, i):
        """[restores min heap property by 'bubbling down' larger elements]

        [
        Compares the smallest child to the current parent until the parent is
        the smallest
        There is a recursive version below also
        ]

        Arguments:
            i {int} -- [index to start bubbling down]
        """
        while (i * 2 <= self.current_size):
            mc = self.getSmallestChild(i)
            if self.ordering(self.key(self.heap[mc]), self.key(self.heap[i])):
                self.swap(i, mc)
                i = mc
            else:
                break

    def getSmallestChild(self, i):
        """[gets the smallest child of the parent node]

        [
        The function where this function is actually called i makes sure that
        2*i < current_size so this function only considers the case until
        2*i + 1 <  current_size.
        Basically compares the parent with child nodes and finds the smallest
        one of the three
        ]

        Arguments:
            i {int} -- [index of parent node]

        Returns:
            number -- [index of smallest of the three -> could be parent]
        """
        # don't have to worry about 2*i being larger as this function wouldn't
        # be called
        if (2 * i + 1 > self.current_size):
            return 2 * i
        else:
            smallest = 2 * i
            if self.ordering(
                    self.key(self.heap[2 * i + 1]),
                    self.key(self.heap[smallest])):
                smallest = 2 * i + 1
            return smallest

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

    def satisfyMinHeapProperty(self, index, current_size):
        """
        @brief      recursive func satisfying min heap property

        @param      self          The object
        @param      index         The index
        @param      current_size  The current size

        @return     { no return val; alters self.heap }
        """
        LC = 2 * index
        RC = 2 * index + 1
        smallest = index
        if (LC <= current_size and self.ordering(
                self.key(self.heap[LC]), self.key(self.heap[index]))):
            smallest = LC
        if (RC <= current_size and self.ordering(
                self.key(self.heap[RC]), self.key(self.heap[smallest]))):
            smallest = RC
        if smallest != index:
            self.swap(index, smallest)
            self.satisfyMinHeapProperty(smallest, current_size)

    def HeapSort(self, reverse=True):
        """
        @brief      { sorts using heapsort algo }

        @param      self     The object
        @param      reverse  If true sorted in descending order

        @return     { sorted array }
        """
        # array to be returned
        sorted_arr = []
        # defined in constructor for heap
        current_size = self.current_size
        while current_size != 0:
            self.swap(1, current_size)
            sorted_arr.append(self.heap[current_size])
            current_size -= 1
            self.satisfyMinHeapProperty(1, current_size)
        # restore the object heap
        self.buildHeap(sorted_arr, self.key)
        return (sorted_arr if reverse else sorted_arr[::-1])

    def reconstructHeap(self, key):
        self.key = key
        self.buildHeap(self.heap[1:])  # ingoring the 0 at front


if __name__ == '__main__':
    """
    main block to execute tests
    """
    # test = [1, 5, 3, 4, 6, 7, 5, 3]
    test = [((3, 4), 2.8284271247461903), ((8, 9), 9.899494936611665),
            ((10, 2), 9.0), ((0.1, 2), 0.9), ((10, 5), 9.486832980505138)]
    print("Initial -- ")
    print(test)
    Heap = Heap(isMin=False)
    Heap.buildHeap(test, key=lambda x: x[1])
    print('after construction:', Heap.heap)
    print(Heap)
    sorted_arr = Heap.HeapSort()
    print("sorted:")
    print(sorted_arr)
    Heap.deleteVal(9.0)
    print("heap after delete:")
    print(Heap.heap)
