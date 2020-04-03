'''
1004. Max Consecutive Ones III
'''
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, j = 0,0
        cnt0 = 0
        queue0 = []
        q_i = 0
        mx_ln, cur_ln = -1, 0
        for i in range(len(A)):
            if A[i] == 0:
                cnt0 += 1
                queue0.append(i)
            if len(queue0) == K:
                mx_ln = max(mx_ln, i-j+1)
                cnt0 -= A[j] ^ 0 ^ 1
                j += 1
                
        print( mx_ln)
        
s = Solution()
s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)