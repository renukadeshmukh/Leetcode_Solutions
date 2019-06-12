'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

'''
ALGORITHM:
Ref: https://www.youtube.com/watch?v=YcJTyrG3bZs
1. At each point of constructing the string of length 2k we make a choice.
2. We can place a "(" and recurse or we can place a ")" and recurse.
3. But we can't just do that placement, we need 2 critical pieces of information.
    The amount of left parens left to place.
    The amount of right parens left to place.
4. We have 2 critical rules at each placement step.
    We can place a ( if we have more than 0 left to place.
    We can only place a ) if there are left parentheses that we can match 
    against. We know this is the case when we have less left parentheses to 
    place than right parentheses to place.
5. Once we establish these constraints on our branching we know that when we 
   have 0 of both parens to place that we are done, we have an answer in our base 
   case.

TIME COMPLEXITY:O( pow(N,4)/sqrt(N) )
SPACE COMPLEXITY:  O(N)
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateParenthesisRecursive(result, "", 0, 0, n)
        return result


    def generateParenthesisRecursive(self, result, well_formed_paren, open, close, n):
        if len(well_formed_paren) == 2*n:
            result.append(well_formed_paren)
        if open < n:
            self.generateParenthesisRecursive(result, well_formed_paren + '(', 
                                              open+1, close, n)
        if close < open:
            self.generateParenthesisRecursive(result, well_formed_paren + ')', 
                                              open, close+1, n)
        
s = Solution()
print(s.generateParenthesis(3))