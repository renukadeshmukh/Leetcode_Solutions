'''
260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that 
appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:
The order of the result is not important. So in the above example, [5, 3] is 
also correct.
Your algorithm should run in linear runtime complexity. Could you implement it 
using only constant space complexity?
'''

'''
ALGORITHM:
1. Suppose that a and b are the numbers that occur once. 
2. XOR all numbers. Because all other numbers occur twice, XOR-ing them will 
   cancel them out. We are left with XOR of a and b.
3. Find the right most set bit in this xor. That means, starting from right, 
   this is the first bit that is different in a and b. all other but in the 
   right are same. 
4. Create a mask, with only this bit set and all other bits being 0. 
5. Maintain 2 variables a and b to get the 2 single numbers. 
5. Iterate over all numbers in nums again. BITWISE AND the mask and each 
   number. If num & mark == 0, XOR num with a else XOR num with b
6. After this iteration a and b will contain the two single occuring nums. 
7. Return [a, b]

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n
        
        mask = 1
        while True:
            if xor & mask == 0:
                mask = mask << 1
            else:
                break
        
        a, b = 0, 0
        for n in nums:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        return [a,b]


s = Solution()
print(s.singleNumber([-1139700704,-1653765433]))
print(s.singleNumber([-1,-1,2,3]))
print(s.singleNumber([-1,2,3,3]))


