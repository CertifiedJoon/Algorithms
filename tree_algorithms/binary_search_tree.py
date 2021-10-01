from linked_binary_tree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, sorted_array = None):
        self._root = None
        self._size = 0
        if sorted_array is not None:
            self.create_minimal_bst(sorted_array)
    
    def create_minimal_bst(self, array):
        """Wrapper for self._rec_create_minimal_bast(array, start, end) method"""
        self._rec_create_minimal_bst(array, 0, len(array)-1)
        
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
            return
        curr = self.root()
        parent = None
        while curr:
            parent = curr
            if element < curr.element():
                curr = self.left(curr)
            else:
                curr = self.right(curr)
        self._add_left(parent, element) if element < parent.element() else self._add_right(parent, element)
            

if __name__ == "__main__":
    bst = BinarySearchTree([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    bst.preorder_indented()
    print(bst.is_balanced())
    print(bst._bfs_list_by_depth())
    print(bst.is_bst())
    print(bst.inorder_successor(bst.root()).element())