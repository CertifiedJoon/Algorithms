class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomListRuntime(self, head):
        c = copied = ListNode(0)
        created = {}
        while head:
            if id(head) in created:
                c.next = created[id(head)]
            else:
                c.next = ListNode(head.val)
                created[id(head)] = c.next
            c = c.next
            if head.random != None:
                if id(head.random) in created:
                    c.random = created[id(head.random)]
                else:
                    c.random = ListNode(head.random.val)
                    created[id(head.random)] = c.random
            head = head.next
        return copied.next
    
    def copyRandomListSpace(self, head):
        curr = head
        while curr:
            new_next = Node(curr.val, curr.next)
            curr.next = new_next
            curr = new_next.next
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        curr_old = head
        curr_new = head_new = head.next
        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next 
        return head_new

head = curr = ListNode(0)
nums = [7,13,11,10,1]

for num in nums:
    curr.next = ListNode(num)
    curr = curr.next

s = Solution()
copied = s.copyRandomList(head.next)
curr = head
while copied and curr:
    if copied is curr:
        break
    print(copied.val,end=" -> ")
    copied = copied.next
    curr = curr.next
print("null")