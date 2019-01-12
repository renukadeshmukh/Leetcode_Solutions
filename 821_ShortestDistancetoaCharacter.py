'''
821. Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the 
shortest distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 
Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''

'''
ALGORITHM:
1. Initialize a result array with int.max of size N
2. for i in [0:N]
3.      if char is C, then set res[i] = 0
4.      keep updating distance in res in both directions (i-1, i+1 and so on) 
5. do this for all occurances of C
6. return res

RUNTIME COMPLEXITY: O(N*P) where P is the number of C in S
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        res = [10005] * len(S)
        
        for i in range(len(S)):
            if S[i] == C:
                res[i] = 0
                j, k = i-1, i+1
                while j >= 0 and S[j] != C:
                    res[j] = min(i-j, res[j])
                    j -= 1
                while k < len(S) and S[k] != C:
                    res[k] = min(k-i, res[k])
                    k += 1
        return res
                                 

