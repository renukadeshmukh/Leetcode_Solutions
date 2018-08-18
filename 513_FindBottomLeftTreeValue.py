'''
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''

'''
Algorithm:
1. Level Order Traversal and keep updating leftmost
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return root
        q = deque()
        q.extend([root, '$'])
        leftmost = root.val

        while len(q) > 1:
            node = q.popleft()
            if node == '$':
                q.append('$')
                leftmost = q[0].val
            else:
                if node.left != None:
                    q.append(node.left) 
                if node.right != None:
                    q.append(node.right) 
        return leftmost

t2 = TreeNode(2)
t1 = TreeNode(1)
t3 = TreeNode(3)

t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1. left = t2
t1.right = t3
t1.left.left = t4
t1.right.left = t5
t1.right.right = t6
t1.right.left.left = t7

s = Solution()
print(s.findBottomLeftValue(t1))