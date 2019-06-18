'''
147. Insertion Sort List

Sort a linked list using insertion sort.
'''

'''
ALGORITHM:
1. Insertion sort iterates, consuming one input element each repetition, and 
growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

RUNTIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(1)
'''

from helpers import linked_list_helper

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        cur = head.next
        prev = head
        
        while cur != None:
            if cur.val < prev.val:
                #put cur at correct place
                next = cur.next
                if cur.val < head.val:
                    cur.next = head
                    head = cur
                    cur = next
                    prev.next = cur
                else:
                    cur1 = head
                    while cur1.next.val < cur.val:
                        cur1 = cur1.next
                    cur.next = cur1.next
                    cur1.next = cur
                    cur = next
                    prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return head
                
s = Solution()

arr = [1,2,3,4]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
head = s.insertionSortList(head)
linked_list_helper.LinkedList.printLinkedList(head)

arr = [4, 1]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
head = s.insertionSortList(head)
linked_list_helper.LinkedList.printLinkedList(head)

arr = [4,2,1,3]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
head = s.insertionSortList(head)
linked_list_helper.LinkedList.printLinkedList(head)

arr = [1,1]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
head = s.insertionSortList(head)
linked_list_helper.LinkedList.printLinkedList(head)