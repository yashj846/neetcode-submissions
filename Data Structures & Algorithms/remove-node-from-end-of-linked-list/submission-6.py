# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        element_to_find = l - n
        curr, prev = head, None 
        pointer = 0
        if element_to_find != 0:
            while pointer < element_to_find:
                prev = curr
                curr = curr.next
                pointer += 1
            prev.next = curr.next
        else:
            head = head.next
        return head

        # curr 
        
        # if prev:
        #     return head
        # else: return None

            

        


        # temp = []
        # curr = head
        # while curr:
        #     temp.append(curr)
        #     curr = curr.next
        # temp2 = []
        # for i in range(len(temp)):
        #     if len(temp) - n != i:
        #         temp2.append(temp[i])
    
        # head = temp2[0] if len(temp2)!= 0 else None
        # for i in range(len(temp2)):
        #     if i == len(temp2) - 1:
        #         temp2[i].next = None
        #     else:
        #         temp2[i].next = temp2[i+1]
        # return head






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


        
        
        



        