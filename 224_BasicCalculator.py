'''
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + 
or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sm = 0
        stack = []

        for c in s:
            if c == '+':
                stack.append(0)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                sm_local = 0
                x = 0
                stack.append(c)
            elif c == '-':
                stack.append(c)
            elif c >= '0' and c <= '9':
                if stack and type(stack[-1]) == int:
                    stack[-1] = stack[-1] * 10 + int(c)
                elif stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(int(c) * -1)
                else:
                    stack.append(int(c))

        print(stack)
    
  

s = Solution()
#print(s.calculate("1 + 1"))
#print(s.calculate(" 2-1 + 2 "))
#print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
print(s.calculate("(11+(2+5+20)-3)+(6+88)"))