'''
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity 
and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was 
in the input.
The first node is considered odd, the second node even and so on ...
'''

'''
ALGORITHM:
1. Maintain odd and even nodes 
2. Append the head of even nodes to end of off nodes.

RUNTIME COMPLEXITY: O(N), where N is the number of nodes
SPACE COMPLEXITY: O(1)
'''

from helpers import linked_list_helper

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head2 = head.next
        
        cur, cur1 = head, head2
        
        while cur1 and cur1.next:
            cur.next = cur.next.next
            cur1.next = cur1.next.next
            cur = cur.next
            cur1 = cur1.next
        cur.next = head2
        return head1

arr = [1,2,3,4,5]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
head = Solution().oddEvenList(head)
