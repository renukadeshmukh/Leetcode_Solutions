'''
61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from helpers import linked_list_helper

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
ALGORITHM:
1. Calculate length of linked list
2. Rotate the linked list 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) ; fot stack
'''

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        if k == 0:
            return head
        
        ln = 0
        p1 = head
        stk = []
        #calculate length of linked list
        while p1 != None:
            stk.append(p1)
            p1 = p1.next
            ln+=1
        rotations = k%ln
        if rotations == 0:
            return head 
        #rotate the linked list
        h1, end, i = None, None, ln-1
        while rotations > 0:
            if h1 == None:
                h1 = stk[i]
                end = h1
            else:
                stk[i].next = h1
                h1 = stk[i]
            i -= 1
            rotations -= 1
        while i >= 0:
            if end.next == None:
                end.next = stk[i]
                end.next.next = None
            else:
                nxt = end.next
                end.next = stk[i]
                end.next.next = nxt
            i -= 1
        return h1
        
        

s = Solution()    
     
head = linked_list_helper.LinkedList.array_to_linkedlist([1,2,3,4,5])
head = s.rotateRight(head, 2)
linked_list_helper.LinkedList.printLinkedList(head)
print()
head = linked_list_helper.LinkedList.array_to_linkedlist([1,2,3])
head = s.rotateRight(head, 4)
linked_list_helper.LinkedList.printLinkedList(head)

print()
head = linked_list_helper.LinkedList.array_to_linkedlist([1,2])
head = s.rotateRight(head, 2)
linked_list_helper.LinkedList.printLinkedList(head)