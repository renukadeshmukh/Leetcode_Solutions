'''
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to 
English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

Constraints:
1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
'''

'''
ALGORITHM:
1. Use stack to store single integers. 
2. Every time you encounter #, pop the last 2 integers, concatenate and push 
   back on the stack.
3. Now convert every entry in the stack into a character, join the array and 
   return the answer. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if c == '#':
                c1, c2 = stack.pop(), stack.pop()
                stack.append(c2+c1)
            else:
                stack.append(c)
        for i in range(len(stack)):
            stack[i] = chr(int(stack[i]) + 96)
        return ''.join(stack)