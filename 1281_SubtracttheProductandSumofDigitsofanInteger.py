'''
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its 
digits and the sum of its digits.
 
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:
1 <= n <= 10^5
'''

'''
ALGORITHM:
1. Calculate sum and product of digits of number and return the difference.

RUNTIME COMPLEXITY : O(N), where N = num digitd in n
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sm = 0
        prod = 1
        
        while n > 0:
            rem = n % 10
            n = n/10
            sm += rem
            prod *= rem
        return prod - sm