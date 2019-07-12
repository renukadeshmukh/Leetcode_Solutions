'''
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a 
height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following 
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

'''
ALGORITHM:
1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for internal recursion stack
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


from helpers.binary_tree_helper import BinaryTree
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        
        return self.sortedArrayToBSTHelper(nums, 0, len(nums)-1)
    
    def sortedArrayToBSTHelper(self, nums, left, right):
        if left > right:
            return None
       
        mid = left + (right - left)//2
        cur_head = TreeNode(nums[mid])
        cur_head.left = self.sortedArrayToBSTHelper(nums, left, mid-1)
        cur_head.right = self.sortedArrayToBSTHelper(nums, mid+1, right)
        return cur_head

s = Solution()
head = s.sortedArrayToBST([-10,-3,0,5,9])
