'''
880. Decoded String at Index
'''

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        word_len = 0
        i = 0
        res = 'a'
        while i < len(S):
            start, end = i, i
            while i < len(S) and S[i].isalpha():
                i += 1
            end = i
            count = 0
            while i < len(S) and not S[i].isalpha():
                count  = count*10 + int(S[i])
                i += 1
            lng = (end-start) * count
            if K > lng:
                K -= lng
            else:
                res = S[start:end] * count
        return res

s = Solution()
print(s.decodeAtIndex("leet2code3", 10))
print(s.decodeAtIndex("ha22", 5))
print(s.decodeAtIndex("a2345678999999999999999", 1))


