'''
933. Number of Recent Calls

Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.
Return the number of pings that have been made from 3000 milliseconds ago until now.
Any ping with time in [t - 3000, t] will count, including the current ping.
It is guaranteed that every call to ping uses a strictly larger value of t than before.


Example 1:
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],
[100],[3001],[3002]]
Output: [null,1,2,3,3]
 

Note:
Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
'''

'''
ALGORITHM:
1. Keep a queue to keep track of pings in order.
2. For every ping, remove all ping that are older than 3000 secs
3. return length of queue

RUNTIME COMPLEXITY: O(N)
SPACE COMPLECITY: O(N)
'''

from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.q = deque()
        
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while t - self.q[0]  > 3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
s = RecentCounter()
print(s.ping(1))
print(s.ping(100))
print(s.ping(3001))
print(s.ping(3002))
