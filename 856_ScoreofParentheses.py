'''
856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on 
the following rule:

> () has score 1
> AB has score A + B, where A and B are balanced parentheses strings.
> (A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6
 
Note:
S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
'''

'''
ALGORITHM:
1. For every '(' push it on the stack
2. For every ')', If top element on stack is '(', then pop the '(' and append 1, 
   because () = 1
3. For every ')', if top element on stack is not '('. then pop all element till
    '(' and add team. Because AB = A+B. Now pop the '(' also and append 2*sm to
    the stack. Because (A) = 2*A
4. Finally, return sum(stack), i.e. sum of all numbers on stack. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        stack = []
        open, close = '(', ')'
        for c in S:
            if c == open:
                stack.append(c)
            else:
                if stack[-1] == open:
                    stack[-1] = 1
                else:
                    num = 0
                    while stack and stack[-1] != open:
                        num += stack.pop()
                    stack[-1] = 2*num
        return sum(stack)

s = Solution()
print(s.scoreOfParentheses("()(())(())"))
print(s.scoreOfParentheses("(()(()))()"))
print(s.scoreOfParentheses("()"))
print(s.scoreOfParentheses("(())"))
print(s.scoreOfParentheses("()()"))
print(s.scoreOfParentheses("(()(()))"))