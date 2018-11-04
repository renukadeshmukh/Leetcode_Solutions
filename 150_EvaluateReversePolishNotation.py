'''
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid 
operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always 
evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

'''
ALGORITHM:
1. If operator push on stack else if operand, pop 2 elements from stack, evaluate
the result, and push the result back on stack
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from math import floor, ceil
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stk.pop()
                a = stk.pop()
                res = self.evaluate(a,b, token)
                stk.append(res)
            else:
                stk.append(int(token))
        return stk[0]
                
    def evaluate(self, a, b, op):
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
        else:
            q = a/(b * 1.0)
            res = floor(q) if q > 0 else ceil(q)
            return int(res)

s = Solution()
#print(s.evalRPN(["2", "1", "+", "3", "*"]))
#print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))