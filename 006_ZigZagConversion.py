'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 1:
                return s
        row, flag = (0,1)
        res = [''] * numRows
        for c in s:
            if flag == 1:
                res[row] += c
                row += 1
                if row == numRows -1:
                    flag = -1
            else:
                res[row] += c
                row -=1
                if row == 0:
                    flag = 1 
        return ''.join(res)             

s = Solution()
st = "PAYPALISHIRING"
numRows = 2
s.convert(st, numRows)