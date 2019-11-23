'''
640. Solve the Equation

Solve a given equation and return the value of x in the form of string "x=#value". 
The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".
If there are infinite solutions for the equation, return "Infinite solutions".
If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:
Input: "x=x"
Output: "Infinite solutions"

Example 3:
Input: "2x=x"
Output: "x=0"

Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:
Input: "x=x+2"
Output: "No solution"
'''

'''
ALGORITHM:
1. Start by splitting the given equation based on = sign. This way, we've separated 
   the left and right hand side of this equation. 
2. Once this is done, we need to extract the individual elements(i.e. x's and the 
   numbers) from both sides of the equation. Put the separated parts into an array.
3. Sum all numbers and x coefficients on lhs and rhs separately. Thus we have 
   x1, n1, x2, and n2.
4. x1-x2 and n2-n1( note n2-n1 is because n1 is moved to rhs while x2 is moved to lhs).
5. If x=0 and n=0, infinite solutions are possible. 
   If x=0 but n!=0, no solution is possible.
   else return "x=n/coeff_of_x"

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        eqs = equation.split("=")
        if len(eqs) != 2:
            return "No solution"
        lhs, rhs = eqs[0], eqs[1]
        x1, n1 = self.parse(lhs)
        x2, n2 = self.parse(rhs)

        x = x1 - x2
        n = n2 - n1        

        if x == 0 and n == 0:
            return "Infinite solutions"
        elif x == 0 and n != 0:
            return "No solution"
        else:
            n = n//x
            return  "x={0}".format(n)

    def parse(self, eqs):
        eqs = eqs.replace("-", "+-")
        eqs = eqs.split("+")
        x, n = 0, 0
        for eq in eqs:
            if not eq:
                continue
            elif eq[-1] == 'x':
                coeff = self.get_coeff(eq[:-1])
                x += coeff
            else:
                n += int(eq)
        return (x,n) 

    def get_coeff(self, param):
        coeff = 1
        if param:
            if param == '-':
                coeff = -1
            else:
                coeff = int(param)
        return coeff


s = Solution()
print(s.solveEquation("-x=-1"))
print(s.solveEquation("x+5-3+x=6+x-2"))
print(s.solveEquation("x=x"))
print(s.solveEquation("2x=x"))
print(s.solveEquation("2x+3x-6x=x+2"))
print(s.solveEquation("x=x+2"))

