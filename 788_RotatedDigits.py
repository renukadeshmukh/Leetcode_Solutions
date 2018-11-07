'''
788. Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we 
get a valid number that is different from X.  Each digit must be rotated - we 
cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 
rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, 
and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
'''

'''
ALGORITHM (for faster algorithm):
1. For num in range 1 to N:
    2. Convert number to string = str_num
    3. If 3,4 or 7 in str_num, return false
    4. else if 2,5,6 or 9 in str_num, inc result
4. return result

RUNTIME COMPLEXITY: O(N*K) where k is avg length of num
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    #Faster and more performant
    def rotatedDigitsNew(self, N):
    """
    :type N: int
    :rtype: int
    """
    count=0
    for num in range(1,N+1):
        s =str(num) 
        if '3' in s or '4' in s or'7' in s :
            continue
        elif '2' in s or '5' in s or'6' in s or '9' in s:
            count+=1   
    return count

    #slower
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1,N+1):
            if self.check_valid(i):
                res += 1
        return res
    
    def check_valid(self, num):
        n = num
        mul = 0
        res = 0
        while n > 0:
            rem = n%10
            r = self.rotate(rem)
            if r == -1:
                return False
            res += (10**mul)* r
            n = n/10
            mul += 1
        return res != num
            
    def rotate(self, x):
        if x in [0,1,8]:
            return x
        elif x in [2,5]:
            return x^2^5
        elif x in [6,9]:
            return x^6^9
        else:
            return -1

s = Solution()
print(s.rotatedDigits(10))