'''
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars. A string is good if 
it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.
 
Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Note:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
'''

'''
ALGORITHM:
1. Count all characters in chars
2. For each word in words, count characters and check if all these characters 
are present in chars
3. If yes, add length of word to result 

RUNTIME COMPLEXITY: O(n*w + l)
                    n = number of words
                    w = avg. word length
                    l = length of chars 
SPACE COMPLEXITY: O(n*w + l)
                    n = number of words
                    w = avg. word length
                    l = length of chars 
'''

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        store = Counter(chars)
        result = 0
        for word in words:
            chr_cnt = Counter(word)
            diff = chr_cnt-store
            if not diff:
                result += len(word)
        return result
