class Solution:
    def connect(self, root):
        if not root:
            return None
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
        return root
    
    def process_child(self, child, prev, leftmost):
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child
            prev = child
        return prev, leftmost