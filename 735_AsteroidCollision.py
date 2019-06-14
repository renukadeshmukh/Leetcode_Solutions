'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign 
represents its direction (positive meaning right, negative meaning left). Each 
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. Two 
asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.

Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving in same direction never meet.

Note:
The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
'''

'''
ALGORITHM:
1. For each asteroid, if result is empty, add the asteroid to result. 
2. If asteroid is moving in positive direction append to result. 
3. If asteroid is negative and last encountered asteroid was also negative, 
append asteroid to result. 
4. If asterodi is negative, and last encountered asteroid was positive, there is
going to be a collision. Pop all the positive asteroid smaller in size. If 
larger positive is found, destroy the negative asteroid. Else append the 
negative asteroid to result. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
        
s = Solution()
print(s.asteroidCollision([2,-6,-2,-1]))