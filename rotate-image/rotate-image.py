class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Find transpose of matrix        
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        # Swap column values
        for i in range(n):
            j, k = 0, n - 1
            
            while j < k:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = temp
                
                j += 1
                k -= 1