/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        if(root == null){
            return [];
        }
        IList<IList<int>> valid_paths = new List<IList<int>>();

        paths(root, targetSum, 0, valid_paths, []);


        return valid_paths;

    }
    public void paths(TreeNode node, int targetSum, int cur_sum, IList<IList<int>> valid_paths, List<int> cur_path){
        cur_sum += node.val;
        cur_path.Add(node.val);
        if(node.right == null && node.left == null){
            if (cur_sum == targetSum){
                valid_paths.Add(new List<int>(cur_path));
            }
        }
        if(node.left != null){
            paths(node.left, targetSum, cur_sum, valid_paths, cur_path);
        }
       
        if(node.right != null){ 
            paths(node.right, targetSum, cur_sum, valid_paths, cur_path);
        }
        cur_path.RemoveAt(cur_path.Count - 1);
    }
}