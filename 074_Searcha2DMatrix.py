'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This 
matrix has the following properties:
> Integers in each row are sorted from left to right.
> The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

'''
ALGORITHM:
1. From the problem statement, it can be seen that if all rows of the matrix
   were appended and converted into one 1D array, the resulting array would be 
   sorted. Also, searching in a sorted attay is logN. 
2. Applying the same logic here, i = 0 (start of 1D array) and j = MN-1(end of
   1D array).
3. Perform binary search between i and j. mid = (i + j)/2
4. Convert mid into row and col using the following formula:
    row = mid//N 
    col = mid % N, where N = total number of cols
5. Similar to binary search, 
   if martix[row][col] == target, return True
   if martix[row][col] > target, j = mid-1
   if martix[row][col] < target, i = mid+1
6. Keep repeating steps 3, 4, 5 till target is found of i <= j
7. If target found, return True, else return False. 


RUNTIME COMPLEXITY: O(Log(MN))
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        i, j = 0, M*N-1

        while i <= j:
            mid = i + (j-i)//2
            r = mid//N 
            c = mid % N

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                j = mid-1
            else:
                i = mid+1
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))
