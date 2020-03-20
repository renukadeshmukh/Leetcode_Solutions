'''
1362. Closest Divisors

Given an integer num, find the closest two integers in absolute difference whose 
product equals num + 1 or num + 2. Return the two integers in any order.

Example 1:
Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, 
the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:
Input: num = 123
Output: [5,25]

Example 3:
Input: num = 999
Output: [40,25]
 
Constraints:
1 <= num <= 10^9
'''

'''
ALGORITHM:
1. n = sqrt(num+2)
2. For x=n to 0, the first set of divisors we find for num+1 or num+2, will be 
   closest in absolute difference. 

RUNTIME COMPLEXITY: O(SQRT(NUM))
SPACE COMPLEXITY: O(1)
'''

from math import sqrt
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num1, num2 = num+1, num+2
        n = int(sqrt(num2))
        
        for x in range(n, -1, -1):
            if num1%x == 0:
                return [x, num1/x]
            
            if num2%x == 0:
                return [x, num2/x]

s = Solution()
print(s.closestDivisors(8))
print(s.closestDivisors(123))
print(s.closestDivisors(999))