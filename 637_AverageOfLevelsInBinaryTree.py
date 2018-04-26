'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [root.val]
        
        result = []
        total = 0
        cnt = 0
        q = deque()
        q.extend([root, '#'])
        while True:
            if len(q) is 1:
                avg = total/cnt
                result.append(avg)
                break
            node = q.popleft()
            if node is '#':
                q.append('#')
                avg = total/cnt
                result.append(avg)
                total = 0
                cnt = 0
            else:
                total += node.val
                cnt += 1
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
        return result
                
        