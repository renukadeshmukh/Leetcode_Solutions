'''
945. Minimum Increment to Make Array Unique

Given an array of integers A, a move consists of choosing any A[i], and 
incrementing it by 1.
Return the least number of moves to make every value in A unique.
 
Example 1:
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to 
have all unique values.

Note:
0 <= A.length <= 40000
0 <= A[i] < 40000
'''

'''
ALGORITHM:
1. Sort the array.
2. For each element from index one till last, if A[i-1] is equal or greater than
   A[i], increment A[i] to be 1 more than A[i-1]


RUNTIME COMPLEXITY: O(NLOGN) for sort
SPACE COMPLEXITY: O(N) for sort.
'''
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        result = 0
        for i in range(1, len(A)):
            if A[i-1] >= A[i]:
                diff = A[i-1] - A[i]
                A[i] += (diff + 1)
                result += (diff + 1)
                print(A)
        return result 
        

s = Solution()
print(s.minIncrementForUnique([1,2,2]))
print(s.minIncrementForUnique([3,2,1,2,1,7]))