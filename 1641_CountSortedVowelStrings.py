'''
1641. Count Sorted Vowel Strings

Given an integer n, return the number of strings of length n that consist only 
of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as 
or comes before s[i+1] in the alphabet. 

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
 
Constraints:
1 <= n <= 50 
'''

'''
ALGORITHM
If we know all the string of len k, so the string of len k + 1 will be
1 Add a before all string of len k
2 Add e before the string of len k, which is starts with or after e
3 Add i before the string of len k, which starts with or after i
4 Add o before the string of len k, which starts with or after o
5 Add u before the string of len k, which starts with or after u

RUNTIME COMPLEXITY O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        memoized_matrix = [[0 for i in range(5)] for j in range(n+1)]
                
        for i in range(n+1):
            for j in range( 4, -1, -1):
                if i == 0:
                    memoized_matrix[i][j] = 1
                elif j == 4:
                    memoized_matrix[i][j] = 1
                else:
                    memoized_matrix[i][j] = memoized_matrix[i-1][j] + memoized_matrix[i][j+1] 
        
        return memoized_matrix[n][0]
                
s = Solution()
print(s.countVowelStrings(1))
print(s.countVowelStrings(4))