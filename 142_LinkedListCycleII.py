'''
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no 
cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which 
represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the 
second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the 
first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
'''

'''
ALGORITHM:
1. Traverse linked list using two pointers - fast and slow.
2. Move one pointer by one and other pointer by two.  
3. If these pointers meet at same node then there is a loop.  
   If pointers do not meet then linked list doesn’t have loop.
4. If a loop is found, initialize slow pointer to head, let fast pointer be at 
   its position.
5. Move both slow and fast pointers one node at a time.
6. The point at which they meet is the start of the loop.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        is_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
        if is_cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None