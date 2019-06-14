'''
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise 
return 0.
You may assume that the version strings are non-empty and contain only digits 
and the . character. The . character does not represent a decimal point and is 
used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is 
the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to 
be 0. For example, version number 3.4 has a revision number of 3 and 4 for its 
first and second level revision number. Its third and fourth level revision 
number are both 0.
'''

'''
ALGORITHM:
1. Split the given version1 and version2 at '.'
2. Compare corresponding portions of the versions to find the higher version

RUNTIME COMPLEXITY: O(N) 
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(4):
            a, b = 0, 0
            if i < len(v1):
                a = int(v1[i])
            if i < len(v2):
                b = int(v2[i])
            
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
            
s = Solution()
print(s.compareVersion("0.1", "1.1"))
print(s.compareVersion("1.0.1", "1"))
print(s.compareVersion("7.5.2.4", "7.5.3"))
print(s.compareVersion("1.01", "1.001"))
print(s.compareVersion("1.0", "1.0.0"))


