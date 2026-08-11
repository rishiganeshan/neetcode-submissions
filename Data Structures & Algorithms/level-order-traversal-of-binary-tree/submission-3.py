# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            res.append([node.val for node in q])

            children = deque()
            while q:
                node = q.popleft()
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            q = children
        
        return res
                
            







        