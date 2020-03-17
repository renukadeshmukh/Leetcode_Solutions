'''
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes. Return the smaller angle (in sexagesimal 
units) formed between the hour and the minute hand.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5

Example 4:
Input: hour = 4, minutes = 50
Output: 155

Example 5:
Input: hour = 12, minutes = 0
Output: 0
 
Constraints:
1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
'''

'''
ALGORITHM:
1. Minute Hand Angle:
   In 60 minutes, minute hand covers 360 degree rotation.
   In 1 minute, minute hand moves 360/60 = 6 degrees
   In x minutes, x * 6 degrees
2. Hour Hand Angle:
   In 12 hours, hour hand covers 360 degree rotation
   In 1 hour, hour hand moves 360/12 = 30 degrees
   In x hours, x * 30 degrees
3. Delta Hour Hand for x Minutes:
   In 60 minutes, hour hand moves (360/12) = 30 degrees
   In x minutes, hour hand will move (x * 30)/60 = x/2 degrees
4. Total hour_hand_angle = hour_hand_angle + delta
5. Angle = minute_angle - hour_angle
6. Return minimum 0f angle and 360 - angle to get smaller angle.

RUNTIME COMPLEXITY : O(1)
SPACE COMPLEXITY : O(1)
'''

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        total = 360
        
        angle_minutes = minutes * 6
        angle_hours = (hour % 12) * 30
        delta = minutes/2.0
        angle_hours += delta
        
        diff = abs(angle_minutes - angle_hours)
        return min(diff, 360-diff)