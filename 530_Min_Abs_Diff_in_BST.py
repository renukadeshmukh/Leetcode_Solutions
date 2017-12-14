'''
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        self.inorderTraversal(root, result)
        min_diff = sys.maxint
        l1 = len(result) - 1
        for i in range(l1):
            min_diff = min(min_diff, result[i+1] - result[i])
        return min_diff
        
    def inorderTraversal(self, root, result):
        if root.left != None:
            self.inorderTraversal(root.left, result)
        result.append(root.val)
        if root.right != None:
            self.inorderTraversal(root.right, result)