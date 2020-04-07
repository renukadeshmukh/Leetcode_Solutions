'''
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given a number s in their binary representation. Return the number of steps to 
reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It's guaranteed that you can always reach to one for all testcases.

Example 1:
Input: s = "1101"
Output: 6

Example 2:
Input: s = "10"
Output: 1

Example 3:
Input: s = "1"
Output: 0

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
'''

'''
ALGORITHM:
1. Traverse the string in reverse
2. For every char, carry = carry & s[i] (carry = 1, if both carry and s[i] are 1)
3. And digit at ith place = carry ^ s[i] (if carry and s[i] are 1, digit will be 0)
4. Thus if digit is 0, increment result by 1 (for even digits)
5. If digit is 1, then increment the result by 2 (once for adding 1 and making 
   last digit even and then dividing by 2). And carry = 1
6. Repeat for all characters in s

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        carry = 0
        stack = [int(c) for c in s]  
        result = 0
        
        for i in range(len(s)-1, 0, -1):
            n = int(s[i])
            carry, sm = carry&n, carry^n
            if sm == 0:
                result += 1
            else:
                carry = 1
                result += 2   
        if carry:
            result += 1               
        return result
    

s= Solution()
print(s.numSteps("11000"))
print(s.numSteps("1101"))
print(s.numSteps("10"))
print(s.numSteps("1"))
