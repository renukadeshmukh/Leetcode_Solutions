'''
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges 
between them.
'''

'''
ALGORITHM:
1. Keep a global variable to maintain largest diameter. 
2. For every node, calculate the height of left and right subtree. 
3. diameter = max(diameter, left_height + right_height)
4. return left_height + right_height + 1

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.diameter = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getHeight(root)
        return self.diameter
    
    
    def getHeight(self, root):
        if root:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        else:
            return 0