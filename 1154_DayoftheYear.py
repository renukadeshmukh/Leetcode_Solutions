'''
1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as 
YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Example 3:
Input: date = "2003-03-01"
Output: 60

Example 4:
Input: date = "2004-03-01"
Output: 61
 
Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''

'''
ALGORITHM:
1. total_days = 0
2. For every month less than given month, add the number of days in that month. 
   Take care of adding 1 extra day for Feburary in leap year. 
   total_days += month_days[i]
3. Add number of days in current month. 
   total_days += days_in_current_month
4. Return total_days

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date = date.split("-")
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        yy, mm, dd = int(date[0]), int(date[1]), int(date[2])
        is_lear_year = (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0)
        
        month = 1
        total_days = 0
        while month < mm:
            total_days += month_days[month-1]
            if month == 2 and is_lear_year:
                total_days += 1
            month += 1
        total_days += dd
        return total_days 
