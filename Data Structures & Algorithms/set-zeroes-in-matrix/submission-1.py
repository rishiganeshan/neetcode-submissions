from math import inf
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        
        m,n = len(matrix),len(matrix[0])

        def scanVert(j):
            for i in range(m):
                if matrix[i][j] == 0:
                    # matrix[0][j] = 0
                    return True
            return False

        def scanHori(i):
            for j in range(n):
                if matrix[i][j] == 0:
                    # matrix[i][0] = 0
                    return True
            return False

        vert = scanVert(0)
        hori = scanHori(0)

        for j in range(1,n):
            if scanVert(j):
                matrix[0][j] = 0
        for i in range(1,m):
            if scanHori(i):
                matrix[i][0] = 0


        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if vert:
            for i in range(m):
                matrix[i][0] = 0
        if hori:
            for j in range(n):
                matrix[0][j] = 0


        
        