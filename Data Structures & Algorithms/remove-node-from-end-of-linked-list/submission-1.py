# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr)
            curr = curr.next
        temp2 = []
        for i in range(len(temp)):
            if len(temp) - n != i:
                temp2.append(temp[i])
        # print(temp2)
    
        head = temp2[0] if len(temp2)!= 0 else None
        for i in range(len(temp2)):
            if i == len(temp2) - 1:
                temp2[i].next = None
            else:
                temp2[i].next = temp2[i+1]
        return head
        # return head
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next






        # curr = head
        # next_r = None

        # while curr:
        #     temp = curr.next
        #     curr.next = next_r
        #     next_r = curr
        #     curr = temp
        # curr = next_r
        # n -= 1
        # prev = curr
        # while n > 0:
        #     prev = curr
        #     curr = curr.next
        #     n -= 1
        # prev.next = curr.next


        # curr = next_r
        # prev = None
        # while curr:
        #     # print(curr.val)
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # return head
        


        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # while n > 1:
        #     prev = curr
        #     curr = curr.next
        #     n -= 1
        # prev.next = curr.next



        # curr = next_r
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return head
            
        
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next


        
        
        



        