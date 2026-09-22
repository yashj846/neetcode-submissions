"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        node_copy = {None:None}
        while curr:
            node_copy[curr] = Node(curr.val)
            curr  = curr.next
        
        curr = head
        while curr:
            temp = node_copy[curr]
            temp.next = node_copy[curr.next]
            temp.random = node_copy[curr.random]
            curr = curr.next
        
        return node_copy[head]




        # curr = head
        # node_details = node_copy[curr]
        # val = node_details[0]
        # new_node = Node(val, None, None)

        # next_n = node_details[1] #Node
        # new_next_node = Node(next_n.val, None, None)

        # random_n = node_details[2] #Node
        # new_random_node = Node(random_n, None, None)

        # new_node.next = new_next_node
        # new_node.random = new_random_node



        # while curr:
        #     node_details = node_copy[curr]


        # print(node_copy)




        