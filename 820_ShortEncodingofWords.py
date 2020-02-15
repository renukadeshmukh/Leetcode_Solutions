'''
820. Short Encoding of Words

Given a list of words, we may encode it by writing a reference string S and a 
list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as 
S = "time#bell#" and indexes = [0, 2, 5]. Then for each index, we will recover 
the word by reading from the reference string from that index until we reach a 
"#" character. What is the length of the shortest reference string S possible 
that encodes the given words?

Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:
1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
'''

'''
ALGORITHM:
1. Reverse every word in the "words" array. This way all suffixes now become 
   prefixes. It is not easy to checl if index of substring is 0
2. Now, sort this new words array. The longers words will come after. example, 
   ["time" , "me"] -> reversed and sorted -> ["em", "emit"]
3. Now starting from backwords, check substring for consecutive words, till 
   substring is found. If not found, add the length of words to answer and update
   indices. 
RUNTIME COMPLEXITY: 
    To reverse = O(N * w) for N words and each word of avg length w.
    To sort = O(N * w * logN) for N words and each word of avg length w.
SPACE COMPLEXITY: O(N * w) for N words and each word of avg length w.
'''

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = [word[::-1] for word in words]
        words.sort()
        
        answer = len(words[-1]) + 1
        i, j = len(words)-1, len(words)-1
        
        while j >= 0:
            if words[i].find(words[j]) != 0:
                i = j
                answer += len(words[j]) + 1
            j -= 1
        return answer
                
                

