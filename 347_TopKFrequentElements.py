'''
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the 
array's size.
'''

'''
ALGORITHM:
1. Count frequency of each element and store in a dictionary <elem>:<count>
2. Reverse the dictionary <count> : <element list with this count>
3. Create a list from reverse_dictionary starting with most frequent elements
   first
4. Return the first k elements


RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        k_arr = []
        n_map = defaultdict(int)
        reverse_n_map = defaultdict(list)
        
        for n in nums:
            n_map[n] += 1
          
        for key in n_map:
            reverse_n_map[n_map[key]].append(key)
        
        for i in range(len(nums), 0, -1):
            if i in reverse_n_map:
                k_arr.extend(reverse_n_map[i])
        return k_arr[:k]
        
        
        

