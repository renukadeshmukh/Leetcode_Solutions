'''
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array 
is defined as follow:
The root is the maximum number in the array.
> The left subtree is the maximum tree constructed from left part subarray 
   divided by the maximum number.
> The right subtree is the maximum tree constructed from right part subarray 
   divided by the maximum number.
> Construct the maximum tree by the given array and output the root node of this 
   tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''

'''
ALGORITHM:
We make use of a function construct(nums, start, end), which returns the maximum 
binary tree consisting of numbers within the indices start and end in the given 
nums array(excluding the rth element).

The algorithm consists of the following steps:
1. Start with the function call construct(nums, 0, n). Here, n refers to the 
   number of elements in the given numsnums array.
2. Find the index, k of the largest element in the current range of indices 
   (start:end). Make this largest element as the local root node.
3. Determine the left child using construct(nums, start, k). Doing this 
   recursively finds the largest element in the subarray left to the current 
   largest element.
4. Similarly, determine the right child using construct(nums, k+1, end).
5. Return the root node to the calling function.


RUNTIME COMPLEXITY: O(N^2)  The function construct() is called n times. At each 
level of the recursive tree, we traverse over all the n elements to find the 
maximum element. In the average case, there will be a nlogn levels leading to a 
complexity of O(nlogn). In the worst case, the depth of the recursive tree can 
grow upto n, which happens in the case of a sorted numsnums array, giving a 
complexity of O(N^2).
SPACE COMPLEXITY: O(n)
'''

from helpers.binary_tree_helper import BinaryTree 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct(nums, 0, len(nums))
        
    def construct(self, nums, start, end):
        if start >= end:
            return None
        else:
            mx, k = -1, -1
            for i in range(start, end):
                if nums[i] > mx:
                    mx = nums[i]
                    k = i
            node = TreeNode(mx)
            node.left = self.construct(nums, start, k)
            node.right = self.construct(nums, k+1, end)
            return node


s = Solution()
root = s.constructMaximumBinaryTree([3,2,1,6,0,5])

bt = BinaryTree()
print(bt.print_binary_tree(root))