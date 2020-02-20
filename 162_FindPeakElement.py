'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one 
of the peaks is fine. You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index 
number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak 
element is 2, or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''

'''
ALGORITHM:
1. Scan left to right looking for the peak element. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
Nore:- Can be done in O(LogN) using binary search approach

'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        i = 0
        while i < len(nums)-1 and nums[i] < nums[i+1]:
            i += 1
        return i

    '''
    We use a modification of this simple Binary Search to our advantage. We start 
    off by finding the middle element, midmid from the given numsnums array. If 
    this element happens to be lying in a descending sequence of numbers. or a 
    local falling slope(found by comparing nums[i]nums[i] to its right neighbour), 
    it means that the peak will always lie towards the left of this element. 
    Thus, we reduce the search space to the left of midmid(including itself) and 
    perform the same process on left subarray.

    If the middle element, midmid lies in an ascending sequence of numbers, or a 
    rising slope(found by comparing nums[i]nums[i] to its right neighbour), it 
    obviously implies that the peak lies towards the right of this element. 
    Thus, we reduce the search space to the right of midmid and perform the same 
    process on the right subarray.

    In this way, we keep on reducing the search space till we eventually reach a 
    state where only one element is remaining in the search space. This single 
    element is the peak element.
    '''    
    def findPeakElementLogarithmic(self, nums) :
        l = 0
        r = len(nums) - 1;
        while l < r :
            int mid = (l + r) / 2;
            if nums[mid] > nums[mid + 1]:
                r = mid;
            else
                l = mid + 1;
        return l;
    
        