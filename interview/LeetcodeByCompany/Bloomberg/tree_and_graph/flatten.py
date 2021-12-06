class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten_stack(self, head):
        prehead = Node(0, None, head, None)
        stack = [pre_head,]
        while stack:
            curr = stack.pop()
            prev.next = curr
            prev = curr
            stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        return prehead.next

    def flatten_morris(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            if curr.child:
                pred = curr.child
                while pred.next:
                    pred = pred.next
                curr.child.prev = curr
                if curr.next: curr.next.prev = pred
                pred.next = curr.next
                curr.next = curr.child
                curr.child = None
            curr = curr.next
        return head