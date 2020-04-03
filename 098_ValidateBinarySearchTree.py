'''
98. Validate Binary Search Tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

import sys
from helpers.binary_tree_helper import BinaryTree
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_limit = -sys.maxsize - 1
        max_limit = sys.maxsize
        return self.isValidBSTHelper(root, min_limit, max_limit)
        

    def isValidBSTHelper(self, root, min_limit, max_limit):
        if root == None:
            return True
        
        if root.value >= min_limit and root.value < max_limit and self.isValidBSTHelper(root.left, min_limit, root.value) and self.isValidBSTHelper(root.right, root.value, max_limit):
            return True
        return False

tree_arr = [2, 1, 3]
root = BinaryTree.build_binary_tree(tree_arr)
tree = BinaryTree.print_binary_tree(root)
print(tree)

s = Solution()
result = s.isValidBST(root)
print(result)