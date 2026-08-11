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

        def recurse(a,b,c,d) -> Optional[TreeNode]:
            if a==b:
                return None

            root = TreeNode(val=preorder[a])

            idx = indic[preorder[a]]
            
            root.left = recurse(a+1,a+1+idx-c, c,idx)
            root.right = recurse(a+1+idx-c,b,idx+1,d)
              

            return root
 
        
        return recurse(0,len(preorder),0,len(preorder))



        