'''
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
'''

class Solution(object):
    
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c = word[0]

        if not self.isCapital(c):
            return self.allSmall(word)
        else:
            word = word[1:]
            flag = self.allSmall(word)
            if not flag:
                return self.allCapital(word)
            return True
                
    def allCapital(self, word):
        for c in word:
            if not self.isCapital(c):
                return False
        return True
        
    def allSmall(self, word):
        for c in word:
            if self.isCapital(c):
                return False
        return True
        
    def isCapital(self, c):
        asci = ord(c)
        if  asci >= 65 and asci <= 90:
            return True
        return False
