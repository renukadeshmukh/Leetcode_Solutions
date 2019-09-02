'''
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''

'''
ALGORITHM:
1. Apply same algorithm as Fibonacci. But instead of adding last 2 elements, 
   add last 3 and store the result in a memoized array.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        store = [0, 1, 1]
        if n <= 2:
            return store[n]
        i = 3
        while i <= n:
            store.append(store[i-1] + store[i-2] + store[i-3])
            i += 1
        return store[n]
