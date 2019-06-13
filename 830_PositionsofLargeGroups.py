'''
830. Positions of Large Groups

In a string S of lowercase letters, these letters form consecutive groups of the 
same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", 
"z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting 
and ending positions of every large group.

The final answer should be in lexicographic order.

Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending 
positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
'''

'''
ALGORITHM:
1. Maintain pointers i, j with i <= j. The i pointer will represent the start of 
the current group, and we will increment j forward until it reaches the end of 
the group.
2. We know that we have reached the end of the group when j is at the end of the 
string, or S[j] != S[j+1]. At this point, we have some group [i, j]; and after, 
we will update i = j+1, the start of the next group.

RUNTIME COMPLEXITY: (N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans