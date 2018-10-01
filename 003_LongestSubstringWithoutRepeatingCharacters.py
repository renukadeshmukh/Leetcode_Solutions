'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a 
substring, "pwke" is a subsequence and not a substring.
'''


from Queue import *


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = Queue(maxsize=0)
        chars = set()
    
        maxlen  = 0
        endIndx = -1
        indx = -1
        for c in s:
            indx += 1
            if c in chars:
                flag = True
                if q.qsize() > maxlen:
                    maxlen = q.qsize()
                    endIndx = indx
                while flag:
                    ch = q.get()
                    chars.remove(ch)
                    if ch == c:
                        flag = False
    
            chars.add(c)
            q.put(c)
    
        return max(maxlen, q.qsize())
