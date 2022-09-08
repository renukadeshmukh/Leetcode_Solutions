'''
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank 
every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to 
Sunday, he will put in $1 more than the day before. On every subsequent Monday, 
he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at 
the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
(2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
(2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
1 <= n <= 1000
'''

'''
ALGORITHM:
total_weeks n = days // 7
total_days d = days % 7

Week1 : (1 + 2 + 3 + 4 + 5 + 6 + 7)
Week2 : Week1 + 7
Week3 : Week1 + 14
Week4 : Week1 + 21
.
.
Weekn = n * Week1 + (7 + 14 + 21 ....)
Weekn = n * Week1 + 7 * (1 + 2 + 3...)
Weekn = n * Week1 + 7 * (n * n-1)/2

Day1 = n
Day2 = n + 1
.
.
Dayd = n + d
Dayd = n + n + 1 + n + 2 ....
Dayd = d * n + (1 + 2 +...d)
Dayd = d * n + (d * d+1)/2

Result = Weekn + Dayd

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        one_week = 28 # 7*8/2 
        weeks = n//7
        days = n%7
        
        week_money = weeks*one_week + ((weeks * (weeks-1)) / 2) * 7
        day_money = days * weeks  + ((days * (days+1)) / 2) 

        return week_money + day_money 
        
        
      