'''
876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

'''
Algorithm:
1. Slow and Fast pointer approach
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) 
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head,head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow if fast.next == None else slow.next

head = ListNode(1)
cur = head
for i in xrange(2,3):
    node = ListNode(i)
    cur.next = node
    cur = cur.next
s = Solution()
print(s.middleNode(head))