'''
1170. Compare Strings by Frequency of the Smallest Character

Let's define a function f(s) over a non-empty string s, which calculates the 
frequency of the smallest character in s. For example, if s = "dcce" then 
f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, 
where each answer[i] is the number of words such that f(queries[i]) < f(W), 
where W is a word in words.

Example 1:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so 
f("cbd") < f("zaaaz").

Example 2:
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query 
both f("aaa") and f("aaaa") are both > f("cc").
 
Constraints:
1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
'''

'''
ALGORITHM:
1. For every word in words, calculate f(word) and store in dict <f(word)>:<count>
2. For every word in queries, 
    Calculate f(query)
    Add up all counts from dict where f(word) > f(query) and append to answer
3. Return answer

RUNTIME COMPLEXITY: O(M*N + N) 
SPACE COMPLEXITY: O(N) for N words
'''

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        fwords = {}
        for word in words:
            freq = self.f(word)
            if freq in fwords:
                fwords[freq] += 1
            else:
                fwords[freq] = 1
                
        answer = []
        for q in queries:
            freq = self.f(q)
            ans = 0
            for fw in fwords:
                if freq < fw:
                    ans += fwords[fw]
            answer.append(ans)
        return answer           
                
        
    def f(self, s):
        freq = 0
        ch = 'z'
        for c in s:
            if c < ch:
                ch = c
                freq = 1
            elif c == ch:
                freq += 1
        return freq
            