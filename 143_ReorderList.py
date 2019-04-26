'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

'''
ALGORITHM:
1. Insert all nodes in a list then append in required format. 
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)

BETTER ALGORITHM:
1. Splits linkedlist in two halves, the first half is >= in size than the second.
   Using the fast and slow pointer approach. 
2. Reverse the second half of list in place.
3. Merge the two lists in place
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

from helpers.linked_list_helper import LinkedList

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head

        cur = head
        list_arr = []
        while cur != None:
            list_arr.append(cur)
            cur = cur.next
            list_arr[-1].next = None
        
        i,j = 0, len(list_arr) - 1
        cur = ListNode(-1)
        head = cur
        while i < j:
            cur.next = list_arr[i]
            cur = cur.next
            cur.next = list_arr[j]
            cur = cur.next
            i ,j = i+1, j-1
        if i == j:
            cur.next = list_arr[i]
        return head.next

s = Solution()
head = LinkedList.array_to_linkedlist([1,2,3,4])
head = s.reorderList(head)
LinkedList.printLinkedList(head)
head = LinkedList.array_to_linkedlist([1,2,3,4,5])
head = s.reorderList(head)
LinkedList.printLinkedList(head)
head = LinkedList.array_to_linkedlist([1,2])
head = s.reorderList(head)
LinkedList.printLinkedList(head)
head = LinkedList.array_to_linkedlist([1])
head = s.reorderList(head)
LinkedList.printLinkedList(head)
