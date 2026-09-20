# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head #eventually get the mid point
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        next_r = None
        while curr:
            temp = curr.next
            curr.next = next_r
            next_r = curr #variable with most recent not none
            curr = temp

        # while slow and next_r:

        # print(curr.val, curr.next)
        l1, l2 = head, next_r

        while l2:
            temp1 = l1.next
            l1.next = l2
            l1 = temp1
            temp2 = l2.next
            l2.next = l1
            l2 = temp2

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        return

            

        #     print(l1.val)
        #     l1 = l1.next
        
        # while l2:
        #     print(l2.val)
        #     l2 = l2.next
        # # while l1 and l2:
        # #     l1.next = l2
        # #     l1 = l1.next
        # #     l2.next = l1
        # #     l2 = l2.next
        
        # return head



        # left, right = head,head
        # while right and right.next:
        #     right = right.next
            

        





        # while left != slow and right != slow:
        #     left.next = right
        #     left = left.next
        #     right.next = left
        #     right = right.prev

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        #     break
        
        return head
        
        
        


   

        # while left <= right:
        #     left.next = right


        


        