'''
916. Word Subsets
'''

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        b_lookup = {}
        a_lookup = {}
        a_set = set(A)
        res_lookup = [0] * len(A)
        res = []
        for a in A:
            a_lookup[a] = self.get_word_dict(a)
        for b in B:
            b_map = self.get_word_dict(b)
            a_set = self.intersection(a_set, a_lookup, b_map)
        return list(a_set)
            

    def intersection(self, a_set, a_lookup, b_map):
        flag = True
        to_remove = set()
        for a in a_set:
            a_map = a_lookup[a]
            for ch in b_map:
                if ch not in a_map or b_map[ch] > a_map[ch]:
                    to_remove.add(a)
                    break
        a_set.difference_update(to_remove)
        return a_set
                  
    def get_word_dict(self, word):
        lookup = {}
        
        for c in word:
            if c not in lookup:
                lookup[c] = 0
            lookup[c] += 1
        return lookup
                        

s = Solution()
word_set = ["amazon","apple","facebook","google","leetcode"]
print(s.wordSubsets(word_set, ["e","o"]))
print(s.wordSubsets(word_set, ["l","e"]))
print(s.wordSubsets(word_set, ["e","oo"]))
print(s.wordSubsets(word_set, ["lo","eo"]))
print(s.wordSubsets(word_set, ["ec","oc","ceo"]))