'''
762. Prime Number of Set Bits in Binary Representation

Given two integers L and R, find the count of numbers in the range [L, R] 
(inclusive) having a prime number of set bits in their binary representation.
(Recall that the number of set bits an integer has is the number of 1s present 
when written in binary. For example, 21 written in binary is 10101 which has 3 
set bits. Also, 1 is not a prime.)

Example 1:
Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Example 2:
Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
'''

'''
ALGORITHM:
1. For each number from L to R, find out how many set bits it has. If that number 
   is 2, 3, 5, 7, 11, 13, 17, 19, 23 or 29 then we add one to our count.
   
RUNTIME COMPLEXITY: O(D), where D = R-Lis the number of integers considered. 
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2,3,5,7,11,13,17,19,23,29,31}
        answer = 0
        for n in range(L, R+1):
            if bin(n).count('1') in primes:
                answer += 1
        return answer
