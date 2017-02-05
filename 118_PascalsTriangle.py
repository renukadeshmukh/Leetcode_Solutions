'''

118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        
        result = [[1]]
        lRow = []
        numRows -= 1
        for i in range(numRows):
            lRow = self.getNextRow(lRow, i)
            result.append(lRow)
        return result
        
        
    def getNextRow(self, lastRow, l):
        res= [1]
        lng = l+1 
        for i in range(lng-1):
            res.append(lastRow[i] + lastRow[i+1])
        res.append(1)
        return res
        
s = Solution()
print s.generate(5)
