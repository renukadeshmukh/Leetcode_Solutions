'''
623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a 
row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree 
nodes N in depth d-1, create two tree nodes with value v as N's left subtree root 
and right subtree root. And N's original left subtree should be the left subtree 
of the new left subtree root, its original right subtree should be the right 
subtree of the new right subtree root. If depth d is 1 that means there is no 
depth d-1 at all, then create a tree node with value v as the new root of the 
whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
'''

'''
ALGORITHM:
1. If d = 1, put the whole current tree as a left child of the newly added node.
2. For inserting the new node at appropriate level, we can start by making a 
   call to insert with the root node and 1 as the current level. Inside every 
   such call, we check if we've reached one level prior to the level where the 
   new node needs to be inserted.

   From this level, we can store the roots of the left and right subtrees of the 
   current node temporarily, and insert the new node as the new left and right 
   subchild of the current node, with the temporarily stored left and right 
   subtrees as the left and right subtrees of the newly inserted left or right 
   subchildren appropriately.

   But, if we haven't reached the destined level, we keep on continuing the 
   recursive calling process with the left and right children of the current 
   node respectively. At every such call, we also incrmenet the depth of the 
   current level to reflect the depth change appropriately.
   
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
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        self.addNode(root, v, d, 1)
        return root
        
    def addNode(self, root, v, d, cur_d):
        if cur_d + 1 == d:
            left = root.left
            right = root.right
            root.left = TreeNode(v)
            root.left.left = left
            root. right = TreeNode(v)
            root.right.right = right
            
        if root.left != None:
            self.addNode(root.left, v, d, cur_d + 1)
        if root.right != None:
            self.addNode(root.right, v, d, cur_d + 1)