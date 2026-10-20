# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def invertNode(node):
            temp = node.left
            node.left = node.right
            node.right = temp

        stack = [root]
        while stack:
            no = stack.pop()
            invertNode(no)
            if no.left:stack.append(no.left)
            if no.right:stack.append(no.right)
        return root




        