'''
784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or 
uppercase to create another string.  Return a list of all possible strings we 
could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''

'''
ALGORITHM:
1. For every letter, form 2 strings, one with lower case and another with upper
case. 
2. For every digit, append the digit as it is. 
3. Once all the characters from S have been processed, append curr to result.
4. Return result.

RUNTIME COMPLEXITY:
SPACE COMPLEXITY: 
'''

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        self.letterCasePermutationHelper(result, "", S)
        return result
        
    def letterCasePermutationHelper(self, result, curr, S):
        if len(S) == 0:
            result.append(curr)
            return
        else:
            if S[0].isdigit():
                self.letterCasePermutationHelper(result, curr + S[0], S[1:])
            else:
                self.letterCasePermutationHelper(result, curr + S[0].lower(), S[1:])
                self.letterCasePermutationHelper(result, curr + S[0].upper(), S[1:])
