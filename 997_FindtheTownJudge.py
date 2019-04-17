'''
997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one 
of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the 
person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town 
judge.  Otherwise, return -1. 

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 
Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''

'''
ALGORITHM:
1. Maintain 2 lists degree and flag
2. for each pair <trustee, trusted>,
   mark flag[trustee] = -1 as he cannot be the judge
   inc count of degree[trusted]
3. If for some i, flag[i] != -1 and degree[i] == N-1, return i as judge
4. else return -1

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degree = [0] * (1+N)
        flag = [0] * (1+N)
        for a,b in trust:
            flag[a] = -1
            degree[b] += 1
        
        for i in range(1, N+1):
            if degree[i] == N-1 and flag[i] != -1:
                return i
        return -1
            