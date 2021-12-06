class Solution:
    def rightSideView2(self, root):
        ret = []
        self._rec_rightSideView(root, 0, ret)
        return ret
    
    def _rec_rightSideView(self, root, depth, ret):
        if not root:
            return
        if len(root) == depth:
            ret.append(root.val)
        else:
            ret[depth] = root.val
        self._rec_rightSideView(root.left, depth + 1, ret)
        self._rec_rightSideView(root.right, depth + 1, ret)
    
    def rightSideView2(self, root):
        if root is None:
            return []
        q = deque([root, None])
        ret = []
        curr = root
        while q:
            prev, curr = curr, q.popleft()
            while curr:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev, curr = curr, q.popleft()
            ret.append(prev.val)
            if q:
                q.append(None)
        return ret
