'''
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 
and 128 % 8 == 0. Also, a self-dividing number is not allowed to contain the 
digit zero.

Given a lower and upper number bound, output a list of every possible self 
dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''

'''
ALGORITHM:
1. For each numberi n the range, check if it is self dividing

RUNTIME COMPLEXITY: O(N), where N is the length if range
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        while left <= right:
            if self.isSelfDividingNumbers(left):
                res.append(left)
            left += 1
        return res

    def isSelfDividingNumbers(self, n):
        n1, flag = n, True
        while n > 0:
            units = n % 10
            if units == 0 or n1 % units != 0:
                flag = False
                break
            n = n/10
        return flag 

print(Solution().selfDividingNumbers(1, 22))