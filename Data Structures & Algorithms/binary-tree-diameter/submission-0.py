# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):
            stack = [[node,1]]
            maxD = 0

            while stack:
                no,de = stack.pop()
                if no:
                    maxD = max(maxD, de)
                    stack.append([no.left, de+1])
                    stack.append([no.right, de+1])
            return maxD

        q = [root]
        res = 0
        while q:
            node = q.pop()
            leftD = maxDepth(node.left)
            rightD = maxDepth(node.right)
            res = max(res, leftD + rightD)
            print(node.val, res)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res





        