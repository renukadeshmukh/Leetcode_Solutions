'''
1390. Four Divisors

Given an integer array nums, return the sum of divisors of the integers in that 
array that have exactly four divisors. If there is no such integer in the array, 
return 0.

Example 1:
Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
 
Constraints:
1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
'''

'''
ALGORITHM:
1. Find divisors for each number. If num divisors == 4, sum the divisors and 
   and the sum to the answer.
2. Return answer. 

RUNTIME COMPLEXITY: O(N* Sqrt(N))
SPACE COMPLEXITY: O(1)
'''

from math import sqrt 
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for n in nums:
            sm = self.getSum(n)
            answer += sm
        return answer
    
    def getSum(self, num):
        nsqrt = sqrt(num)
        divisors = set([1, num])
        
        i = 2
        while len(divisors) <= 5 and i <= nsqrt:
            rem = num%i
            if rem == 0:
                divisors.add(i)
                divisors.add(num/i)
            i += 1
        if len(divisors) == 4:
            return sum(divisors)
        return 0