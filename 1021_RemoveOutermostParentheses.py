'''
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where 
A and B are valid parentheses strings, and + represents string concatenation.  
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses 
strings.

A valid parentheses string S is primitive if it is nonempty, and there does not 
exist a way to split it into S = A+B, with A and B nonempty valid parentheses 
strings.

Given a valid parentheses string S, consider its primitive decomposition: 
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in 
the primitive decomposition of S.
 
Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition 
"(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is 
"()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 
Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
'''

'''
ALGORITHM:
1. Iterate on the string and keep track of count of open and close brackets.
2. If c == '(' and open_count == close_count, skip this bracket
3. If c == ')' and open_count == close_count, skip this bracket

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for storing result 
'''

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        opn, close = 0,0
        result = []
        for c in S:
            if c == '(':
                opn += 1
                if opn-1 != close:
                    result.append(c)
            else:
                close += 1
                if opn != close:
                    result.append(c)    
        return ''.join(result)
        
