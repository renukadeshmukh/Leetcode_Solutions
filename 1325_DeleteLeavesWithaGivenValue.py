'''
1325. Delete Leaves With a Given Value

Given a binary tree root and an integer target, delete all the leaf nodes with 
value target.
Note that once you delete a leaf node with value target, if it's parent node 
becomes a leaf node and has the value target, it should also be deleted (you 
need to continue doing that until you can't).

Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed  
After removing, new nodes become leaf nodes with value (target = 2)

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:
Input: root = [1,1,1], target = 1
Output: []

Example 5:
Input: root = [1,2,3], target = 1
Output: [1,2,3]

Constraints:
1 <= target <= 1000
Each tree has at most 3000 nodes.
Each node's value is between [1, 1000].
'''

'''
ALGORITHM:
1. Recursively call removeLeafNodes on the left and right.
2. If root.left == root.right == null and root.val == target,
   the root node is now a leaf with value = target, we return null.
3. Otherwise return root node itself.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY : O(HEIGHT)
'''

from helpers.binary_tree_helper import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root.left != None:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right != None:
            root.right = self.removeLeafNodes(root.right, target)
            
        if root.left == None and root.right == None and root.val == target:
            return None
        else:
            return root 
        
s = Solution()
root = BinaryTree.build_binary_tree([1,2,3,2,None,2,4])
root = s.removeLeafNodes(root, target = 2)
tree = BinaryTree.print_binary_tree(root)
print(tree)