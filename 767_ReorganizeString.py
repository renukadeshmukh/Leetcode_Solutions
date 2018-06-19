'''
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent 
to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

Algorithm:
1. Scan the string and store it in a dictionary with count of each char
2. Invert the dictionary such that key i the count and value is letters with that count
3. Revert sort the count values 
4. If rev_sorted_keys[0]  > math.ceil(length of string/2), then there is no possible answer.
   Return ''
5. Inilialize result array
5. Fill in the letters(letters with highest occurance first) at alternate positions(index 0,2,4,...).
   Once you reach end of array, start again for odd index(index 1,3,5,...)
'''
import math
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        map = self.generate_charmap(S)
        rev_map = self.invert_charmap(map)
        result = self.reorganize(rev_map, len(S))
        return result

    def reorganize(self, rev_map, lng):
        
        rev_sorted_keys = sorted(rev_map.keys(), reverse=True)

        result = [''] * lng
        i = 0
        if rev_sorted_keys[0]  > math.ceil(lng/2) :
            return ''
        for cnt in rev_sorted_keys:
            chars = rev_map[cnt]
            for c in chars:
                x = cnt
                while x > 0:
                    result[i] = c
                    i += 2
                    if  i >= lng:
                        i = 1     
                    x -= 1
                
                print(result)
        return ''.join(result)

    def generate_charmap(self, S):
        map = {}
        for c in S:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        print(map)
        return map

    def invert_charmap(self, map):
        rev_map = {}
        for c in map:
            cnt = map[c]
            if cnt in rev_map:
                rev_map[cnt].append(c)
            else:
                rev_map[cnt] = [c]
        print(rev_map)
        return rev_map

   
            

        

st = 'aab'

s = Solution()
res = s.reorganizeString(st)
print(res)