# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indic = {}
        for i,num in enumerate(inorder):
            indic[num] = i

        a = 0

        def recurse(c,d) -> Optional[TreeNode]:
            nonlocal a
            if c==d:
                return None

            root = TreeNode(val=preorder[a])

            idx = indic[preorder[a]]
            
            a += 1
            root.left = recurse(c,idx)
            root.right = recurse(idx+1,d)
  
              

            return root
 
        
        return recurse(0,len(preorder))



        