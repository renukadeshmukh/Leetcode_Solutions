'''
717. 1-bit and 2-bit Characters

We have two special characters. The first character can be represented by one bit 0. The second character 
can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character 
or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

'''

'''
Algorithm:
1. bits[i] = 1, count 2 bits (i += 2)
2. else i += 1
3. if i == len-1 and last bit = 0, return True else False
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) -1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if bits[-1] == 0 and i == len(bits) - 1:
            return True
        return False

s = Solution()
res = s.isOneBitCharacter([1, 1, 0])
print(res)

res = s.isOneBitCharacter([1, 1, 1, 0])
print(res)

res = s.isOneBitCharacter([1, 0, 0])
print(res)

res = s.isOneBitCharacter([ 0])
print(res)