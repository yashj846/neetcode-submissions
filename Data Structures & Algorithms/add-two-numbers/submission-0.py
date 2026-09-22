# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        array_n = []
        while l1 and l2:
            add = (l1.val + l2.val + carry) % 10
            carry =  (l1.val + l2.val + carry) // 10
            add_n = ListNode(add)
            array_n.append(add_n)
            l1 = l1.next
            l2 = l2.next

        while l1:
            add = (l1.val + carry) % 10
            carry =  (l1.val + carry) // 10
            add_n = ListNode(add)
            array_n.append(add_n)
            l1 = l1.next

        while l2:
            add = (l2.val + carry) % 10
            carry =  (l2.val + carry) // 10
            add_n = ListNode(add)
            array_n.append(add_n)
            l2 = l2.next

        for i in range(1, len(array_n), 1):
            array_n[i-1].next = array_n[i]
        
        if carry != 0:
            array_n[len(array_n)-1].next = ListNode(carry, None)
        else:
             array_n[len(array_n)-1].next = None
        
        return array_n[0]
            
        

