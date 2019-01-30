'''
515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

'''
ALGORITHM:
1. Level order traversal and find max in each level.

RUNTIME COMPLEXITY: (N)
SPACE COMPLEXITY: (N)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
                
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        q = deque()
        q.extend([root,'#'])
        result = []
        temp = []
        while True:
            if len(q) == 1:
                result.append(max(temp))
                break
            node = q.popleft()
            if node == '#':
                q.append('#')
                result.append(max(temp))
                temp = []
            else:
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)   
        return result
