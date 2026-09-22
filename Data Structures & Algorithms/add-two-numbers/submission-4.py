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
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            add = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10


            temp.next = ListNode(add)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # while l1:
        #     add = (l1.val + carry) % 10
        #     carry =  (l1.val + carry) // 10
        #     temp.next = ListNode(add)
        #     temp = temp.next
        #     l1 = l1.next

        # while l2:
        #     add = (l2.val + carry) % 10
        #     carry =  (l2.val + carry) // 10
        #     temp.next = ListNode(add)
        #     temp = temp.next
        #     l2 = l2.next
        
        if carry != 0:
            temp.next = ListNode(carry, None)
        
        return ans.next
            
        

