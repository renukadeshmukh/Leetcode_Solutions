'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

'''
ALGORITHM:
1. San the 2 lists and convert them into numbers num1 and num2
2. Add num1 and num2
3. Convert the sum into a linkedlist and return the Head.

TIME COMPLEXITY: O(N), where N is the length of the bigger linked-list  
SPACE COMPLEXITY: O(1)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        while l1 != None or l2 != None:
            sm = 0
            if l1:
                num1 = num1*10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2*10 + l2.val
                l2 = l2.next
                
        sm = num1 + num2
        if sm == 0:
            return ListNode(0)
        nxt = None
        while sm > 0:
            node = ListNode(sm%10)
            sm = sm/10
            node.next = nxt
            nxt = node
        return node
                
            
        
