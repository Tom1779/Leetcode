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
    public void traverse(TreeNode node, IList<int> nodes){
        if(node.left != null){
            traverse(node.left, nodes);
        }
        nodes.Add(node.val);
        if(node.right != null){
            traverse(node.right, nodes);
        }

    }

    public IList<int> InorderTraversal(TreeNode root) {
        IList<int> nodes = new List<int>();

        if(root != null){
            traverse(root, nodes);
        }

        return nodes;
        
    }
}