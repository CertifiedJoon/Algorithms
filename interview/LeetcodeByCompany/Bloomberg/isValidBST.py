class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recIsValidBST(root, float('-inf'), float('inf'))
        
    def recIsValidBST(self, root, lo, hi):
        if not root:
            return True
        if root.val <= lo or root.val >= hi:
            return False
        return self.recIsValidBST(root.left, lo, root.val) and self.recIsValidBST(root.right, root.val, hi)