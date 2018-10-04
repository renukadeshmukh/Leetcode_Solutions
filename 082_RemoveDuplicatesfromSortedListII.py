'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers 
from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

'''
ALGORITHM:
1. Iterate on the list and keep track of prev, cur and next
2. While cur == next, delete all next and then delete current
3. Move prev, cur and next ahead. 

RUNTIME COMPLEXITY: (N)
SPACE COMPLEXITY: O(1)
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev,cur,next = None, head, head.next
        
        while nxt != None:
            if cur.val == nxt.val:
                while nxt and cur.val == nxt.val:
                    cur.next = cur.next.next
                    nxt = cur.next
                if prev:
                    prev.next = cur.next
                else:
                    head = nxt
                if not nxt:
                    break
                cur = nxt
                nxt = cur.next
            else:
                prev = cur
                cur = nxt
                nxt = cur.next

        return head

def generate_linkedlist(nums):
    head = ListNode(nums[0])
    cur = head
    for n in nums[1:]:
        node = ListNode(n)
        cur.next = node
        cur = cur.next
    return head

def print_linkedlist(head):
    cur = head
    while cur != None:
        print(cur.val, '-->')
        cur = cur.next


s = Solution()
h1 = generate_linkedlist([1,2,3,3,4,4,5])
head = s.deleteDuplicates(h1)
print_linkedlist(head)
print()
h2 = generate_linkedlist([1, 1,5 ])
head = s.deleteDuplicates(h2)
print_linkedlist(head)
print()
h3 = generate_linkedlist([1,1, 2,2,3,3,4, 5 ])
head = s.deleteDuplicates(h3)
print_linkedlist(head)
print()
h3 = generate_linkedlist([1,1, 2,2,3,3,4,4,5, 5 ])
head = s.deleteDuplicates(h3)
print_linkedlist(head)
