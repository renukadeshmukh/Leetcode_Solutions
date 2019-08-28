'''
942. DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), 
let N = S.length. Return any permutation A of [0, 1, ..., N] such that for all 
i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1] 

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]

Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
'''

'''
ALGORITHM:
1. Keep track of the smallest and largest element we haven't placed. 
   low = 0, high = len(S)
2. If we see an 'I', place the small element; otherwise place the large element.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low, high = 0, len(S)
        result = []
        for i in range(len(S)):
            if S[i] == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result