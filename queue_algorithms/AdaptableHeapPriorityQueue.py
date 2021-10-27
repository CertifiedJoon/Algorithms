from .HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        __slots__ =  '_index'
        def __init__(self, pos, key, val):
            super().__init__(key, val)
            self._index = pos
    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = j
        self._data[j]._index = i
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)