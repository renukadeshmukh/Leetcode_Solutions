'''
1329. Sort the Matrix Diagonally

Given a m * n matrix mat of integers, sort it diagonally in ascending order from 
the top-left to the bottom-right then return the sorted array.

Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''

'''
ALGORITHM:
1. Traverse the matrix diagonal-wise and store elements in an array. 
2. Sort the array.
3. Put the elements back in the diagonal in sorted order. 

RUNTIME COMPLEXITY: O(M*N*XlogX) M*N for traversal and XlogX for sorting
SPACE COMPLEXITY: O(X), where X = max(M,N)
'''

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(mat), len(mat[0])
        
        for k in range(M-1, 0, -1):
            self.helper(k, 0, mat, M, N)
                
        for k in range(N):
            self.helper(0, k, mat, M, N)
        return  mat
    
    def helper(self, i, j, mat, M, N):
        arr = []
        i1, j1 = i, j
        while i1 < M and j1 < N:
            arr.append(mat[i1][j1])
            i1, j1 = i1+1, j1+1
        arr.sort()
        i1, j1, c = i, j, 0
        while i1 < M and j1 < N:
            mat[i1][j1] = arr[c]
            i1, j1, c = i1+1, j1+1, c+1
            
            
s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))