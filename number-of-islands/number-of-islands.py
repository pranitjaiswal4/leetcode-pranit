class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0
        m = len(grid)
        n = len(grid[0])
        
        boundary = lambda row, col : -1 < row < m and -1 < col < n
        isValid = lambda i, j: grid[i][j] == "1"
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(i, j):               
            
            # Mark Visited
            grid[i][j] = "#"
            
            for x,y in direction:
                newX = x+i
                newY = y+j
                
                if boundary(newX, newY):
                    if isValid(newX, newY):
                        dfs(newX, newY)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    output += 1
                    dfs(i, j)
        
        return output