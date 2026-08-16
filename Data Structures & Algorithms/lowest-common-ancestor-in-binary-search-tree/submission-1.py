# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node, target, path):
            
            path.append(node)

            if target == node.val:
                return path
            
            elif target < node.val:
                return dfs(node.left, target, path)
            
            else:
                return dfs(node.right, target, path)

        pathp = dfs(root,p.val,[])
        pathq = dfs(root,q.val,[])

        res = 0
        
        while res < len(pathp) and res < len(pathq) and pathp[res] == pathq[res]:
            res += 1
        
        return pathp[res-1]


            

        