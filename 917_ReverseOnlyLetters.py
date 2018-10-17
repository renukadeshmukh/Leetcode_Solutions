'''
917. Reverse Only Letters

Given a string S, return the "reversed" string where all characters that are not
a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
'''

'''
ALGORITHM:
1. Convert string to char array
2. i = 0 and j = len(S) - 1
3. if both S[i] and S[j] are alpha, swap them, increment i, decrement j
4. else if S[i] is alpha, decrement j
5. else increment i
6. join and return the char array 

RUNTIME COMPLEXITY: O(N) where N is length of string
SPACE COMPLEXITY: O(N), where an extra array is used to build the result 
'''

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        arr, i, j = list(S), 0, len(S)-1
        while i < j:
            flag1, flag2 = arr[i].isalpha(), arr[j].isalpha()
            if  flag1 and flag2:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif flag1:
                j -= 1
            else:
                i += 1
        return ''.join(arr)
        

