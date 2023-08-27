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
    public void Flatten(TreeNode root) {
        if(root == null){
            return;
        }
        TreeNode leftSide = root.left;
        TreeNode rightSide = root.right;
        root.left = null;
        this.Flatten(leftSide);
        this.Flatten(rightSide);
        root.right = leftSide;
        TreeNode curr = root;
        while(curr.right != null){
            curr = curr.right;
        }
        curr.right = rightSide;
    }
}