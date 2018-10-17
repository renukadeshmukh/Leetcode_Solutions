'''
429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, 
from left to right, level by level).

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
'''

'''
ALGORITHM:
Same approach as Level order traversal for Binary Tree. 

RUNTIME COMPLEXITY : O(N)
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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """       
        if root == None:
            return []
        q = deque()
        res = []
        tmp = []
        q.extend([root, "#"])
        while len(q) > 1:
            node = q.popleft()
            if node == "#":
                q.append("#")
                res.append(tmp)
                tmp = []
            else:
                tmp.append(node.val)
                if node.children:
                    for c in node.children:
                        q.append(c)  
        res.append(tmp)
        return res 


