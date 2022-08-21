'''
1253. Reconstruct a 2-Row Binary Matrix

Given the following details of a matrix with n columns and 2 rows :

> The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
> The sum of elements of the 0-th(upper) row is given as upper.
> The sum of elements of the 1-st(lower) row is given as lower.
> The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is 
  given as an integer array with length n.

Your task is to reconstruct the matrix with upper, lower and colsum.
Return it as a 2-D integer array.
If there are more than one valid solution, any of them will be accepted.
If no valid solution exists, return an empty 2-D array.

Example 1:
Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

Example 2:
Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []

Example 3:
Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 
Constraints:
1 <= colsum.length <= 10^5
0 <= upper, lower <= colsum.length
0 <= colsum[i] <= 2
'''

'''
ALGORITHM:
1. Since it is a binary array, possible values of colsum can be 0, 1, 2
2. If sum == 2, that means both the cells in that column are 1.
3. Create 2 arrays for row1 and row2 initialized with zeroes. 
4. First populate values in row1 and row2 where colsum is 2. Update upper and
   lower sum. 
5. Now populate values in row1 and row2 where colsum is 1. If upper > 0, assign 
   1 to row1, else if lower > 0, assign 1 to row2. Update upper and lower sum. 
6. If at the end  lower and upper are not zero, return empty result. 
7. Else return [row1, row2]

TIME COMPLEXITY : O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        invalid = False
        row1 = [0] * n
        row2 = [0] * n
    
        
        cells_with_colsum_one = []
        for i in range(n):
            if colsum[i] == 1:
                cells_with_colsum_one.append(i)
            elif colsum[i] == 2:
                row1[i] = 1
                row2[i] = 1
                upper -= 1
                lower -= 1
            
        for i in cells_with_colsum_one:
            if upper > 0:
                row1[i] = 1
                upper -= 1
            elif lower > 0:
                row2[i] = 1
                lower -= 1
            else:
                invalid = True
                break
            
        if invalid or lower != 0 or upper != 0:
            return []
        
        return [row1, row2]
    
 

s = Solution()
arr = s.reconstructMatrix(2, 3, [2, 2, 1, 1])
print(arr)