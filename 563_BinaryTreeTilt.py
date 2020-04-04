'''
563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of 
all left subtree node values and the sum of all right subtree node values. Null 
node has tilt 0.
The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Note:
The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
'''

'''
ALGORITHM:
We need to find the tilt value at every node of the given tree and add up all 
the tilt values to obtain the final result. To find the tilt value at any node, 
we need to subtract the sum of all the nodes in its left subtree and the sum of 
all the nodes in its right subtree.

Thus, we make use of a recursive function traverse which when called from any 
node, returns the sum of the nodes below the current node including itself. With 
the help of such sum values for the right and left subchild of any node, we can 
directly obtain the tilt value corresponding to that node.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilts = [0]
        self.traverse(root, tilts)
        return tilts[0]
        
    def traverse(self, root, tilts):
        if root is None:
            return 0
        else:
            sm_left, sm_right = 0, 0
            if root.left is not None:
                sm_left = self.traverse(root.left, tilts)
            if root.right is not None:
                sm_right = self.traverse(root.right, tilts)
            tilts[-1] += abs(sm_left-sm_right)
            return sm_left + sm_right + root.val
                