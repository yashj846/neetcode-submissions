# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def recursiveInvert(node):
            if not node:
                return

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:recursiveInvert(node.left)
            if node.right:recursiveInvert(node.right)
        
        recursiveInvert(root)
        return root





        