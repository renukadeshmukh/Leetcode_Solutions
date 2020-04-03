'''
592. Fraction Addition and Subtraction

Given a string representing an expression of fraction addition and subtraction, 
you need to return the calculation result in string format. The final result 
should be irreducible fraction. If your final result is an integer, say 2, you 
need to change it to the format of fraction that has denominator 1. So in this 
case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"

Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:
Input:"1/3-1/2"
Output: "-1/6"

Example 4:
Input:"5/3+1/3"
Output: "2/1"

Note:
>The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
>Each fraction (input and output) has format ±numerator/denominator. If the 
first input fraction or the output is positive, then '+' will be omitted.
>The input only contains valid irreducible fractions, where the numerator and 
denominator of each fraction will always be in the range [1,10]. If the 
denominator is 1, it means this fraction is actually an integer in a fraction 
format defined above.
>The number of given fractions will be in the range [1,10].
>The numerator and denominator of the final result are guaranteed to be valid 
and in the range of 32-bit int.
'''

'''
ALGORITHM:
RUNTIME COMPLEXITY:
SPACE COMPLEXITY: 
'''
from math import sqrt
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression = expression.replace('-', '+-')
        parts = expression.split('+')
        all_denominators = set()
        numerator, denominator = 0, 1
        
        for part in parts:
            if part:
                n, d = part.split('/')
                n, d = int(n), int(d)
                numerator = (numerator * d + n * denominator)
                if d not in all_denominators:
                    all_denominators = \
                        all_denominators.union(self.getPrimeFactors(d))
                denominator = denominator * d
                
        return self.reduceFraction(numerator, denominator, all_denominators)

    def getPrimeFactors(self, num):
        if num == 1: return set()
        factors = set()
        factors.add(num)
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                factors.add(i)
                factors.add(num//i)
        return factors

    def reduceFraction(self, numerator, denominator, all_denominators):
        for d in all_denominators:
            while numerator % d == 0 and denominator % d == 0:
                numerator, denominator = numerator//d, denominator//d
        return "{0}/{1}".format(numerator, denominator)

s = Solution()
print(s.fractionAddition("-7/2-7/9+3/2-9/10+3/8+1/2-3/10-1/1-2/1+8/3"))
print(s.fractionAddition("-5/1+8/1+1/1"))
print(s.fractionAddition("-1/2+1/2"))
print(s.fractionAddition("-1/2+1/2+1/3"))
print(s.fractionAddition("1/3-1/2"))
print(s.fractionAddition("5/3+1/3"))
print(s.fractionAddition("7/3+5/2-3/10"))
print(s.fractionAddition("5/2+2/9-5/6"))