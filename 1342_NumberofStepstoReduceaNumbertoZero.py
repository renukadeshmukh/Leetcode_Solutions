'''
1342. Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to 
zero. If the current number is even, you have to divide it by 2, otherwise, you 
have to subtract 1 from it.

Example 1:
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:
Input: num = 8
Output: 4

Example 3:
Input: num = 123
Output: 12
 
Constraints:
0 <= num <= 10^6
'''

'''
ALGORITHM:
1. While num > 0, if number is even, divide by 2, else substract 1. Inc steps
   for every operation
RUNTIME COMPLEXITY: 
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2 == 0:
                num = num/2
            else:
                num -= 1
            steps += 1
            
        return steps