'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return head
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = RandomListNode(cur.label)
            cur = cur.next
            cur.next = nxt
            cur = cur.next
        cur = head
        while cur != None:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        cur = head
        head1 = cur.next
        cur1 = head1
        while cur.next.next != None:
            cur.next = cur.next.next
            cur1.next = cur1.next.next
            cur = cur.next
            cur1 = cur1.next
        cur.next = None
           
        return head1

l1 = RandomListNode(-1)
l2 = RandomListNode(2)
l3 = RandomListNode(3)
l4 = RandomListNode(4)
l5 = RandomListNode(5)
l6 = RandomListNode(6)
l7 = RandomListNode(7)
l8 = RandomListNode(8)
l9 = RandomListNode(9)
l10 = RandomListNode(10)

head = l1
'''
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l10
'''
#l1.random = l1
l2.random = l1
l3.random = l1
l4.random = l2
s= Solution()
s.copyRandomList(head)