# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp = ListNode(0)
        ans = temp 
        while l1 and l2:
            add = (l1.val + l2.val + carry) % 10
            carry =  (l1.val + l2.val + carry) // 10
            temp.next = ListNode(add)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            add = (l1.val + carry) % 10
            carry =  (l1.val + carry) // 10
            temp.next = ListNode(add)
            temp = temp.next
            l1 = l1.next

        while l2:
            add = (l2.val + carry) % 10
            carry =  (l2.val + carry) // 10
            temp.next = ListNode(add)
            temp = temp.next
            l2 = l2.next
        
        if carry != 0:
            temp.next = ListNode(carry, None)
        
        return ans.next
            
        

