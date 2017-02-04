'''

204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

'''

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        result = 0
        buffer = [None]*n

        i = 2
        sqrtn = math.sqrt(n)
        while i < sqrtn:
            if buffer[i] != -1:
                buffer = self.updateBuffer(buffer, i, n)
            i+=1
        for x in buffer:
            if x == None:
                result += 1
        
        return result - 2
        
    def updateBuffer(self, buffer, dv, n):
        i = dv*dv
        while i < n:
            buffer[i] = -1
            i += dv
        return buffer
