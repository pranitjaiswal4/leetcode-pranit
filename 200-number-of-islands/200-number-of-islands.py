class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        isBoundary = lambda i, j : 0 <= i < m and 0 <= j < n
        isValid = lambda i, j : grid[i][j] == '1'
        
        def dfs(i, j):
            grid[i][j] = '#'
            
            for x, y in directions:
                newX = x + i
                newY = y + j           
                
                if isBoundary(newX, newY):
                    if isValid(newX, newY):
                        dfs(newX, newY)
        
        
        for i in range(m):
            for j in range(n):
                if isValid(i, j):
                    count += 1
                    dfs(i, j)
                    
        return count
        