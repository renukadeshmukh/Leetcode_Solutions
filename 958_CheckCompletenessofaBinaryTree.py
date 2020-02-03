'''
958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely 
filled, and all nodes in the last level are as far left as possible. It can have 
between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values 
{1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as 
possible.

Example 2:
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:
The tree will have between 1 and 100 nodes.
'''

'''
ALGORITHM:
1. Modified Level Order Traversal
2. Keep traversing the tree in level order. For first Null node, update a flag 
   to mark that first flag is encounerted. 
3. If any non-Null node is seen after a Null node is seen, return False. 
4. After the entire tree is traversed return True indicating a complete binary
   tree. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        end = False
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
        
        