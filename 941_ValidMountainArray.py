'''
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain 
array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
 
Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note
0 <= A.length <= 10000
0 <= A[i] <= 10000 
'''

'''
ALGORITHM:
1. Initialize i=0 and j=len(A)-1
1. while A[i] < A[i+1], increment i
2. while A[j] < A[j-1], decrement j
3. if i ==j, return True else return False

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        
        i, j = 0, len(A) - 1
        
        while i < j and A[i] < A[i+1]:
            i += 1
            
        while j > 1 and A[j] < A[j-1]:
            j -= 1

        if i == 0:
            return False
        elif j == len(A)-1:
            return False
        if i == j:
            return True
        return False

