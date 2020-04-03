'''
1324. Print Words Vertically

Given a string s. Return all the words vertically in the same order in which 
they appear in s. Words are returned as a list of strings, complete with spaces 
when is necessary. (Trailing spaces are not allowed). Each word would be put on 
only one column and that in one column there will be only one word.

Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"

Example 3:
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 
Constraints:
1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.
'''

'''
ALGORITHM:

RUNTIME COMPLEXITY:
SPACE COMPLEXITY: 
'''

class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        longest = max([len(w) for w in words])
        
        result = []
        for j in range(longest):
            temp = [' '] * len(words)
            for i in range(len(words)):
                if len(words[i]) > j:
                    temp[i] = words[i][j]
            result.append(''.join(temp).rstrip())
        return result
                
s = Solution()
print(s.printVertically("CONTEST IS COMING"))