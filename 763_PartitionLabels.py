'''
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into 
as many parts as possible so that each letter appears in at most one part, and 
return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

'''
ALGORITHM:
1. Iterate on the string, for each character save the fitst and last index in
   a dictionary as :- dic[c] = [first_index, last_index]
2. Then convert this dictionary into array
   arr = dic.values()
3. Sort this array w.r.t srart_index
4. Merge overlapping intervals
5. Return length of each final interval as an array.

TIME COMPLEXITY: O(NlogN)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(S)):
            if S[i] not in dic:
                dic[S[i]] = [i,i]
            else:
                dic[S[i]][1] = i
        
        intervals = sorted(dic.values(), key=lambda x: x[0])
        merged = self.mergeIntervals(intervals)
        res = []
        for elem in merged:
            res.append(elem[1] - elem[0] + 1)
        return res
        
    def mergeIntervals(self, arr):
        res = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i][0] > res[-1][1]:
                res.append(arr[i])
            elif arr[i][1] > res[-1][1] and arr[i][0] < res[-1][1]:
                res[-1][1] = arr[i][1]
        return res
            
            
            
        
        
            