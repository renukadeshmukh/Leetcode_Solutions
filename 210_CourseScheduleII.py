'''
210. Course Schedule II
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        scheduled = set()
        course_map = {}
        for i in range(numCourses):
            course_map[i] = set()
        for c in prerequisites:
            course_map[c[0]].add(c[1])
        flag = False
        while len(order) < len(course_map):
            flag = False
            for key in course_map:
                if key not in scheduled:
                    diff = course_map[key].difference(scheduled)
                    if len(diff) == 0:
                        flag = True
                        order.append(key)
                        scheduled.add(key)
            if flag == False:
                return []
        return order

s = Solution()
order = s.findOrder(2, [[0,1]])
print(order)

order = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(order)
