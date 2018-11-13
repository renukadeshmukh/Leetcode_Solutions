'''
594. Longest Harmonious Subsequence

We define a harmonious array is an array where the difference between its maximum 
value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious 
subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''

'''
ALGORITHM
1. Iterate on the array and count occurance of each number and save it to dict1
2. Iterate on dict1 and for each key, check if key+1 is also present
    mx_cnt = max(mx_cnt , dict1[key]+dict1[key1])
    
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for n in nums:
            if n not in dict1:
                dict1[n] = 0
            dict1[n] += 1
        
        mx_cnt = 0
        for key in dict1:
            key1 = key+1
            if key1 in dict1:
                mx_cnt = max(mx_cnt , dict1[key]+dict1[key1])
                
        return mx_cnt
                    
                
        