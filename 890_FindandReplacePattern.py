'''
890. Find and Replace Pattern

You have a list of words and a pattern, and you want to know which words in 
words matches the pattern. A word matches the pattern if there exists a 
permutation of letters p so that after replacing every letter x in the pattern 
with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: 
every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 
You may return the answer in any order. 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 
Note:
1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
'''

'''
ALGORITHM:
1. maintain a lookup for word->pattern and rev_lookup for pattern->word
2. if a character in lookup or rev_look is already mapped, do not consider it

RUNTIME COMPLEXITY: O(N*M), where n is the number of words and m is length of each word 
SPACE COMPLEXITY: (N*M), where n is the number of words and m is length of each word
'''
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(word) == len(pattern):
                lookup = {}
                rev_lookup = {}
                flag = True
                for i in range(len(pattern)):
                    w,p = word[i], pattern[i]
                    if w not in lookup and p not in rev_lookup:
                        lookup[w] = p
                        rev_lookup[p] = w
                    elif w in lookup and p not in rev_lookup:
                        flag = False
                        break
                    elif w not in lookup and p in rev_lookup:
                        flag = False
                        break
                    else:
                        if lookup[w] != p and rev_lookup[p] != w:
                            flag = False
                            break
                if flag:
                    res.append(word) 
        return res
                        
        