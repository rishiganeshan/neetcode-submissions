# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(node, lbound, ubound):
            if not node:
                return True
            if node.val <= lbound or node.val >= ubound:
                return False
            
            return recurse(node.left, lbound, min(node.val,ubound)) and recurse(node.right, max(node.val,lbound), ubound)


        return recurse(root, -math.inf, math.inf)
