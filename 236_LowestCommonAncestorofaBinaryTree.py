'''
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in 
the tree. According to the definition of LCA on Wikipedia: “The lowest common 
ancestor is defined between two nodes p and q as the lowest node in T that has 
both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4] 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of 
itself according to the LCA definition.
 
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

'''
ALGORITHM:
1. This is a bottom up approach where the base case is
2. If the root is null then return null.
3. If the one of the nodes(p or q) is root, then return root.
4. Now we find the left node and the right node by recursively calling 
lowestCommonAncestor on left, right subtrees and check if :
 > Both left and right are not null, then root is the lowest common ancestor.
 > If left is null then both the nodes are in right subtree and the right node 
   is the LCA.
 > If right is null then both nodes are in the left subtree and the left node is 
   the LCA.
   
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        elif root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left == right == None:
            return None
        elif left != None and right != None:
            return root
        elif left == None:
            return right
        else:
            return left
