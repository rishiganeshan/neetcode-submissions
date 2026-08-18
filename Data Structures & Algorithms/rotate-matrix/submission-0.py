class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        def newPoint(i,j):
            oneonecol = len(matrix) - 1
            oneonerow = 0
            # n = 2 -> 1, 3-> 1.5, 4->2

            newJ = oneonecol - i
            verI = oneonerow + j

            return (verI,newJ)

        seen = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i,j) in seen:
                    continue
                # print((i,j))
                
                a = newPoint(i,j)
                b = newPoint(a[0],a[1])
                c = newPoint(b[0],b[1])
                # print(a)
                # print(b)
                # print(c)
                # print()
                seen.add((i,j))
                seen.add(a)
                seen.add(b)
                seen.add(c)


                matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]],matrix[i][j] = matrix[i][j], matrix[a[0]][a[1]],matrix[b[0]][b[1]],matrix[c[0]][c[1]]
                
        