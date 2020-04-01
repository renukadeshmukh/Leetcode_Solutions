'''
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array 
are smaller than it. That is, for each nums[i] you have to count the number of 
valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100
'''

'''
ALGORITHM:
1. Store [index, num] for every num in an array arr.
2. Sort arr by num
3. Using the sorted version of arr, we get the sorted position of every num. 
4. Using this array, find the original index of the num and add how many 
   elements on the left as the count lesser elements. 
RUNTIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])
            
        arr.sort(key = lambda x: x[0])
        print arr
        result = [0] * len(nums)
        count = 0
        for i in range(1, len(arr)):
            if arr[i][0] == arr[i-1][0]:
                result[arr[i][1]] = result[arr[i-1][1]]
            else:
                result[arr[i][1]] = i
        return result
