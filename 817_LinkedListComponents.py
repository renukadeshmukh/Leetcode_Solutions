'''
817. Linked List Components

You are given the head of a linked list containing unique integer values and an 
integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected 
if they appear consecutively in the linked list.
 

Example 1:
0 -> 1 -> 2 -> 3
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected 
components.

Example 2:
0 -> 1 -> 2 -> 3 -> 4
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] 
are the two connected components.
 
Constraints:
The number of nodes in the linked list is n.
1 <= n <= 104
0 <= Node.val < n
All the values Node.val are unique.
1 <= nums.length <= n
0 <= nums[i] < n
All the values of nums are unique.
'''

'''
ALGORITHM:
1. Add numbers in nums to a set for fast read. 
2. As you iterate over the linkedlist keep track of connected components. 
3. Increment the result when a new component is found. 
4. Return result. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums_set = set(nums)
        cur = head 
        is_continued = False
        
        while cur != None:
            if cur.val in nums_set and is_continued == False:
                is_continued = True
                result += 1
            elif cur.val not in nums_set:
                is_continued = False
            cur = cur.next
        
        return result