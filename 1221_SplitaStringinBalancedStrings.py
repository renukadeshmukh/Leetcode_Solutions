'''
1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains 
same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 
Constraints:
1 <= s.length <= 100
'''

'''
ALGORITHM:
1. For each char in s, maintain count of L and R.
2. Everytime l_cnt == r_cnt, ic result by 1
3. Return result.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l_cnt, r_cnt = 0, 0
        result = 0
        for c in s:
            if c == 'L':
                l_cnt += 1
            else:
                r_cnt += 1
            if l_cnt == r_cnt:
                result += 1
        return result
                
        