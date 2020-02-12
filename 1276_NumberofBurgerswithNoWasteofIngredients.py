'''
1276. Number of Burgers with No Waste of Ingredients

Given two integers tomatoSlices and cheeseSlices. The ingredients of different 
burgers are as follows:
Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices 
equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not 
possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

Example 1:
Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 
tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.

Example 2:
Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make burgers.
Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 
small burgers there will be 15 cheese remaining.

Example 4:
Input: tomatoSlices = 0, cheeseSlices = 0
Output: [0,0]

Example 5:
Input: tomatoSlices = 2, cheeseSlices = 1
Output: [0,1]
 
Constraints:
0 <= tomatoSlices <= 10^7
0 <= cheeseSlices <= 10^7
'''

'''
1. The program can be solved mathematically, by treating it as 2 equations with 
   2 unknowns x and y. 
   x + y =  cheeseSlices
   4x + 2y = tomatoSlices
2. Solve for x and y and if a valid solution is found return the answer else 
   return [].
RUNTIME COMPLAXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        #x + y =  cheeseSlices
        #4x + 2y = tomatoSlices
        
        result = (tomatoSlices - 2 * cheeseSlices) / 2
        total_jumbo, total_small = result, cheeseSlices - result
        if total_jumbo < 0 or total_small < 0:
            return []
        if 4*total_jumbo + 2*total_small == tomatoSlices:
            return [total_jumbo, total_small]
        return []
        
