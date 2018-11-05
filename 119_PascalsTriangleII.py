'''
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the 
Pascal's triangle. Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''

'''
RUNTIME COMPLEXITY: (k*k)
SPACE COMPLEXITY: (k*k)
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = 1
        rows = [[0,1,0], [0,1,1,0]]
        if rowIndex <= k:
            return rows[rowIndex][1:-1]
        
        while k < rowIndex:
            tmp = [0]
            row = rows[-1]
            for i in range(len(row)-1):
                tmp.append(row[i] + row[i+1])
            tmp.append(0)
            rows.append(tmp)
            k += 1
        return rows[-1][1:-1]
                
        

