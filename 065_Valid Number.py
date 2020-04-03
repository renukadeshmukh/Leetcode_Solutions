'''
65. Valid Number
'''

import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        
        regex = "^([+-]?\d)?\d*((\d+\.)?|(\.\d+(e[+-]?\d+)?)?|(\d+e[+-]?\d+)?)$"
        if re.match(regex, s.strip()):
            return True
        return False

s = Solution()
print(1, s.isNumber("0")==True) #true
print(2, s.isNumber(" 0.1 ")==True) #true
print(3, s.isNumber("abc")==False) #false
print(4, s.isNumber("1 a")==False) #false
print(5,s.isNumber("2e10")==True) #true
print(6,s.isNumber(" -90e3   ")==True) #true
print(7,s.isNumber("1e")==False) #false
print(8,s.isNumber("e3")==False) #false
print(9,s.isNumber(" 6e-1")==True) #true
print(10,s.isNumber(" 99e2.5 ")==False) #false
print(11,s.isNumber("53.5e93")==True) #true
print(12,s.isNumber(" --6 ")==False) #false
print(13,s.isNumber("-+3")==False) #false
print(14,s.isNumber("95a54e53")==False) #false
print(15,s.isNumber(".1")==True) #True
print(16,s.isNumber("-")==False) #false
print(17,s.isNumber("   ")==False) #false
print(18,s.isNumber("e3")==False) #false
print(18,s.isNumber("3.")==True) #true
print(18,s.isNumber("3.e")==False) #falses
print(18,s.isNumber(".")==False) #falses
