'''
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of 
the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum 
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the 
node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        elif t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

        
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)
t4 = TreeNode(5)

t1.left = t2
t1.right = t3
t1.left.left = t4

t5 = TreeNode(2)
t6 = TreeNode(1)
t7 = TreeNode(3)
t8 = TreeNode(4)
t9 = TreeNode(7)
t5.left = t6
t5.right = t6
t5.left.right = t8
t5.right.right = t9

s = Solution()
res = s.mergeTrees(t1, t5)
print(res)