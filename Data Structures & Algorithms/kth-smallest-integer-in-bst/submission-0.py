# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def recurse(node):
            if len(arr) == k:
                return
            if not node:
                return
            
            if node.left:
                recurse(node.left)
            if len(arr) == k:
                return
            arr.append(node.val)
            if len(arr) == k:
                return
            if node.right:
                recurse(node.right)
            if len(arr) == k:
                return



        recurse(root)
        return arr[-1]

            




        