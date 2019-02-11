'''
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify 
repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that 
occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

'''
ALGORITHM:
1. Store all possible 10-character subsequences in lookup set. 
2. If same sequence is encountered again, add it to result. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ln = len(s) - 9
        lookup = set()
        result = set()
        for i in range(ln):
            dna = s[i:i+10]
            if dna in lookup:
                result.add(dna)
            else:
                lookup.add(dna)
        return list(result)

s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))