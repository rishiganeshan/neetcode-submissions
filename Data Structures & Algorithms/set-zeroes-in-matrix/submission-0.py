from math import inf
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        
        m,n = len(matrix),len(matrix[0])

        def update(x,y):
            for j in range(n):
                if matrix[x][j] != 0:
                    matrix[x][j] = inf
            for i in range(m):
                if matrix[i][y] != 0:
                    matrix[i][y] = inf


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    update(i,j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == inf:
                    matrix[i][j] = 0

        
        