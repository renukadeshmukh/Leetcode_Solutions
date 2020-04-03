'''
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters 
A to Z where different letters represent different tasks.Tasks could be done 
without original order. Each task could be done in one interval. For each interval, 
CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same 
tasks, there must be at least n intervals that CPU are doing different tasks or 
just be idle.

You need to return the least number of intervals the CPU will take to finish all 
the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        jmap = self.map_jobs(tasks)
        inv_map = self.invert_map(jmap)
        print(jmap)
        print(inv_map)
        res = self.schedule(inv_map, n, len(jmap))
        
        return len(res)
        
    def schedule(self, inv_map, n, unique_jobs):
        keys = inv_map.keys()
        keys = sorted(keys, reverse = True)
        max_cnt = keys[0]
        size = max(max_cnt * unique_jobs, max_cnt * (n + 1))
        res, i, j = [''] * size, -1,-1

        for key in keys:
            jobs = inv_map[key]
            for job in jobs:
                print(res)
                cnt = key
                j += 1
                i = j
                while cnt > 0:
                    res[i] = job
                    i += (n+1)
                    cnt -=1
        res = self.cleanup(res)
        return res        
        
    def cleanup(self, res):
        i = len(res) - 1
        while res[i]  == '':
            i -= 1
        return res[:i+1]         


    def map_jobs(self, tasks):
        jmap = {}
        for task in tasks:
            if task in jmap:
                jmap[task] += 1
            else:
                jmap[task] = 1
        return jmap
    
    def invert_map(self, jmap):
        inv_map = {}
        for job in jmap:
            cnt = jmap[job]
            if cnt in inv_map:
                inv_map[cnt].append(job)
            else:
                inv_map[cnt] = [job]
        return inv_map

s = Solution()
tasks = ["A","A","A","B","B","B",]
n = 0
res = s.leastInterval(tasks, n)
print(res)   