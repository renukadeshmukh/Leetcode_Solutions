'''
744. Find Smallest Letter Greater Than Target

Given a list of sorted characters letters containing only lowercase letters, and 
given a target letter target, find the smallest element in the list that is 
larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and 
letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
'''

'''
ALGORITHM:
1. Binary Search 

RUNTIME COMPLEXITY: O(NLOGN)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        start, end = 0, len(letters)-1
        
        while start <= end:
            mid = start + (end-start)//2
            if letters[mid-1] <= target and letters[mid] > target:
                return letters[mid]
            elif  letters[mid] <= target and letters[mid+1] > target:
                return letters[mid+1]            
            elif letters[mid] <= target:
                start = mid
            else:
                end = mid
        