'''
791. Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more 
than once. S was sorted in some custom order previously. We want to permute the 
characters of T so that they match the order that S was sorted. More specifically, 
if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", 
"cbda" are also valid outputs.

Note:
S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
'''

'''
ALGORITHM:
1. Iterate through T, generating a dictionary with the keys being the letter, and 
   the values being the number of occurences of that letter in T. 
   ie abcc -> {a:1, b:1, c:2}
2. Iterate on S. For each letter, if that letter is in our dictionary (which 
   means it was in T), we just append that letter as many times as it appears in 
   T. 
3. At the end, there could be some letters that were in T that weren't in S, so 
   append the rest of these by going through the dictionary again.

RUNTIME COMPLEXITY: O(S + T) where S and T are len(S) and len(T)
SPACE COMPLEXITY: O(T) where T = len(T)
'''

from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = []
        
        t_dict = defaultdict(int)
        for c in T:
            t_dict[c] += 1
        
        s_set = set()
        for c in S:
            s_set.add(c)
            if c in t_dict:
                result.extend([c] * t_dict[c])
        for c in t_dict:
            if c not in S:
                result.extend([c] * t_dict[c])
                
        return ''.join(result)
                
            
            

