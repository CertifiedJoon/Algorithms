class Solution:
    def isPalindromeRec(self, head):
        self.front_pointer = head
        def recCheckPalindromic(curr):
            if not curr:
                return True
            if not recCheckPalindromic(curr.next):
                return False
            if curr.val != self.front_pointer.val:
                return False
            self.front_pointer = self.front_pointer.next
            return True
        return recCheckPalindromic(head)    

    def isPalindromeInPlace(self, head):
        fast = slow = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        