class Solution:
    def hasCycle(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return False