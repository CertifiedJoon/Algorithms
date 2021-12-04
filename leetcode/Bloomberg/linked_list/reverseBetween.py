class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        curr = head
        prev = None
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        before_left = prev 
        left_node = curr
        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if before_left:
            before_left.next = prev
        else:
            head = prev
        left_node.next = curr
        return head