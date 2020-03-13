'''
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 
Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

'''
ALGORITHM:
1. Use Level order traversal to add levels. Return the sum of last level. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque([root, '#'])
        cur_sm = 0
        while len(q) > 1:
            elem = q.popleft()
            if elem == '#':
                q.append('#')
                cur_sm = 0
            else:
                cur_sm += elem.val
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
                
        
        return cur_sm

