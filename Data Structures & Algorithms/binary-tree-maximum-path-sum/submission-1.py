# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -1001
        # node to (left, right)




        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            # dic[node] == [left,right]
            
            best = max(node.val, node.val+left, node.val+right)
            res = max(best,left+right+node.val,res)

            return best
            
        
        dfs(root)
        return res


            



        