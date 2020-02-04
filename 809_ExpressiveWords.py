'''
809. Expressive Words

Sometimes people repeat letters to represent extra feeling, such as 
"hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we 
have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal 
to S by any number of applications of the following extension operation: choose 
a group consisting of characters c, and add some number of characters c to the 
group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to 
get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 
3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  
If S = "helllllooo", then the query word "hello" would be stretchy because of 
these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 
or more.

Notes:
0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
'''

'''
ALGORITHM:
For each word check if S is a stretchy version or not. Return count of 
stretchy words.
To check if a word is stretchy or not, follow the following algorithm:
1. Iterate on S and word using a while loop
2. If S[i] != word[j] => return False
3. Let S[i] == word[j] == c
4. Count number of consecutive characters == c in both S and word. Keep 
   incrementing i and j. Store the counts in cnt1 and cnt2
5. If cnt1 == cnt2, contnue 
5. If cnt1 < cnt2, S does not have enough characters to complete word. => Return 
   False
6. If cnt1 > cnt2 but cnt1 < 3, => return False (ground size should ne atleast 3)
7. Once the while loop complete, verify that end is reached for both S and word.
8. If yes, return True else return False

RUNTIME COMPLEXITY: O(KN) where K is num words and N is len(largest word)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        answer = 0
        for word in words:
            if self.checkWord(S, word):
                answer += 1
        return answer
        
        
    def checkWord(self, s, word):
        i, j = 0, 0
        valid = True
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                c = s[i]
                cnt1, cnt2 = 1, 1
                i, j = i+1, j+1    
                while i < len(s) and s[i] == c:
                    i += 1
                    cnt1 += 1
                while j < len(word) and word[j] == c:
                    j += 1
                    cnt2 += 1
                if cnt1 < cnt2 or (cnt1 != cnt2 and cnt1 < 3):
                    valid = False
                    break 
                
            else:
                valid = False
                break
        if i == len(s) and j == len(word):
            return valid
        return False



s = Solution()
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))