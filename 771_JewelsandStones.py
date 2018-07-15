'''
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones
you have.  Each character in S is a type of stone you have.  You want to know how many of the stones 
you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case 
sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

'''
Algorithm:
1. Put all characters from J in a set as reading from a set is O(1) time
2. Iterate on S and increment count if each stone is present in J

TIME COMPLEXITY: O(m) + O(n) -> where m = length of J and n = length of S
SPACE COMPLEXITY: O(m) -> where m = length of J
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        for c in J:
            jewels.add(c)
        jewel_cnt = 0
        for c in S:
            if c in J:
                jewel_cnt += 1
        return jewel_cnt