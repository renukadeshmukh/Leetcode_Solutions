'''
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, t_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.sumPath(root, t_sum, 0)
        
    def sumPath(self, root, t_sum, a_sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            if a_sum + root.val == t_sum:
                return True
            else:
                return False
        else:
            return self.sumPath(root.left, t_sum, a_sum + root.val) or self.sumPath(root.right, t_sum, a_sum + root.val)