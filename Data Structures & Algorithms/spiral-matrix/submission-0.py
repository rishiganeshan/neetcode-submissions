class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        colMov = 1
        rowMov = 0

        m = len(matrix)
        n = len(matrix[0])

        moves = {(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}



        res = []

        i,j = 0,0

        for _ in range(100):

            res.append(matrix[i][j])
            matrix[i][j] = -1000
            
            if len(res) == m*n:
                return res
            if 0 <= i+rowMov < m and 0 <= j+colMov < n and matrix[i+rowMov][j+colMov] != -1000:
                
                i += rowMov
                j += colMov
            else:
                rowMov, colMov = moves[(rowMov,colMov)]
                i += rowMov
                j += colMov
                




        