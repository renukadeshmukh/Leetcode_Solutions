
'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''

'''
ALGORITHM:
1. Calculate length of both linkedlists
2. Move head ahead for longer linkedlist, so that both are same length.
3. Run a loop comparing the 2 linkedlist till you find the mergeed node

TIME COMPLEXITY:O(N)
SPACE COMPLEXITY:O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lng1 = self.get_length(headA)
        lng2 = self.get_length(headB)
        
        if lng1 > lng2:
            headA = self.move_head(lng1 - lng2, headA)
        else:
            headB = self.move_head(lng2-lng1, headB)

        while(headA != None):
            if headA == headB:
                break
            headA = headA.next
            headB = headB.next
        
        return headA
            
    def move_head(self, distance, head):
        while distance>0:
            head = head.next
            distance -= 1
        return head
            
        
    def get_length(self, head):
        lng = 0
        while head != None:
            lng += 1
            head=head.next
        return lng