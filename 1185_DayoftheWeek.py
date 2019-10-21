'''
1185. Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year 
respectively.

Return the answer as one of the following values 
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 
Constraints:
The given dates are valid dates between the years 1971 and 2100.
'''

'''
ALGORITHM:
1. Keep track of total days since 1/1/1971. total_days = 0
1. For each year since 1971 (except the current year), add the number of days in 
   that year. 356 for normal years and 366 for leap years.
   total_days += 365 for normal years
   total+days += 366 for leap years
   We do not consider the current years because it will have less than 365 days.
2. For every month in current year, except the current month, add number of days 
   in that month. 
   total_days += num of days in each month
3. Add number of days in current month. 
   total_days += day
4. To convert total_days to week day, take % 7.
   day_of_week = total_days % 7
5. Rotate the week array by 4 places because, 1/1/1971 was a Thursday. 
   days = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
6. Return days[day_of_week]

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        
        days = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', ]
        total_days = 0
        month -= 1
        while month > 0:
            total_days += self.days_of_month(month, year)
            month -= 1
        year -= 1
        while year >= 1971:
            total_days += 365 + self.is_leap_year(year)
            year -= 1
        total_days += day 
        
        day_of_week =  total_days % 7
        return days[day_of_week]
        
    
    def is_leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 1
        return 0
    
    def days_of_month(self, month, year):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month != 2:
            return days[month-1]
        return days[month-1] + self.is_leap_year(year)
        
    
s = Solution()
print(s.dayOfTheWeek(21, 12, 1980))
print(s.dayOfTheWeek(31, 1, 1971)) #Sunday  
print(s.dayOfTheWeek(31, 8 , 2019)) #Saturday 
print(s.dayOfTheWeek(18, 7, 1999)) #Sunday
print(s.dayOfTheWeek(15, 8, 1993)) #Sunday