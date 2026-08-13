class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Node()
        m,n = len(board), len(board[0])
        offset = [-1,0,1,0,-1]
        path = []
        seen = set()
        ans = set()

        def addWord(word):
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node(char)
                cur = cur.children[char]
            cur.end = True


        def dfs(x,y,node):
            if node.end:
                ans.add(''.join(path))

            if not 0 <= x < m or not 0 <= y < n or (x,y) in seen or board[x][y] not in node.children:
                return

            

            seen.add((x,y))
            path.append(board[x][y])

            newNode = node.children[board[x][y]]

            for j in range(1,len(offset)):
                dfs(x + offset[j],y + offset[j-1],newNode)

            path.pop()
            seen.remove((x,y))
        
        for word in words:
            addWord(word)

        for x in range(m):
            for y in range(n):
                dfs(x,y,root)

        return list(ans)

                    



        

        