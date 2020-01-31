'''
230. Kth Smallest Element in a BST 

Given a binary search tree, write a function kthSmallest to find the kth smallest 
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to 
find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

'''
ALGORITHM:
1. Property of BST : inorder traversal of BST is an array sorted in the 
   ascending order.
2. Traverse BST tree in inorder traversal and return the kth element. 

RUNTIME COMPLEXITY : O(N)
SPACE COMPLEXITY: O(N) for stack space. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nums = [0, 0]
        self.inorder(root, nums, k)
        return nums[1]
        
    def inorder(self, root, nums, k):
        if root == None:
            return
        
        self.inorder(root.left, nums, k)
        nums[0] += 1
        if nums[0] == k:
            nums[1] = root.val
            return
        self.inorder(root.right, nums, k)
        