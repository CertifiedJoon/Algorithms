class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect2(self, root):
        order = []
        self.list_by_depth(root, order)
        for depth in range(len(order)):
            for i in range(len(order[depth]) - 1):
                order[depth][i].next = order[depth][i+1]

    def list_by_depth(self, root, order, depth = 0):
        if not root:
            return
        if len(order) == depth:
            order.append([root])
        else:
            order[depth].append(root)
        self.list_by_depth(root.left, order, depth + 1)
        self.list_by_depth(root.right, order, depth + 1)

    def connect3(self, root):
        self._rec_connect(root, None)
        return root

    def _rec_connect(self, node, parent):
        if not node:
            return
        self._rec_connect(node.left, node)        
        if parent:
            if node == parent.left:
                node.next = parent.right
            elif parent.next and node == parent.right:
                node.next = parent.next.left
        self._rec_connect(node.right, node)

    def connect4(self, root):
        parent = None
        curr = root
        while curr:
            if parent:
                if curr == parent.left:
                    curr.next = parent.right
                elif parent.next and curr == parent.right:
                    curr.next = parent.next.left
            if curr.left:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    parent = curr
                    curr = curr.left
                elif prev.right == curr:
                    prev.right = None
                    parent = curr
                    curr = curr.right
            else:
                parent = curr
                curr = curr.right
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        return root

