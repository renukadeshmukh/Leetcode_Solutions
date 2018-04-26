'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        
        q = deque()
        q.extend([root,'#'])
        result = []
        temp = []
        while True:
            if len(q) == 1:
                result.append(temp)
                break
            node = q.popleft()
            if node == '#':
                q.append('#')
                result.append(temp)
                temp = []
            else:
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)   
        return result
        