'''
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 
6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or 
one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are 
currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", 
"0:32"]

Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it 
should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for 
example "10:2" is not valid, it should be "10:02".
'''

'''
ALGORITHM:
1. Compute all times from 00:00 to 11:59 and check if number of set bits = num

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    result.append('%d:%02d' % (h, m))
        return result