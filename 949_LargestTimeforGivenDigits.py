'''
949. Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 
00:00, a time is larger if more time has elapsed since midnight. Return the 
answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""
 
Note:
A.length == 4
0 <= A[i] <= 9
'''

'''
ALGORITHM:
1. From 23:59 to 00:00 go over every minute of 24 hours. 
2. If all 4 digits are in A, return the answer else return ""
  
RUNTIME COMPLEXITY: O(24 * 60)
SPACE COMPLEXITY: O(Len(A))
'''

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h//10, h % 10, m//10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return "{}{}:{}{}".format(t[0], t[1], t[2], t[3])
        return ''