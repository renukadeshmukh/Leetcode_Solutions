'''
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lst = list()
        while n > 0:
            n -= 1
            rem = n % 26
            lst.insert(0, chr(rem + 65))
            n = n/26
        return ''.join(lst)