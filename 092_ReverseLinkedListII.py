'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 <= m <= n <= length of list.
Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

'''
RUNTIME COMPLEXITY : O(n)
SPACE COMPLEXITY : (1)
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printLinkedList(self, head):
        cur = head
        while cur != None:
            print(cur.val, '-->>')
            cur = cur.next

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cnt = 1
        cur1 = head
        prev1 = None
        while cnt < m:
            prev1 = cur1
            cur1 = cur1.next
            cnt += 1
        cur = cur1
        prev = None
        tmp = cur1
        while cur != None and cnt <= n:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            cnt += 1
        if prev1:
            prev1.next = prev
        else:
            head = prev
        tmp.next = nxt
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

head = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
#s.printLinkedList(head)
head = s.reverseBetween(head,1,5)
s.printLinkedList(head)