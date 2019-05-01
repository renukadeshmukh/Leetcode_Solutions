'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

ALGORITHM:
Use the Hare and Tortoise approach. 
1. The fast pointer(hare) umpts 2 nodes but the slow pointer(tortoise) jumps one node at a time. 
2. If fast pointer become null, then no loop.
3. Else if fast == slow, then loop detected.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        isCyclic = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                isCyclic = True
                break

        return isCyclic


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)


node1.next = node
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node6

s = Solution()
print(s.hasCycle(node1))