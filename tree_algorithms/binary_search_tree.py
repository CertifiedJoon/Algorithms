from .linked_binary_tree.py import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, sorted_array = None):
        self._root = None
        self._size = 0
        if sorted_array is not None:
            self.create_minimal_bst(array)
    
    def create_minimal_bst(self, array):
        """Wrapper for self._rec_create_minimal_bast(array, start, end) method"""
        self._rec_create_minimal_bst(array, start, end)
        
    def _rec_create_minimal_bst(self, array, start, end):
        """Create a binary search tree with minimal height from a sorted array"""
        if end < start:
            return
        mid = start + (end - start) // 2
        
        self.insert(array[mid])
        self._rec_create_minimal_bst(array, start, mid - 1)
        self._rec_create_minimal_bst(array, mid + 1, end)
        
    def insert(self, element):
        """inserts an element to a tree"""
        if self.is_empty():
            self._add_root(element)
        curr = self.root()
        parent = None
        while curr:
            parent = curr
            if element < curr.element():
                curr = self.left(curr)
            else:
                curr = self.right(curr)
        self._add_left(parent, element) if element < parent.element()
                                        else self._add_right(parent, element)
            
    def list_by_depth(self):
        """create a list of lists of element in same depth"""
        
    def _rec_list_by_depth(self, p, depth, l):
        if not p:
            return
        if depth >= len(l):
            l.append([])
        l[depth].append(p.element())
        self._rec_list_by_depth(p.left(), depth + 1, l)
        self._rec_list_by_depth(p.right(), depth + 1, l)
    