class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ret = curr = ListNode()
        while l1 != None or l2 != None or carry == 1:
            if l1 == None and l2 == None and carry == 1:
                carry, digit = divmod(carry, 10)
            elif l1 == None:
                carry, digit = divmod(carry + l2.val, 10)
            elif l2 == None:
                carry, digit = divmod(carry + l1.val, 10)
            else:
                carry, digit = divmod(carry + l1.val + l2.val, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            if l2:
                l2 = l2.next
            if l1:
                l1 = l1.next
        return ret.next
