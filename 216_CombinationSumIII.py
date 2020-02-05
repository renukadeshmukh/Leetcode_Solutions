'''
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given 
that only numbers from 1 to 9 can be used and each combination should be a unique 
set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

'''
ALGORITHM:
1. Maintain a temporary set of integers. If length of set == k and sum of 
   integers == n, add this combination to result.
2. Else for num in range (1, 9), add num to set, and temp_sum and recursively 
   call the function with updated set and sum values. 

Note*: To improve runtime, also pass the currently added set element x to 
    recursive call. So that in the next iteration of the for loop, the loop can
    begin at x+1. This way same numbers are not considered again and again. 

RUNTIME COMPLEXITY: O(9^k)
SPACE COMPLEXITY: O(N) for stack space + O(k) for temp set
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(k, n, 0, set(), 0, result)
        return result
        
    def helper(self, k, n, sm, st, num, result):
        if len(st) == k:
            if sm == n :
                result.append(list(st))
            return
        for i in range (num+1, 10):
            st.add(i)
            self.helper(k, n, sm+i, st, i, result)
            st.remove(i)
        
s = Solution()
result = s.combinationSum3(3, 7)
print(result)
result = s.combinationSum3(3, 9)
print(result)