class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = []
        offset = [-1,0,1,0,-1]
        visited = set()

        def dfs(i,x,y):
            if i == len(word):
                return True
            if (x,y) in visited:
                return False
            if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
                return False
            if board[x][y] != word[i]:
                return False

            visited.add((x,y))
            path.append(board[x][y])
            
            for idx in range(1,len(offset)):
                if dfs(i+1,x+offset[idx-1],y+offset[idx]):
                    return True

            path.pop()
            visited.remove((x,y))

            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(0,x,y):
                    return True
        
        return False
            
