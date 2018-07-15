'''
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''

'''
Algorithm:
1. For each character if ascii value >= 65 and <= 90, compute its lowercase

TIME COMPLEXITY: O(n)
'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = []
        for c in str:
            if ord(c) >= 65 and ord(c) <= 90:
                c = chr(ord(c) + 97 -65)
            result.append(c)
        return ''.join(result)