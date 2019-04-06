'''
970. Powerful Integers

Given two positive integers x and y, an integer is powerful if it is equal to 
x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur 
at most once.

Example 1:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Note:
1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
'''

'''
ALGORITHM:
BRUTE FORCE
1. x_pow_arr = Find all powers of x <= bound
2. y_pow_arr = Find all powers of y <= bound
3. Check all (a,b) sums in x_pow_arr and y_pow_arr <= bound

RUNTIME COMPLEXITY: O(log^2 bound)
SPACE COMPLEXITY: O(log^2 bound)
'''
class Solution(object):
    
    def getPowerArray(self, z, bound):
        pow_arr = [1]
        zp = 1
        if z != 1:
            while zp <= bound:
                zp = zp * z
                pow_arr.append(zp)
        return pow_arr
        
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_pow_arr = self.getPowerArray(x, bound)
        y_pow_arr = self.getPowerArray(y, bound)
                
        result = set()
        for a in x_pow_arr:
            for b in y_pow_arr:
                sm = a + b
                if sm <= bound:
                    result.add(sm)
                else:
                    break
                    
        return list(result)

