'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

'''
'''
Solution 1:
Sort each string. Keep adding each string to the hashmap based of the sorted key value. 
Return the values of the hashmap

Solution 2: (Better)
Assign a prime number to each character. Iterate on the string and find product of the values
represented as the string. All anagrams will have the same product value
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        map = {}
        
        for s in strs:
            s1 = ''.join(sorted(s))
            if s1 not in map:
                map[s1] = []
            map[s1].append(s)
        
        return map.values()