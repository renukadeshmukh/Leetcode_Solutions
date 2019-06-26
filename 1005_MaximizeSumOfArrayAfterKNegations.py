'''
1005. Maximize Sum Of Array After K Negations

Given an array A of integers, we must modify the array in the following way: we 
choose an i and replace A[i] with -A[i], and we repeat this process K times in 
total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way. 

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:
1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
'''

'''
ALGORITHM:
1. Sort the array
2. Convert negative numbers to positive while K > 0
3. If all numbers are positive, but K is still greater than 0:
   > If 0 present in array, no need to negate any more numbers
   > If 0 not present in array, sort all elements in the array again and negate
     the smallest element K times.
4. Return sum of array.

RUNTIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(NLOGN)
'''

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        if A[0] < 0:
            while i < len(A) and A[i] < 0 and K:
                A[i] = A[i]*-1
                K -= 1
                i += 1
        if K and i < len(A) and A[i] == 0:
            K = 0
            i += 1
        if K%2 == 1:
            A.sort()
            A[0] = A[0]*-1
        
        return sum(A)
            
        
        
