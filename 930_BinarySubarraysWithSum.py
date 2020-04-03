'''
930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
'''


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        sm = 0
        i, j = 0, 0
        count = 0
        while j < len(A):
            sm += A[j]
            if sm > S:
                while sm > S:
                    sm -= A[i]
                    i += 1
                    #j -= 1
            if sm == S:
                count += 1
                print((i,j))
            j += 1

        
        return count
            
s = Solution()
#print(s.numSubarraysWithSum([0,0,0,0,0], 0))
print(s.numSubarraysWithSum([1,0,1,0,1], 2))

