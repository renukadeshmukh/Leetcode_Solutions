'''
423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of 
digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. 
That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
'''

'''
ALGORITHM:
The idea is:

for zero, it's the only word has letter 'z',
for two, it's the only word has letter 'w',
......
so we only need to count the unique letter of each word, Coz the input is always valid.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [0] * 10
        for c in s:
            if c == 'z':
                res[0] += 1
            elif c == 'w':
                res[2] += 1
            elif c == 'u':
                res[4] += 1
            elif c == 'x':
                res[6] += 1
            elif c == 'g':
                res[8] += 1
            elif c == 'o':
                res[1] += 1
            elif c == 'h':
                res[3] += 1
            elif c == 'f':
                res[5] += 1
            elif c == 's':
                res[7] += 1
            elif c == 'i':
                res[9] += 1
                
        res[1] = res[1] - res[0] - res[2] - res[4]
        res[3] = res[3] - res[8]
        res[5] = res[5] - res[4]
        res[7] = res[7] - res[6]
        res[9] = res[9] - res[5] - res[6] - res[8]
        answer = []
        for i in range(10):
            if res[i]:
                answer.append(str(i)*res[i])
        return ''.join(answer)
                