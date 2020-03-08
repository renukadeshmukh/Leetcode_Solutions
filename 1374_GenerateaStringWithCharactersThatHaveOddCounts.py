'''
1374. Generate a String With Characters That Have Odd Counts

Given an integer n, return a string with n characters such that each character 
in such string occurs an odd number of times. The returned string must contain 
only lowercase English letters. If there are multiples valid strings, return any 
of them.  
 
Example 1:
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times 
and the character 'z' occurs once. Note that there are many other valid strings 
such as "ohhh" and "love".

Example 2:
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. 
Note that there are many other valid strings such as "ag" and "ur".

Example 3:
Input: n = 7
Output: "holasss"
 
Constraints:
1 <= n <= 500
'''

'''
ALGORITHM: 
1. If n is odd, return return a string of a.....a of length n
2. If b is even, return a string on (n-1) a and b (a.....ab)
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n-1) + 'b'
