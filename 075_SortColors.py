'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in the 
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, 
respectively.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
 
Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
'''

'''
ALGORITHM:
This is a Dutch Flag problem. 

1. Keep three indices low = -1, mid = 0 and high = N and there are four ranges, 
   0 to low (the range containing 0), low to mid (the range containing 1), 
   mid to high (the range containing unknown elements) and high to N (the range 
   containing 2).
2. Traverse the array from start to end and mid is less than high. 
3. If the element is 0 then swap the element with the element at index low and 
   update low = low + 1 and mid = mid + 1
4. If the element is 1 then update mid = mid + 1
5. If the element is 2 then swap the element with the element at index high and 
update high = high – 1. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        low, mid, high = -1, 0, len(nums)
        
        while mid < high:
            if nums[mid] == 0:
                low += 1
                nums[low], nums[mid] = nums[mid], nums[low] 
                mid += 1
            elif nums[mid] == 2:
                high -= 1
                nums[high], nums[mid] = nums[mid], nums[high] 
            else:
                mid += 1