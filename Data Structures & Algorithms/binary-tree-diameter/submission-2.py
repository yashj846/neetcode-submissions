# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):

            if not node:
                return 0

            return 1 + max(maxDepth(node.left), maxDepth(node.right))


        q = [root]
        res = 0
        while q:
            node = q.pop()
            leftD = maxDepth(node.left)
            rightD = maxDepth(node.right)
            res = max(res, leftD + rightD)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res





        