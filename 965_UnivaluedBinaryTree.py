'''
965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false
 
Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
'''

'''
ALGORITHM:
1. Traverse the tree and check if all node values are the same

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkIsUnivalTree(root, root.val)
        
    def checkIsUnivalTree(self, root, val):
        if root == None:
            return True
        elif root.left == None and root.right == None and root.val == val:
            return True
        else:
            return root.val == val and self.checkIsUnivalTree(root.left, val) and self.checkIsUnivalTree(root.right, val)
            
