class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        m = len(matrix)
        n = len(matrix[0])

        d = 0
        directions = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]
        isBoundary = lambda i, j : 0 <= i < m and 0 <= j < n
        isValid = lambda i, j : matrix[i][j] != '#'

        def getXY(d, i, j):
            newX = i + directions[d][0]
            newY = j + directions[d][1]
            return newX, newY

        def dfs(i, j):
            nonlocal d
            result.append(matrix[i][j])
            matrix[i][j] = '#'

            newX, newY = getXY(d, i, j)

            if isBoundary(newX, newY):
                if not isValid(newX, newY):
                    d = (d + 1) % 4
                    newX, newY = getXY(d, i, j)
            else:
                d = (d + 1) % 4
                newX, newY = getXY(d, i, j)
                
            if len(result) < (m * n):
                dfs(newX, newY)

        dfs(0, 0)
        return result