class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        int rows = grid.length;
        int columns= grid[0].length;

        for(int i=0; i<rows;i++)
        {
            for(int j=0; j<columns; j++)
            {
                if(grid[i][j]=='1')
                {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }

        return count;
    }

    private void dfs( char [][] matrix , int i , int j)
    {

        if(i<0 || i>= matrix.length || j>=matrix[0].length || j<0 || matrix[i][j]=='0') return; 

        matrix[i][j]='0';

        dfs(matrix, i+1, j);   //down 
        dfs(matrix, i-1,j);   //up
        dfs(matrix, i, j+1);// right
        dfs(matrix, i,j-1); // left 
    }
}