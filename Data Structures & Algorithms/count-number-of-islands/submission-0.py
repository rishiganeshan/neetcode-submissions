class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        for go through each cell in grid:
            if thing is land: increment ans by 1, call dfs on cell

        in dfs, just convert any land to water
        retur

        O(m*n)

        """
        m,n = len(grid),len(grid[0])

        offsets = [-1,0,1,0,-1]
        res = 0

        def dfs(i,j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            
            for idx in range(1,len(offsets)):
                dfs(i+offsets[idx-1],j+offsets[idx])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)

        return res



        