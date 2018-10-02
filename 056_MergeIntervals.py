'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.start, reverse=False)
        first = intervals[0].start
        last = intervals[0].end
        i = 1
        while(i < len(intervals)):
            cur = intervals[i]
            
            #case 1: current interval lies within first and last. Hence we can ignore this interval 
            if cur.start >= first and cur.end <= last:
                i += 1
                continue
            #case 2: current interval has no overlap with first and last, Hence save first and last and start new interval
            elif cur.start > last:
                result.append([first,last])
                first = cur.start
                last = cur.end
            #case 3: there is an overlap between the interval
            else:
                last = cur.end
            i += 1
        result.append([first,last])        
        return result
            
        
        
input = [[1,5],[0,6],[2,13]]
intervals = []
for pair in input:
    interval = Interval(pair[0], pair[1])
    intervals.append(interval)

s = Solution()
print s.merge(intervals)
    