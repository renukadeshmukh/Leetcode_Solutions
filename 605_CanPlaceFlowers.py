'''
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some 
are not. However, flowers cannot be planted in adjacent plots - they would compete 
for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty 
and 1 means not empty), and a number n, return if n new flowers can be planted in 
it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''

'''
ALGORITHM:
1. Append 0 and beginning and end of array
2. if not (flowerbed[i-1] or flowerbed[i+1] or flowerbed[i]), then 
    n -= 1 and flowerbed[i] = 1
3. Repeat for all elements in the array

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed)-1):
            if not (flowerbed[i-1] or flowerbed[i+1] or flowerbed[i]):  
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
            
        
                
s = Solution()
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))