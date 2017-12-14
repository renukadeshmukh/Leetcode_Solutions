'''
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary 
words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). 
Please reload the code definition to get the latest changes. 

'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        st = set()
        for word in wordDict:
            if word not in st:
                st.add(word)
                
        return self.word_break(s, st, False)
    
    def word_break(self, s, st, flag):
        print s
        if s in st:
            return True
        else:
            lng = len(s)
            for i in range(lng):
                print s[:i]
                if s[:i] in st:
                    flag = (self.word_break(s[i:], st, flag) or flag)
        return flag
    
    
    def word_break_iter(self, s, st, flag):
        print s
        if s in st:
            return True
        else:
            i=0
            lng = len(s)
            while i < lng:
                print s[i:]
                if s[:i] in st:
                    s = s[i:]
                    lng = len(s)
        
            
s = Solution()
print s.wordBreak("codes", ["leet","code"])   

mystr = "hello"
print mystr[0:1] 
