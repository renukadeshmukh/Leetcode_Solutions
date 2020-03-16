'''
1380. Lucky Numbers in a Matrix

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix 
in any order. A lucky number is an element of the matrix such that it is the 
minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and 
the maximum in its column

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and 
the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
'''

'''
ALGORITHM:
1. Keep 2 arrays of size M and N, to keep track of mininums in each row and maxs 
   in each column respectively. 
2. Return the intersection of these 2 arrays. 
 
RUNTIME COMPLEXITY: O(M*N)
SPACE COMPLEXITY: O(M+N)
'''

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(matrix), len(matrix[0])
        row_mins = [100001] * m
        col_maxs = [-1] * n
        
        for i in range(m):
            for j in range(n):
                row_mins[i] = min(row_mins[i], matrix[i][j])
                col_maxs[j] = max(col_maxs[j], matrix[i][j])
        
        return set(row_mins).intersection(set(col_maxs))
                