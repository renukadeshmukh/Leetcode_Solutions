'''
1313. Decompress Run-Length Encoded List

We are given a list nums of integers representing a list compressed with run-length 
encoding. Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] 
(with i >= 0).  For each such pair, there are a elements with value b in the 
decompressed list. Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we 
generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4,4] is [2,4,4,4]. 

Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
'''

'''
ALGORITHM:
1. Iterate on the array and re-create the original array by appending required
   number of elements for each entry in list. 

Consider list of size N and final result of size M
RUNTIME COMPLEXITY: O(M*N)
SPACE COMPLEXITY: O(M*N)
'''

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for i in range(0, len(nums), 2):
            result.extend([nums[i+1]] * nums[i])
        return result