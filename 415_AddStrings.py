'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

'''
RUNTIME COMPLEXITY: O(n) where n is the size of larger string
SPACE COMPLEXITY: O(n) to build the result
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        carry = 0
        i = len(num1)-1
        j = len(num2)-1
        res = []
        while i >= 0  or j >= 0:
            sm = 0
            if i > -1:
                sm += ord(num1[i]) - 48
                i -= 1
            if j > -1:
                sm += ord(num2[j]) - 48
                j -= 1
            if carry:
                sm += 1
            carry, sm = sm/10, sm%10  
            res.append(str(sm))
        
        if carry:
            res.append('1')
        return ''.join(reversed(res))
        

s =  Solution()
print(s.addStrings('9999', '99'))
