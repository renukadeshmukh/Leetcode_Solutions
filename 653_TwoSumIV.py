'''
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two 
elements in the BST such that their sum is equal to the given target.

Input:                                     Input:
    5                                         5
   / \                                       / \
  3   6                                     3   6                                    
 / \   \                                   / \   \
2   4   7                                 2   4   7

Target = 9                               Target = 9

Output: True                             Output: False
'''

'''
Solution:
Using HashSet
If the sum of two elements x + yx+y equals kk, and we already know that xx exists 
in the given tree, we only need to check if an element yy exists in the given tree, 
such that y = k - xy=k−x. Based on this simple catch, we can traverse the tree in 
both the directions(left child and right child) at every step. We keep a track of 
the elements which have been found so far during the tree traversal, by putting them 
into a setset.

For every current node with a value of pp, we check if k-pk−p already exists in the 
array. If so, we can conclude that the sum kk can be formed by using the two elements 
from the given tree. Otherwise, we put this value pp into the setset.

If even after the whole tree's traversal, no such element pp can be found, the sum kk 
can't be formed by using any two elements.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.traverse(root, k, set(), False)
    
    def traverse(self, root, k , st, flag):
        if root == None:
            flag = False
            return flag
        elif root != None:
            val = root.val
            if k - val in st:
                flag = True
                return flag
            else:
                st.add(val)
                
            return flag or 
                   self.traverse(root.left, k, st, flag) or 
                   self.traverse(root.right, k, st, flag) 