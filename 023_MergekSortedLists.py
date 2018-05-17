# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
from pip._vendor.requests.api import head
from collections import deque

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Merge 2 lists at a time to reduce the merging time to logarithmic value. 
    Merge 2 lists and append the output in a queue. Keep doing this till queue size = 1
    '''
    def merge(self, l1, l2):
        
        res = ListNode(-1)
        cur = res
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 == None:
            cur.next = l2
        elif l2 == None:
            cur.next = l1
        
        return res.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return []
        q = deque()
        q.extend(lists)
        while len(q) > 1:
            l1 = q.popleft()
            l2 = q.popleft()
            h = self.merge(l1, l2)
            q.append(h)
            
        return q[0]
            
    
h1 = ListNode(1)
h1.next = ListNode(4)
h1.next.next = ListNode(5)

h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)

h3 = ListNode(2)
h3.next = ListNode(6)

s = Solution()
s.mergeKLists([h1, h2, h3])