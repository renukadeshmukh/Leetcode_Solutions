'''
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nstr = '1'
        while n > 1:
            nstr = self.getNext(nstr)
            n -=1
        return nstr
            
    def getNext(self, nstr):
        cnt = 0
        next = ''
        x = nstr[0]
        l1 = len(nstr)
        for i in range(l1):
            if nstr[i] == x:
                cnt += 1
            else:
                next += str(cnt) + str(x)
                cnt = 1
                x = nstr[i]
        next += str(cnt) + str(x)
        cnt = 1
        x = nstr[l1-1]
        
        return next