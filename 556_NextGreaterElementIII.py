'''
556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer 
which has exactly the same digits existing in the integer n and is greater in 
value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
 
Example 2:
Input: 21
Output: -1
'''

'''
ALGORITHM:
1. Scan the number from right to left till first increasing pair of digits.(x,y)
   Meaning, find the first dip from right.
2. If there is no such pair, that means this number is already the biggest.
   Return -1
3. Find the smallest digit from right part such that digit > x
4. Swap digit with x. 
5. Sort the remaining digits in ascending ordering and append back to the original
   number. 

RUNTIME COMPLEXITY: O(NlogN)
SPACE COMPLEXITY: O(N)
'''

from math import pow
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        y = n%10
        n = n//10
        store = []
        while n > 0:
            store.append(y)
            x = n%10
            if x < y:
                break
            y = x
            n = n//10
        if n == 0:
            return -1

        min_greater_than_dip = self.get_min_greater_than_dip(x, y, store)
        store.append(x)
        store.remove(min_greater_than_dip)
        store.sort()
        n1 = 0
        for i in store:
            n1 = n1 * 10 + i
        n = (n - x + min_greater_than_dip) * pow(10,len(store)) + n1 
        
        if n < 2147483647:
            return int(n)
        return -1

    def get_min_greater_than_dip(self, x, y, store):
        for elem in store:
            if elem < y and elem > x:
                y = elem
        return y

s = Solution()
print(s.nextGreaterElement(12443322))
print(s.nextGreaterElement(9876))
print(s.nextGreaterElement(12344321))
print(s.nextGreaterElement(2147483647))
print(s.nextGreaterElement(12))
        