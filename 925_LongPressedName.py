'''
925. Long Pressed Name

Your friend is typing his name into a keyboard.  Sometimes, when typing a 
character c, the key might get long pressed, and the character will be typed 1 or 
more times.

You examine the typed characters of the keyboard.  Return True if it is possible 
that it was your friends name, with some characters (possibly none) being long 
pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
'''

'''
ALGORITHM:
1. scan both strings, compare chracters.
2. while characters from both strings match, increment i and j
3. else if typed string has extra repeated characters, inc j till next matching 
   character with name is found
4. else return False
5. After loop completes, check if i == len(name) as well, indicating all characters 
   have been found. Return True else, return False

TIME COMPLEXITY: (N), where n is the size of longer input string
SPACE COMPLEXITY: (1)
'''


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j = 0,0
        l1,l2 = len(name), len(typed)
        while i < l1 and j < l2:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        if i == l1:
            return True
        else:
            return False
                
s = Solution()
s.isLongPressedName("pyplrz", "ppyypllr")