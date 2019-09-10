'''
859. Buddy Strings

Given two strings A and B of lowercase letters, return true if and only if we 
can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''

'''
ALGORITHM:
1. If len(A) != len(B), return False
2. Compare characters at same index in A and B
3. If cjaracters are different in more than 3 places, return False
4. If characters are different in exactly 2 places, check if they can be swapped.
   If yes, return True, else return False
5. If characters are not different in any place, check if A has repeated 
   characters that can be swapped, by using set. If yes, return True else False.
   
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) => for set(A)
'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        diff_cnt = 0
        a1,a2,b1,b2 = '','','',''
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_cnt += 1
                if diff_cnt > 2:
                    return False
                if diff_cnt == 1:
                    a1, b1 = A[i], B[i]
                else:
                    a2, b2 = A[i], B[i]
        if diff_cnt == 0:
            return len(A) != len(set(A))
        else:
            return a1 == b2 and b1 == a2
                