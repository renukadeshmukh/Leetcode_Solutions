'''
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each 
line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as 
you can in each line. Pad extra spaces ' ' when necessary so that each line has 
exactly maxWidth characters. Extra spaces between words should be distributed as 
evenly as possible. If the number of spaces on a line do not divide evenly 
between words, the empty slots on the left will be assigned more spaces than the 
slots on the right.
For the last line of text, it should be left justified and no extra space is 
inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

'''
ALGORITHM:
1. Find out how many words can fir in a line of width = maxwidth
2. Apply login for justification

RUNTIME COMPLEXITY: O(N) where n is total number of characters
SPACE COMPLEXITY: O(N) where n is total number of characters.
'''

from math import ceil
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        tmp = [words[0]]
        lng = len(words[0])
        word_cnt = 1
        line_len = lng
        for word in words[1:]:
            if lng + len(word)  < maxWidth:
                tmp.append(' ')
                tmp.append(word)
                word_cnt += 1
                lng += (len(word) + 1) 
                line_len += len(word)
            else:
                result.append(self.justify(tmp, word_cnt, line_len, maxWidth))
                lng = len(word)
                tmp = [word]
                word_cnt = 1
                line_len = len(word)
                
        result.append(self.leftJustify(tmp, maxWidth))
        return result
    
    def justify(self, arr, num_words, length, maxwidth):
        diff = maxwidth - length 
        num_words -= 1

        if num_words == 0:
            return arr[0] + (' ' * diff)
        
        used_space = 0
        for i in range(1, len(arr), 2):
            spaces =  int(ceil(diff/(num_words)))
            arr[i] = (' ' * spaces)
            diff -= spaces
            num_words -= 1
        return ''.join(arr)
    
    def leftJustify(self, arr, maxwidth):
        line = ''.join(arr)
        diff = maxwidth - len(line)
        return line + (' ' * diff)
            



s = Solution()

words = ["This", "is", "an", "example", "of", "text", "justification."]
print(s.fullJustify(words, 16))
words = ["What","must","be","acknowledgment","shall","be"]
print(s.fullJustify(words, 16))

words = words = ["Science","is","what","we","understand","well","enough","to",
                "explain", "to","a","computer.","Art","is","everything","else",
                "we","do"]
print(s.fullJustify(words, 20))

words = ["Listen","to","many,","speak","to","a","few."]
print(s.fullJustify(words, 6))
