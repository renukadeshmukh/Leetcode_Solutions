'''
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of 
alphabet on only one row's of American keyboard.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

'''
ALGORITHM
1. For 3 rows in keyboard, create 3 sets for characters from each row.
2. Check if every word belongs to one set only. 

RUNTIME COMPLEXITY: O(N*M) for n words of avg length m
SPACE COMPLEXITY: O(26*2) to store capital and small letters
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set(['q', 'Q', 'w','W', 'e','E', 'r','R', 't','T', 'y','Y', 'u','U', 'i','I', 'o','O', 'p','P'])
        set2 = set(['a','A', 's','S', 'd','D', 'f','F', 'g','G', 'h','H', 'j','J', 'k','K', 'l', 'L'])
        set3 = set(['z','Z', 'x','X', 'c','C', 'v','V', 'b','B', 'n','N', 'm','M'])
    
        result = []
        for word in words:
            snum = self.whichSet(word[0], set1, set2, set3)
            f = True
            if snum == 1:
                for c in word:
                    if c not in set1:
                        f = False
                        break
            elif snum == 2:
                for c in word:
                    if c not in set2:
                        f = False
                        break
            else:
                for c in word:
                    if c not in set3:
                        f = False
                        break
            if f:
                result.append(word)
                
        return result
        
        
    def whichSet(self, c, set1, set2, set3):
        if c in set1:
            return 1
        elif c in set2:
            return 2
        else:
            return 3