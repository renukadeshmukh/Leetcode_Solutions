'''
1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all 
elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are 
the same as in arr2.  Elements that don't appear in arr2 should be placed at the 
end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 
Constraints:
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
'''

'''
ALGORITHM:
1. Calculate count of all elements in arr1
2. Based of order of elements in arr2, populate elements from arr1
3. Sort and add the rest of the elements. 

RUNTIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(N)
'''

from collections import defaultdict
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        mydict = defaultdict(int)
        for a in arr1:
            mydict[a] += 1
        
        result = []
        for a in arr2:
            cnt = mydict[a]
            temp = [a] * mydict[a]
            result.extend(temp)
                
        others = []
        arr2 = set(arr2)
        for key in mydict:
            if key not in arr2:
                temp = [key] * mydict[key]
                others.extend(temp)
        others.sort()
        return result + others
            


