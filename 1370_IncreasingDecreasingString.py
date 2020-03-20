'''
1370. Increasing Decreasing String

Given a string s. You should re-order the string using the following algorithm:

. Pick the smallest character from s and append it to the result.
. Pick the smallest character from s which is greater than the last appended 
  character to the result and append it.
. Repeat step 2 until you cannot pick more characters.
. Pick the largest character from s and append it to the result.
. Pick the largest character from s which is smaller than the last appended 
  character to the result and append it.
. Repeat step 5 until you cannot pick more characters.
. Repeat the steps from 1 to 6 until you pick all characters from s.
. In each step, If the smallest or the largest character appears more than once 
  you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the 
mentioned algorithm.

Example 3:
Input: s = "leetcode"
Output: "cdelotee"

Example 4:
Input: s = "ggggggg"
Output: "ggggggg"

Example 5:
Input: s = "spo"
Output: "ops"

Constraints:
1 <= s.length <= 500
s contains only lower-case English letters.
'''

'''
ALGORITHM:
1. Store cnt of each character in an arr of length 26. 
2. Following the algorithm in the problem statement to generate the answer. 

RUNTIME COMPLEXITY: ?
SPACE COMPLEXITY: O(26)
'''

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = len(s)
        arr = [0] * 26
        result = []
        for c in s:
            arr[ord(c)-97] += 1
       
        while cnt > 0:
            for i in range(26):
                if arr[i] > 0:
                    result.append(chr(i+97))
                    arr[i] -= 1
                    cnt -= 1
            for i in range(25, -1, -1):
                if arr[i] > 0:
                    result.append(chr(i+97))
                    arr[i] -= 1
                    cnt -= 1
                    
        return ''.join(result)


