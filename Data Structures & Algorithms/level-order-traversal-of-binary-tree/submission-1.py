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
        q.append((root,1))
        row = None

        while q:
            cur = q.popleft()
            node = cur[0]
            level = cur[1]
            if level > len(res):
                res.append([node.val])
                row = res[-1]
            else:
                row.append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        
        return res
                
            







        