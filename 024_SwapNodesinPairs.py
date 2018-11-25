'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

'''
ALGORITHM:
Similar to normal node swapping using temp variable. 
However catch here is to also keep track of nxt and prev nodes so that correct
nodes can be pointed to and maintained after swapping. 
The prev should point to second node after swapping to be able to further follow
Nxt should point to first node after swapping to be able to further follow cur.next

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        cur = head
        prev = None
        head = cur.next
        while cur != None and cur.next != None:
            nxt = cur.next
            tmp = nxt.next
            nxt.next = cur
            cur.next = tmp
            
            cur = tmp
            if prev==None:
                prev = head.next
            else:
                prev.next = nxt
                prev = nxt.next
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
h1 = generate_linkedlist([1,2,3])
head = s.swapPairs(h1)
print_linkedlist(head)