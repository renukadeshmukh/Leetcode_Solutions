'''
848. Shifting Letters

We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
'''

'''
RUNTIME COMPLEXITY : O(n)
SPACE COMPLEXITY : O(1)
'''

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        sm = sum(shifts[0:len(shifts)])
        sm1 = 0
        res = []
        for i in xrange(len(S)):
            x = (ord(S[i]) - 97 + sm) % 26 + 97
            c = str(unichr(x))
            sm -= shifts[i]
            res.append(c)
        return ''.join(res)

s = Solution()
print(s.shiftingLetters('abc', [3,5,9]))