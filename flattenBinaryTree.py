"""
Time Complexity : O(n) where n is the number of nodes
Space Complexity : O(h) where h is the heaight of the tree
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Base Case
        if root == None:
            return
        # 1. Store left and right sub-trees and then make left sub-tree as Null
        left_side = root.left
        right_side = root.right
        root.left = None
        # 2. Recursively flatten the sub-trees
        self.flatten(left_side)
        self.flatten(right_side)
        # 3. Assign the flattened left sub-tree to the right of root
        root.right = left_side
        # 4. Assign the flattened right sub-tree to the right of the last node of the flattened left sub-tree
        current = root
        while(current.right):
            # Go to the last node
            current = current.right
        current.right = right_side