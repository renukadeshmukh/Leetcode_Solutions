'''
179. Largest Number

Given a list of non negative integers, arrange them such that they form the 
largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an 
integer.
'''

'''

ALGORITHM:
1. Convert int array to string array
2. Sort the array in reverse order. 
    NOTE: the sorting function is important. y+x > x+y 
    e.g. ["3", "30", "9"] => [ "9", "30", "3"]
3. Convert the array into string and return the string

RUNTIME COMPLEXITY: O(nlogn) for sorting 
SPACE COMPLEXITY: O(N) for sorting (python uses timsort)
'''

def numeric_compare(x, y):
    if x+y > y+x:
        return -1
    return 1
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        nums = sorted(nums, cmp=numeric_compare)
        if nums[0] == "0":
            return "0"
        return ''.join(nums)
        