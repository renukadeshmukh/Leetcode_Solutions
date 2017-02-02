
'''
485. Max Consecutive Ones   

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''

class Solution(object):
    '''
    Count consecutive 1s and keep updating the max
    '''
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        temp = 0
        for n in nums:
            if n == 1:
                temp+=1
            else:
                max1 = max(temp, max1)
                temp=0
                
        return max(temp, max1)
