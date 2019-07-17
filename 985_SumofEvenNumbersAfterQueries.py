'''
985. Sum of Even Numbers After Queries

We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as 
the answer to the i-th query.

Example 1:
Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length
'''

'''
ALGORITHM:
1. Maintain SUM_EVEN, the sum of even elements throughout one query operation.
2. When acting on an array element A[index], the rest of the values of A remain 
   the same. 
3. Remove A[index] from S if it is even, then add A[index] + val back (if it is even.)

RUNTIME COMPLEXITY: O(N+Q), where N=length of A and Q=number of queries
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sm_even = 0
        for a in A:
            if a % 2 == 0:
                sm_even += a
        result = []
        for query in queries:
            val,index = query[0], query[1]
            if A[index] % 2 == 0:
                sm_even -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sm_even += A[index]
            result.append(sm_even)
        return result

s = Solution()
print(s.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]] ))