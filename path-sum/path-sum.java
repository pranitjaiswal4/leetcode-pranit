/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return dfs(root, targetSum, 0);
    }
    
    public boolean dfs(TreeNode node, int targetSum, int sum) {
        boolean found = false;
        
        if (node != null) {
            
            sum += node.val;
            
            if (node.left == null && node.right == null) {
                if(sum == targetSum) {
                    found = true;
                }
            }
            
            if (node.left != null) {
                found = found || dfs(node.left, targetSum, sum);
            }
            
            if (node.right != null) {
                found = found || dfs(node.right, targetSum, sum);
            }
        }
        
        return found;
    }
}