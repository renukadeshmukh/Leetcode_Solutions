'''
967. Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference 
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the 
number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is 
valid.

You may return the answer in any order.
 
Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
Note:
1 <= N <= 9
0 <= K <= 9
'''

'''
ALGORITHM:
1. An N digit number is just an N-1 digit number with a final digit added. 
2. If the N-1 digit number ends in a digit d, then the N digit number will end in 
d−K or d+Kd+K (provided these are digits in the range [0,9]). 
3. Also, we should be careful about leading zeroes -- only 1 digit numbers will 
start with 0.

RUNTIME COMPLEXITY: O(2^N)
SPACE COMPLEXITY: O(2^N)
'''

from collections import deque
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        q = deque()
        for i in range( 10):
            q.append(i)
        if N == 1:
            return list(q)
        q.popleft()
        for i in range(N-1):
            q_len = len(q)
            for j in range(q_len):
                elem = q.popleft() 
                units = elem % 10
                n1 = units + K
                n2 = units - K
                if n1 < 10:
                    q.append(elem * 10 + n1)
                if n2 >= 0 and n2 != n1:
                    q.append(elem * 10 + n2)
        return list(q)

s = Solution()
print(s.numsSameConsecDiff(3, 7))
print(s.numsSameConsecDiff(2, 1))