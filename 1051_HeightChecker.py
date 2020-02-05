'''
1051. Height Checker

Students are asked to stand in non-decreasing order of heights for an annual 
photo. Return the minimum number of students not standing in the right 
positions.  (This is the number of students that must move in order for all 
students to be standing in non-decreasing order of height.)

 
Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
 
Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100
'''

'''
ALGORITHM: 
1. Create a deep copy of heights = h_copy.
2. sort heights.
3. Iterate over h_copy and heights. For every h_copy[i] != heights[i], inc 
   result.
4. Return result. 

RUNTIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(N)
'''
import copy
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h_copy = copy.copy(heights)
        heights.sort()
        
        result = 0
        for i in range(len(heights)):
            if h_copy[i] != heights[i]:
                result += 1
        return result

s = Solution()
result = s.heightChecker([1,1,4,2,1,3])
print(result)