'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x. You should preserve the original 
relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

'''
ALGORITHM:
1. Maintain two queues, the first one stores all nodes with val less than x , 
   and the second queue stores all the rest nodes. 
2. Then concat these two queues. 
3. Remember to set the next of second queue a null next, to avoid infinite loop.
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
from helpers import linked_list_helper

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
 
        lower, higher = ListNode('#'), ListNode('#')
        cur1, cur2 = lower, higher

        cur = head
        while cur != None:
            nxt = cur.next
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = nxt
        cur2.next = None
        cur1.next = higher.next
        return lower.next

input = [1,4,3,2,5,2]
head = linked_list_helper.LinkedList.array_to_linkedlist(input)

s = Solution()
h = s.partition(head, 3)
linked_list_helper.LinkedList.printLinkedList(head)

input = [2,1]
head = linked_list_helper.LinkedList.array_to_linkedlist(input)
head = s.partition(head, 2)
linked_list_helper.LinkedList.printLinkedList(head)
