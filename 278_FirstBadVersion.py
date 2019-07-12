'''
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since 
each version is developed based on the previous version, all the versions after 
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version 
is bad. Implement a function to find the first bad version. You should minimize 
the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

'''


'''
ALGORITHM:
1. Binary Search
TIME COMPLEXITY: O(LOGN)
SPACE COMPLEXITY: O(1)
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1,n
        if isBadVersion(1) == True:
            return 1
        elif isBadVersion(n) == False:
            return -1
        last_bad = -1
        while low <= high:
            mid = low + (high - low)//2
            isbad = isBadVersion(mid)
            if isbad:
                last_bad = mid
                high = mid - 1
            else:
                low = mid + 1
        return last_bad
                
  
s = Solution()
print(s.firstBadVersion(3))