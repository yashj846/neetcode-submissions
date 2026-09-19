# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1.val <= list2.val:  
        #     res = ListNode(list1.val, None)
        # else:
        res = ListNode(None, None)
        res_temp = res

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            res = res.next

        if list1:
            res.next = list1
        if list2:
            res.next = list2

        return res_temp.next

        