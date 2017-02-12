'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of 
characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = len(s)
        l2 = len(t)
        
        if l1 != l2:
            return False
            
        dict = {}
        s_arr = list(s)
        t_arr = list(t)
        res = []
        mapped = set()
        for i in range(l1):
            if s_arr[i] in dict:
                if dict[s_arr[i]] != t_arr[i]:
                    return False
            elif t_arr[i] in mapped:
                return False
            else:
                dict[s_arr[i]] = t_arr[i]
                mapped.add(t_arr[i])
            
        return True
                    
           