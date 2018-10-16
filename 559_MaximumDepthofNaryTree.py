'''
559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node.

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
'''

'''
ALGORITHM:
1. BFS Traversal. 

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        q = deque()
        q.extend([root, "#"])
        maxDepth = 1
        while len(q) > 1:
            node = q.popleft()
            if node == "#":
                maxDepth += 1
                q.append("#")
            elif node.children:
                for c in node.children:
                    q.append(c)        
        return maxDepth