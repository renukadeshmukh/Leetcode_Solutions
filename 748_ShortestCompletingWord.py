'''
748. Shortest Completing Word

Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. 
Such a word is said to complete the given string licensePlate Here, for letters we ignore case. For example, "P" on 
the licensePlate still matches "p" on the word. It is guaranteed an answer exists. If there are multiple answers, 
return the one that occurs first in the array. The license plate might have the same letter occurring multiple times. 
For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.

Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
'''

'''
ALGORITHM:
1. create license map for licensePlate
2. create word map for each word.
3. compare both dict to check if match is possible.


Runtime Complexity : O(n*m) for n words with average length m
Space Complexity : O(n*m) for n words with average length m
'''
import sys
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license_map = {}
        licensePlate = licensePlate.lower()
        for c in licensePlate:
            if (c >= 'a' and c <= 'z'):
                if c in license_map:
                    license_map[c] += 1
                else:
                    license_map[c] = 1
                
        result = ''
        min_len = sys.maxint
        for word in words:
            if len(word) < min_len:
                word_map = self.build_map_for_map(word)
                compare = self.compare_licensemap_and_wordmap(license_map, word_map)
                if compare:
                    result = word
                    min_len = len(word)
        return result

    def compare_licensemap_and_wordmap(self, license_map, word_map):
        flag = True
        for key in license_map:
            if not (key in word_map and license_map[key] <= word_map[key]):
                flag = False
                break
        return flag

    def build_map_for_map(self, line):
        line_map = {}
        for c in line:
            if c in line_map:
                line_map[c] += 1
            else:
                line_map[c] = 1
        return line_map
        

s = Solution()
res = s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
print(res)
res = s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])
print(res)