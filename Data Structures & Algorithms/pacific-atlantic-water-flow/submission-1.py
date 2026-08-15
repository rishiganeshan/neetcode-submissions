class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pa = set()
        a = set()

        x,y = len(heights), len(heights[0])

        def dfs(p,i,j):

            p.add((i,j))
            
            offsets = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]

            for newI, newJ in offsets:
                if not (0 <= newI < x and 0 <= newJ < y) or (newI,newJ) in p:
                    continue
                if heights[newI][newJ] < heights[i][j]:
                    continue
                dfs(p,newI,newJ)




        
        for i in range(x):
            dfs(pa,i,0)
        for j in range(y):
            dfs(pa,0,j)

        for i in range(x):
            dfs(a,i,y-1)
        for j in range(y):
            dfs(a,x-1,j)


        return list(list(tup) for tup in pa.intersection(a))
