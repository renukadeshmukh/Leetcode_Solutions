'''
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements 
into the memory at once?
'''

'''
ALGORITHM:
1. Insert both arrays into dictionary
2. Iterate on smaller array. 
3. If key in both arrays insert the key min(small[key], large[key]) in result array

RUNTIME COMPLEXITY : O(N) where n is size of larger array
SPACE COMPLEXITY : (M + N) where m and n are size of respective arrays.
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = self.to_dict(nums1)
        dict2 = self.to_dict(nums2)
        res = []
        if len(dict1) < len(dict2):
            small = dict1
            large = dict2
        else:
            small = dict1
            large = dict2
        
        for key in small:
            if key in large:
                arr = [key] * min(small[key], large[key])
                res.extend(arr)
        return res
        
    def to_dict(self, nums):
        my_dict = {}
        for n in nums:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1
        return my_dict
