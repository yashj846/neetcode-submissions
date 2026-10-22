# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        def depth(node):
            if not node:
                return 0

            return 1 + max(depth(node.left), depth(node.right))
        # print(depth(root))
        
        q = deque()
        q.append(root)
        for_each_node = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                leftH = depth(node.left)
                rightH = depth(node.right)
                if abs(leftH-rightH) > 1:
                    return False
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
                # for_each_node.append([node.val, leftH, rightH])
                # print(for_each_node)

        return True
        