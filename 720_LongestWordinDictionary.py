'''
720. Longest Word in Dictionary
'''

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key=lambda x: len(x) )
        word_set = set(words)
        result = words[-1]
        for i in range(len(words)-1, -1, -1):
            if words[i] in word_set and self.checkLongestWord(words[i], word_set):
                return words[i]
        return ""
                
                
    def checkLongestWord(self, word, word_set):
        for i in range(len(word)):
            if word[:i+1] in word_set:
                word_set.remove(word[:i+1])
            else:
                return False
        return True

s = Solution()
print(s.longestWord(["w","wo","wor","worl","world"]))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple", "balls"]))