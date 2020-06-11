'''
226. Invert Binary Tree

Invert a binary tree.

Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

'''
ALGORITHM:
1. Recurse over the tree
2. Call invert for left-subtree.
3. Call invert for right-subtree.
4. Swap left and right subtrees. 

RUNTIME COMPLEXITY: O(N) For n nodes in the binary tree
SPACE COMPLEXITY: O(N) For recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return root
        else:
            temp = root.left
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)
            root.left = right
            root.right = left
            return root 