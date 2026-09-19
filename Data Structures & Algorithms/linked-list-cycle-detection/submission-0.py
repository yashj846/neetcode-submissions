# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        next_list = []
        while head:
            if head not in next_list:
                next_list.append(head)
            else:
                return True
            head =head.next
        return False


        