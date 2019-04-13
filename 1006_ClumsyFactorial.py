'''
1006. Clumsy Factorial

Normally, the factorial of a positive integer n is the product of all positive 
integers less than or equal to n.  For example, 
factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we 
swap out the multiply operations for a fixed rotation of operations: 
multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, 
these operations are still applied using the usual order of operations of 
arithmetic: we do all multiplication and division steps before any addition or 
subtraction steps, and multiplication and division steps are processed left to 
right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 
equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns 
the clumsy factorial of N.

Example 1:
Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

Example 2:
Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 
Note:
1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)
'''

'''
ALGORITHM:
We can easily observe below:

5 * 4 / 3 = 6
6 * 5 / 4 = 7
10 * 9 / 8 = 11
...
...
...
so we can get this formula: i * (i-1) / (i-2) = i+1 when i >= 5

we can simplify our computation as below:

    i * (i-1) / (i-2) + (i-3) - (i-4) * (i-5) / (i-6) + (i-7) - (i-8) * .... + rest elments
=   (i+1) + "(i-3)" - "(i-4) * (i-5) / (i-6)" + "(i-7)" - "(i-8) * " .... + rest elments
=   (i+1) + "(i-3) - (i-3)" + "(i-7) - (i-7)" +  ....  + rest elments
=   (i+1) + rest elments

we can call each 4 numbers a chunk, so from N // 4 we can know how many chunks 
there are, then the rest 0, 1, 2 and 3 elements will influence our final result.

when 0 element left: final result is (i+1) + ... + 5 - (4*3/2) + 1, which is i+1
when 1 element left: final result is (i+1) + ... + 6 - (5*4/3) + 2 - 1, which is i+2
when 2 element left: final result is (i+1) + ... + 7 - (6*5/4) + 3 - 2 * 1, which is i+2
when 3 element left: final result is (i+1) + ... + 8 - (7*6/5) + 4 - 3 * 2 / 1, which is i-1

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

from collections import deque
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        elif N <= 4:
            return N+3
        elif N % 4 == 0:
            return N + 1
        elif N % 4 == 3:
            return N - 1
        else:
            return N + 2
