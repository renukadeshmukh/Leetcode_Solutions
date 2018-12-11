'''
453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves 
required to make all array elements equal, where a move is incrementing n - 1 
elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

'''
ALGORITHM:
let's define sum as the sum of all the numbers, before any moves; 
minNum as the min number int the list; 
n is the length of the list;

After, say m moves, we get all the numbers as x , and we will get the following 
equation:
 sum + m * (n - 1) = x * n
and actually,
  x = minNum + m
It comes from two observations:
1. the minum number will always be minum until it reachs the final number, because 
   every move, other numbers (besides the max) will be increamented too;
2. from above, we can get, the minum number will be incremented in every move. So, 
   if the final number is x, it would be minNum + moves;

Finally, we will get
  sum - minNum * n = m


TIME COMPLEXITY: (N) for sum and min operations
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sum(nums) - min(nums) * len(nums)
        return res