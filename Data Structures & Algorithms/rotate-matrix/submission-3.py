class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        def newPoint(i,j):
            oneonecol = len(matrix) - 1
            oneonerow = 0
            # n = 2 -> 1, 3-> 1.5, 4->2

            newJ = oneonecol - i
            verI = oneonerow + j

            return (verI,newJ)



        l, r = 0, len(matrix) - 1
        i = 0
        while l < r:
            for j in range(l, r):
 
                i = l             
                a = newPoint(i,j)
                b = newPoint(a[0],a[1])
                c = newPoint(b[0],b[1])
                matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]],matrix[i][j] = matrix[i][j], matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]]
            l += 1
            r -= 1



                
        