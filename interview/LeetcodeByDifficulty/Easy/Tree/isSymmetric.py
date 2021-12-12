class Solution:
    def isSymmetric(self, root):
        #try plain dfs or bfs or level order traversal
        left = [node.val for node in self.morris_traversal_left(root)]
        right = [node.val for node in self.morris_traversal_right(root)]
        return left == right

    def morris_traversal_left(self, head):
        root = head
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                if prev.right == root:
                    yield root
                    prev.right = None
                    root = root.right
            else:
                yield TreeNode(-101)
                yield root
                root = root.right
        yield TreeNode(-101)
    
    def morris_traversal_right(self, head):
        root = head
        while root:
            if root.right:
                prev = root.right
                while prev.left and prev.left != root:
                    prev = prev.left
                if not prev.left:
                    prev.left = root
                    root = root.right
                if prev.left == root:
                    yield root
                    root = root.left   
                    prev.left = None
            else:
                yield TreeNode(-101)
                yield root
                root = root.left
        yield TreeNode(-101)