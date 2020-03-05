'''
318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. You may assume that each word 
will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
'''

'''
ALGORITHM:
1. For every word calculate a mask and store in an array.
   The mask is calculated by setting the ord(c) - 97 bit, for every character
   in word.
2. For every set of 2 words in input if words[i] & words[j] == 0, that means, 
   they do not contain any common characters. Calculate the product of length 
   of these 2 words and keep track of max_product. 

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(N) where N = len of input array
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        ln = len(words)
        mask_arr = [0] * ln
        for i in range(ln):
            mask = 0
            for c in words[i]:
                mask = mask | (1 << ord(c)-97)
            mask_arr[i] = mask
                
        max_prod = 0
        for i in range(ln-1):
            for j in range(i+1, ln):
                if mask_arr[i] & mask_arr[j] == 0:
                    max_prod = max(max_prod, len(words[i] * len(words[j])))
        return max_prod
            
s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(s.maxProduct(["a","aa","aaa","aaaa"]))