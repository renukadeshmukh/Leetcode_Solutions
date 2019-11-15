'''
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every 
key of the original BST is changed to the original key plus sum of all keys 
greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

'''
ALGORITHM:
1. Perform a reverse in-order traversal is via recursion.
2. Maintain A "global" sum so each recursive call can access and modify the 
   current total sum. 
3. Essentially, recurse on the right subtree, visit the current node by updating 
   its value and the total sum, and finally recurse on the left subtree.

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
    
    def __init__(self):
        self.sum = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            root.val += self.sum
            self.sum = root.val
            self.convertBST(root.left)
        return root
        
    
