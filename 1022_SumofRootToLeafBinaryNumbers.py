'''
1022. Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path 
represents a binary number starting with the most significant bit.  For example, 
if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, 
which is 13.

For all leaves in the tree, consider the numbers represented by the path from 
the root to that leaf.
Return the sum of these numbers. 

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''

'''
ALGORITHM:
1. Find all path from root to leaves. DFS recursion should help do that.
2. For generating numbers binary -> decimal, num * 2 + root.val

RUNTIME COMPLEXITY: O(N) for N nodes in tree
SPACE COMPLEXITY: O(1)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0
        
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.sumRootToLeafHelper(root, 0)
        return self.total
        
    def sumRootToLeafHelper(self, root, num):
        num = num * 2 + root.val
        if root.left == None and root.right == None:
            self.total += num
            return
        if root.left != None:
            self.sumRootToLeafHelper(root.left, num)
        if root.right != None:
            self.sumRootToLeafHelper(root.right, num)
                        

