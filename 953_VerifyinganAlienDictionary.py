'''
953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but 
possibly in a different order. The order of the alphabet is some permutation of 
lowercase letters.

Given a sequence of words written in the alien language, and the order of the 
alphabet, return true if and only if the given words are sorted lexicographicaly 
in this alien language. 

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], 
hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is 
shorter (in size.) According to lexicographical rules "apple" > "app", because 
'l' > '∅', where '∅' is defined as the blank character which is less than any 
other character (More info).
 
Note:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
'''

'''
ALGORITHM:
1. Store the order in a dictionary by assigning an increasing value to character
   in order.
2. For every pair of 2 words, check if they are in lexicographic order. 

RUNTIME COMPLEXITY: O(N * C) For N word of average length C
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = self.get_order_lookup(order)
        for i in range(len(words)-1):
            if not self.compare(words[i], words[i+1], order_dict):
                return False
        return True
    
    def get_order_lookup(self, order):
        order_dict = {}
        i = 0
        for c in order:
            order_dict[c] = i
            i += 1
        return order_dict
    
    def compare(self, word1, word2, order_dict):
        min_ln = min(len(word1), len(word2))
        print min_ln
        
        for i in range(min_ln):
            if word1[i] == word2[i]:
                continue
            elif order_dict[word1[i]] < order_dict[word2[i]]:
                return True
            else:
                return False
        return len(word1) < len(word2)