'''
988. Smallest String Starting From Leaf

Given the root of a binary tree, each node has a value from 0 to 25 representing 
the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', 
and so on.
Find the lexicographically smallest string that starts at a leaf of this tree 
and ends at the root.
(As a reminder, any shorter prefix of a string is lexicographically smaller: for 
example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a 
node that has no children.)

Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"

Note:
The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
'''

'''
ALGORITHM:
1. Using post-order traversal, generate all string leaf-to-root paths and 
   use min() function to get the minimum path. 
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
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        return self.post_order_traversal(root, '', 'z')
        
    def post_order_traversal(self, root, path, min_path):
        if root.left == None and root.right == None:
            path = chr(root.val + 97) + path
            min_path = min(path, min_path)
            return min_path
        left, right = 'z', 'z'
        if root.left:
            left = self.post_order_traversal(root.left, chr(root.val + 97) + path, min_path)
        if root.right:
            right = self.post_order_traversal(root.right, chr(root.val + 97) + path, min_path)
        return min(left, right)
