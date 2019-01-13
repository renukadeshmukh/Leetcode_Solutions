'''
539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the 
minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''

'''
ALGORITHM:
1. Convert each timestamp to minutes (hours*60+minutes)
    =>if any minute_value apprears twice, return 0
2. sort the minutes array
3. find the minimum difference between adjacent minute values
4. find the difference between 0th and nth index (because clock is circular)
5. return the minimum difference

RUNTIME COMPLEXITY: O(NLogN) 
SPACE COMPLEXITY: O(N) where n is the size of input
'''
        
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_points = []
        time_points_st = set()
        for point in timePoints:
            mins = self.get_minutes(point)
            if mins in time_points_st:
                return 0
            time_points.append(mins)
            time_points_st.add(mins)
        time_points.sort()
        min_diff = 1440
        for i in range(len(time_points)-1):
            min_diff = min(min_diff, (time_points[i+1]-time_points[i]))    
        min_diff = min(min_diff, 1440 + time_points[0] - time_points[-1] )
            
        return min_diff
        
    
    def get_minutes(self, time):
        time_arr = time.split(":")
        mins = int(time_arr[0])*60 + int(time_arr[1])
        return mins
        

