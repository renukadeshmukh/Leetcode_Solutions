'''
547. Friend Circles
'''


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        priority_queue = dict()
        result = 0
        for i in range(len(M)):
            for j in range(i):
                if i not in priority_queue:
                    priority_queue[i] = set()
                if j not in priority_queue:
                    priority_queue[j] = set()
                if M[i][j] and i!=j:
                    priority_queue[i].add(j)
                    priority_queue[j].add(i)
        
        for friend in priority_queue:
            friends = priority_queue[friend]
            if friend not in visited:
                visited.add(friend)
                result += 1
            visited.update(friends)
        return result

s = Solution()
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))