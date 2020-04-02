'''
1038. Binary Search Tree to Greater Sum Tree

Given the root of a binary search tree with distinct values, modify it so that 
every node has a new value equal to the sum of the values of the original tree 
that are greater than or equal to node.val.
As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees. 

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 
Constraints:
The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
'''

'''
ALGORITHM:
By leveraging the fact that the tree is a BST, we can find an O(n) solution. The 
idea is to traverse BST in reverse inorder. Reverse inorder traversal of a BST 
gives us keys in decreasing order. Before visiting a node, we visit all greater 
nodes of that node. While traversing we keep track of sum of keys which is the 
sum of all the keys greater than the key of current node.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for recursion
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.left = None
#         self.right = None

from helpers.binary_tree_helper import BinaryTree
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root, 0)
        return root
    
    def traverse(self, root, sm):
        if root == None:
            return sm
        right = self.traverse(root.right, sm)
        root.value += right
        left = self.traverse(root.left, root.value)
        return left

bt = BinaryTree()
root = bt.build_binary_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
tree = bt.print_binary_tree(root)
print(tree) 

s = Solution()
s.bstToGst(root)
print(bt.print_binary_tree(root))