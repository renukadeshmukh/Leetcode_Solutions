'''
814. Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every 
node's value is either a 0 or a 1. Return the same tree where every subtree (of 
the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant 
of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:
The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
'''

'''
ALGORITHM:
1. Prune children of the tree recursively. The only decisions at each node are 
whether to prune the left child or the right child.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        self.pruneTreeHelper(root)
        return root
                
    def pruneTreeHelper(self, root):
        if root.left == None and root.right == None:
            return root.val
        else:
            left,right = 0,0
            if root.left != None:
                left = self.pruneTreeHelper(root.left)
                if left == 0:
                    root.left = None
            if root.right != None:
                right = self.pruneTreeHelper(root.right)
                if right == 0:
                    root.right = None
            return left + right + root.val


