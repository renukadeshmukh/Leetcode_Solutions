'''
872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values 
of those leaves form a leaf value sequence. Two binary trees are considered leaf
-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 
are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
'''

'''
ALGORITHM:
1. Get leaf nodes for both trees.
2. Compare of the 2 sets of leaf notes are equal

RUNTIME COMPLEXITY: O(M+N), tree1 has m nodes and tree2 has n nodes
SPACE COMPLEXITY: O(M+N)
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_nodes1 = self.getLeafNodes(root1)
        leaf_nodes2 = self.getLeafNodes(root2)
        if leaf_nodes1 == leaf_nodes2:
            return True
        return False
        

    def getLeafNodes(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root.left == None and root.right == None:
            res.append(root)
        elif root.left != None:
            self.getLeafNodes(root.left, res)
        elif root.right != None:
            self.getLeafNodes(root.right, res)
        return res
        


