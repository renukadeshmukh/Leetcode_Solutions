'''
1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing 
two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is 
guaranteed the answer is unique.

Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and 
equal, and this is the only possible move.  The result of this move is that the 
string is "aaca", of which only "aa" is possible, so the final string is "ca".
 
Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
'''

'''
ALGORITHM:
1. Maintain a stack of unique elements. 
2. For every character c in S, if stack[top] == c, pop c from stack, and skip all
   contiguous character in S that are equal to c
3. Return the remaining stack elements.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        stack.append(S[0])
        for i in range(1, len(S)):
            c = S[i]
            if stack and stack[-1] == c:
                stack.pop()
                while i < len(S) and S[i] == c:
                    i += 1
            else:
                stack.append(c)
        return ''.join( stack)
            