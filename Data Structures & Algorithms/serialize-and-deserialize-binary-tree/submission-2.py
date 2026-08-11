# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encode = []

        if root:
            q = deque([root])
        else:
            return ""
            
        # count = 0
        while q:
            cur = q.popleft()
            if cur:
                # count += 1
                encode.append(str(cur.val))
                encode.append('|')
                q.append(cur.left)
                q.append(cur.right)
            else:
                # count += 1
                encode.append("*")
                encode.append('|')
            # refarcotr the below line, expensive
        # print(count)

        return ''.join(encode[:-1])


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        q = deque()

        def nodify(s):
            if s == "*":
                return None
            if s[0] == "-":
                return TreeNode(-1*int(s[1:]))
            return TreeNode(int(s))

        data = [nodify(s) for s in data.split("|")]

        q.append(data[0])
        root = q[0]
        i = 1
        # print(len(data))
        while q:
            cur = q.popleft()
            if not cur:
                continue
            cur.left = data[i]
            q.append(cur.left)
            i += 1
            cur.right = data[i]
            i += 1
            q.append(cur.right)
        return root


        

            
            
            


