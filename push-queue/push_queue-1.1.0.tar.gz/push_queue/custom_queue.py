from queue import Queue


class CustomQueue(Queue):
    '''
    push an item into the queue,
    if the queue is full,get an old item out ,
    and put the new item into the queue
    '''
    def push(self, item):
        with self.mutex:
            if 0 < self.maxsize <= self._qsize():
                old_item = self._get()
                self._put(item)
                self.unfinished_tasks += 1
                self.not_empty.notify()
                return old_item
            else:
                self._put(item)
                self.unfinished_tasks += 1
                self.not_empty.notify()






