'''
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued 
grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the 
blue nodes are the even-value grandparents.
 

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

'''
ALGORITHM:
1. Modify inorder traversal and pass parent and grandparent values to inorder
   traversal
2. If grandparent is even, add root.val to the final sum

RUNTIME COMPLEXITY: O(N) for recursion
SPACE COMPLEXITY: O(N) for recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sm = self.inorder(root, -1, -1)
        return sm
        
        
    def inorder(self, root, parent, gparent):
        if root == None:
            return 0

        x = 0
        if gparent % 2 == 0:
            x = root.val
        sm_left = self.inorder(root.left, root.val, parent)
        sm_right = self.inorder(root.right, root.val, parent)
            
        return x + sm_left + sm_right
            
        