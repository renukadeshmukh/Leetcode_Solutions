'''
1209. Remove All Adjacent Duplicates in String II

Given a string s, a k duplicate removal consists of choosing k adjacent and equal 
letters from s and removing them causing the left and the right side of the 
deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.
 
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
'''

'''
ALGORITHM:
1. Maintain 2 stacks. Stack1 keeps track of last seen character. Stack2 keeps 
   track of count of consecutive characters. 
2. For every char c in s, if stack1 is empty, append c to stack1 and 1 to stack2
3. else if c is same as last char in stack1, inc count of c in stack2. 
4. Else if c is not same as last char, append c to stack1 and 1 to stack2
5. Pop from stack1 and stack2, if count of last char == k

RUNTIME COMPLEXITY: O(N), where N is length if input string
SPACE COMPLEXITY: O(N), where N is length if input string
'''

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack1, stack2 = [], []
        
        for c in s:
            if stack1 and stack1[-1] == c:
                stack2[-1] += 1
                if stack2[-1] == k:
                    stack1.pop()
                    stack2.pop()
            else:
                stack1.append(c)
                stack2.append(1)

        result = ''
        for i in range(len(stack1)):
            result += stack1[i]*stack2[i]
        return result