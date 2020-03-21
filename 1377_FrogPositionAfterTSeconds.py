'''
1377. Frog Position After T Seconds

Given an undirected tree consisting of n vertices numbered from 1 to n. A frog 
starts jumping from the vertex 1. In one second, the frog jumps from its current 
vertex to another unvisited vertex if they are directly connected. The frog can 
not jump back to a visited vertex. In case the frog can jump to several vertices 
it jumps randomly to one of them with the same probability, otherwise, when the 
frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the tree are given in the array edges, where edges[i] = [fromi, toi] 
means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.

Example 1:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
jumping with 1/3 probability to the vertex 2 after second 1 and then jumping 
with 1/2 probability to vertex 4 after second 2. Thus the probability for the 
frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 

Example 2:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 

Example 3:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666

Constraints:
1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
Answers within 10^-5 of the actual value will be accepted as correct.
'''

'''
ALGORITHM:
1. Perform BFS traversal on the tree and keep calculating probability for every
   node till you reach target node. 
2. Keep decrementing time(t) for every next level. 
3. If you run out of time before node is reached, return 0
4. If you reach target node in valid time, calculate probability and return.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict, deque
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        priority_queue = defaultdict(list)
        for e in edges:
            e1, e2 = e[0], e[1]
            priority_queue[min(e1, e2)].append(max(e1, e2))
        #print( priority_queue)

        q = deque([(1,1), '#'])
        answer = 0
        while t >= 0 and len(q) > 1:
            elem = q.popleft()
            if elem == '#':
                q.append('#')
                t -= 1
            else:
                node, probability = elem[0], elem[1]
                if node == target and (node not in priority_queue or t == 0):
                    answer = probability
                    break
                elif elem[0] in priority_queue:
                    num_children = len(priority_queue[node])
                    probability = probability/num_children
                    for child in priority_queue[node]:
                        q.append((child, probability))

        return answer
                
s = Solution()
print(s.frogPosition(3, [[2,1],[3,2]], 1, 2))
print(s.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4))
print(s.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7))
print(s.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6))
