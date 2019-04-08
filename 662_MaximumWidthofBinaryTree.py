'''
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. The binary tree has 
the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the 
leftmost and right most non-null nodes in the level, where the null nodes 
between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 
(5,3,null,9).

Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width is the third level with the length 2 (5,3).

Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width is the second level with the length 2 (3,2).

Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 
(6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
'''

'''
ALGORITHM:
The main idea in this question is to give each node a position value. If we go 
down the left neighbor, then position -> position * 2; and if we go down the 
right neighbor, then position -> position * 2 + 1. This makes it so that when we 
look at the position values L and R of two nodes with the same depth, the width 
will be R - L + 1.

Traverse each node in breadth-first order, keeping track of that node's position. 
For each depth, the first node reached is the left-most, while the last node 
reached is the right-most.

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
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = []
        q.append((root, 0, 0))
        cur_depth = result = start = 0
        for node, depth, pos in q:
            if node:
                q.append((root.left, depth+1, pos*2))
                q.append((root.left, depth+1, pos*2+1))
            if depth != cur_depth:
                cur_depth = depth
                result = max(result, start - pos + 1)
                start = pos
        return result