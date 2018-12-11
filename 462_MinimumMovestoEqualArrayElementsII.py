'''
462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to 
make all array elements equal, where a move is incrementing a selected element
by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''

'''
ALGORITHM:
1. find the median of the array as median is equidistant from both max and min 
    elements in the array.
2. Now every element in array: 
    find diff = abs(median - element), as these many number of moves are needed 
    to make this element equal to median
    res += diff
3. return diff

TIME COMPLEXITY: O(NlogN) for sorting purpose
SPACE COMPLEXITY: (N) for sorting purpose
'''

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums)/2]
        res = 0
        for n in nums:
            res += abs(n-median)
            
        return res
        