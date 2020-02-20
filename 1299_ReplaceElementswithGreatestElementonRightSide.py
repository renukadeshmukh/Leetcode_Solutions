'''
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 
Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''

'''
ALGORITHM:
1. Iterate over the array in reverse and keep track of maximum encountered from 
   right. 
2. Keep updating the array in reverse with the maximum value.
3. Return the final array. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], maximum = maximum,  max(arr[i], maximum)
        return arr
