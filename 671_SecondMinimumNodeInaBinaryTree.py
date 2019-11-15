'''
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative 
value, where each node in this tree has exactly two or zero sub-node. If the node 
has two sub-nodes, then this node's value is the smaller value among its two 
sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) 
always holds.

Given such a binary tree, you need to output the second minimum value in the set 
made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''

'''
ALGORITHM:
1. Perform in-order traversal. 
2. Maintain first and second min values and keep on updating for each node 
   visited.
3. Return the second_min found. If not then return -1. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(H), where h is height of the tree, for recursion stack
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys  
class Solution(object):
    def __init__(self):
        self.min1  = sys.maxint
        self.min2 = sys.maxint
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #print self.min1, self.min2
        if root:
            self.findSecondMinimumValue(root.left)
            print self.min1, self.min2
            if root.val < self.min1:
                self.min1, self.min2 = root.val, self.min1
            elif root.val > self.min1 and root.val < self.min2:
                self.min2 = root.val
            self.findSecondMinimumValue(root.right)
        if self.min2 == sys.maxint:
            return -1
        return self.min2
            
        