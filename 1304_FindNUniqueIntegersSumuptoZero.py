'''
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they 
add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]

Constraints:
1 <= n <= 1000
'''

'''
ALGORITHM:
1. For i in range 1 through n/2 + 1, generate pairs (i, -i) and append to 
   result. 
2. If n is odd, append 0 to result. 
3. Return result. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for result 
'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        half = n/2
        answer = []
        for i in range(1, half+1):
            answer.extend([i, -i])
        if n % 2 == 1:
            answer.append(0)
        return answer