# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ppath,qpath = [],[]
        pval, qval = p.val, q.val

        def getPath(node, val, path):
            if not node:
                return False
            if node.val == val:
                path.append(node)
                return True
            path.append(node)
            if getPath(node.left, val, path):
                return True
            if getPath(node.right, val, path):
                return True
            path.pop()
            return False
        
        getPath(root,pval,ppath)
        getPath(root,qval,qpath)

        res = -1

        for i in range(min(len(ppath),len(qpath))):
            if ppath[i] == qpath[i]:
                res = i
            else:
                break

        return ppath[res]



