'''
906. Super Palindromes

Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the 
inclusive range [L, R]. 

Example 1:
Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
 
Note:
1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
'''
from math import sqrt, ceil,floor, log10
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        l = int(ceil(sqrt(L)))
        r = int(floor(sqrt(R)))
        i = l
        res = []
        while i <= r:
            if self.checkPalindrome(i):
                sq = i*i
                if self.checkPalindrome(sq):
                    res.append([i,sq])
                    
            i += 1
        return res
        
    def checkPalindrome(self, n):
        ln = int(log10(n))
        isparam = True
        while n > 10:
            u = n % 10
            dv = 10 ** ln
            l = n / dv
            if u != l:
                isparam = False
                break
            n = n%dv
            n = n/10
            ln -= 2
        return isparam


s = Solution()
print(s.superpalindromesInRange(375259531, 1265368034085))
#print(s.checkPalindrome(17161))



