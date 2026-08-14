# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        maxPathSum = root.val
        
        # returns max straight path from node, including 0
        def dfs(node):
            nonlocal maxPathSum

            if not node:
                return 0
            
            bestLeft = dfs(node.left)
            bestRight = dfs(node.right)

            maxPathSum = max(maxPathSum, node.val + bestLeft + bestRight)

            return max(max(bestLeft,bestRight) + node.val, 0)
        
        dfs(root)

        return maxPathSum
        