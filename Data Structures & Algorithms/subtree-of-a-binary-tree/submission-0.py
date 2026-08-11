# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self,p,q):
        if not p and q or not q and p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.same(p.left,q.left) and self.same(p.right,q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if self.same(root,subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True

        return False

        
