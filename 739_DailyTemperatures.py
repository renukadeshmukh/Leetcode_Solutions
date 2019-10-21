'''
739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in 
the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each 
temperature will be an integer in the range [30, 100].
'''

'''
ALGORITHM:
1. Maintain a stack of temparatures.
2. If stack is empty push temprature t
3. Else if temprature t > stack[-1], pop all tempratures less than t and record
   the days before warmer temprature t was encountered, in result 
   Append temprature t to stack.
4. Return result

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(T)
        i = -1
        for t in T:
            i += 1
            if stack and T[stack[-1]] < t:
                while stack and T[stack[-1]] < t:
                    x = stack.pop()
                    result[x] = i - x
            stack.append(i)
        return result

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))