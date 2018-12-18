'''
946. Validate Stack Sequences

Given two sequences pushed and popped with distinct values, return true if and 
only if this could have been the result of a sequence of push and pop operations 
on an initially empty stack.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Note:
0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
'''

'''
ALGORITHM:
1. Initialize i and j to iterate over pushed and popped. 
   initialize a stack(array) and visited(set) 
2. i < len(pushed) and j < len(popped) 
3. if popped[j] is visited 
    check if popped[j] is top of the stack
        if yes then pop from stack and inc j
    else you can pop a visited element that is not at top of stack. Return False
4.  push element from 'pushed' array onto stack
    Add this element to visited list and inc i
5. After while loop completes, if stack is empty return True else return False.

RUNTIME COMPLEXITY: O(M+N) where M and N are length if imputs
SPACE COMPLEXITY: O(N) where N is length of pushed elements
'''

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        visited = set()
        stack = []
        i,j = -1,0
        while :
            if popped[j] in visited:
                if stack[-1] != popped[j]:
                    return False
                else:
                    j += 1
                    stack.pop()
            else:
                i += 1
                stack.append(pushed[i])
                visited.add(pushed[i])
                
                
        if len(stack) == 0:
            return True
        return False
                
s = Solution()
print(s.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))