'''
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of 
the squares of each number, also in sorted non-decreasing order.
 
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

'''
ALGORITHM:
1. Keep two pointers, i=0 and j= len-1
2. res = [], k = len-1
3. if A[i]*A[i] > A[j]*A[j], copy the A[i]*A[i] at res[k] and inc i
4. Else copy  A[j]*A[j] at res[k] and dec j
5. dec k
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        res = [0] * len(A)
        k = j
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res[k] = A[i]*A[i]
                i += 1
            else:
                res[k] = A[j]*A[j]
                j -= 1
            k -= 1
            
        return res

