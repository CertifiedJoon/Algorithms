class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        def array_to_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = array_to_tree(left, inorder_index[root_value] - 1)
            root.right = array_to_tree(inorder_index[root_value] + 1, right)

            return root
        
        preorder_index = 0
        inorder_index = {}

        for i, val in enumerate(inorder):   
            inorder_index[val] = i

        return array_to_tree(0, len(preorder) - 1)
