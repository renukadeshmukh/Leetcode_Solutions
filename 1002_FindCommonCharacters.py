'''
1002. Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of 
all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you 
need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

'''
ALGORITHM:
1. Maintain count of each character in each word.
2. Take minimum of all occurance counts for each character and add the character
   to result array minimum times. 

RUNTIME COMPLEXITY: O(M*N) for N words with average length M
SPACE COMPLEXITY: O(26 * N) = O(N)

'''


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        char_map = {}
        for i in range(len(A)):
            for c in A[i]:
                if c not in char_map:
                    char_map[c] = [0] * len(A)
                char_map[c][i] += 1
                
        result = []
        for c in char_map:
            count = min(char_map[c])
            result.extend([c] * count)
        return result
