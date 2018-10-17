'''
922. Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even. Sort the array so that whenever A[i] is odd, 
i is odd; and whenever A[i] is even, i is even. You may return any answer array 
that satisfies this condition.

Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

'''
ALGORITHM:
1. Iterate on the array and find all indices with incorrect elements.
2. Swap the elements at incorrect indices.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_indices, even_indices, i = [], [], 0
        for a in A:
            if i%2 == 0 and A[i] % 2 == 1:
                even_indices.append(i)
            elif i%2 == 1 and A[i] % 2 == 0:
                odd_indices.append(i)
            i += 1
        for x,y in zip(odd_indices, even_indices):
            A[x], A[y] = A[y], A[x]
        return A
        
        