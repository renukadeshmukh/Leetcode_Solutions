'''
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node 
values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's 
descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s == None or t == None:
            return False
        
        return self.preorderTraversal(s, t)

    def preorderTraversal(self, s, t):
        if s == None:
          return;
        res = False
        if s.val == t.val:
            res = self.checkSameTree(s, t)
            if res:
                return res
            else:
                print(s.val)

        #then recur on left sutree 
        if not res:
            self.preorderTraversal(s.left, t) 

            #now recur on right subtree
            self.preorderTraversal(s.right, t)
        return resx

    def checkSameTree(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        elif tree1 == None or tree2 == None:
            return False
        elif tree1.val != tree2.val:
            return False
        else:
            return self.checkSameTree(tree1.left, tree2.left) and  self.checkSameTree(tree1.right, tree2.right)

sol = Solution()

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

print(sol.isSubtree(s,t))