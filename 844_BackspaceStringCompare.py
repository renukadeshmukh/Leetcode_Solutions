'''
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''

'''
ALGORITHM:
1. Maintain two stacks and keep updating for every operation. 
2. Compare if the stacks are equal. 

Better approach:
Maintain two pointers instead of maintaining auxillary space. 

RUNTIME COMPLEXITY: O(M+N)
SPACE COMPLEXITY: O(M+N)
'''

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s,t = [],[]
        for c in S:
            if c == '#' and s:
                s.pop()
            elif c != '#':
                s.append(c)
                
        for c in T:
            if c == '#' and t:
                t.pop()
            elif c != '#':
                t.append(c)

        return s == t

