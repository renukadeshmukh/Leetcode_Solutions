'''
884. Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated 
words.  Each word consists only of lowercase letters.) A word is uncommon if it 
appears exactly once in one of the sentences, and does not appear in the other 
sentence. Return a list of all uncommon words. 

You may return the list in any order.
Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:
0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''

'''
ALGORITHM:
1. Maintain 2 sets, one for new words and one for words encountered a second time.
2. Return set difference of new - old.

RUNTIME COMPLEXITY: O(m + n), where m and n are lengths of A and B
SPACE COMPLEXITY: (m + n)
'''

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        new = set()
        old = set()
        a = A.split()
        b = B.split()
        for w in a + b:
            if w not in new:
                new.add(w)
            else:
                old.add(w)
        return list(new.difference(old))
        
