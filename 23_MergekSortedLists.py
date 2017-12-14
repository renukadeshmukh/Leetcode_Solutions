# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
from pip._vendor.requests.api import head
class Solution(object):
    
    head = None
    end = None
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        x = 0
        while x < k:
            min_n = sys.maxint
            which_lst = -1
            for i in range(k):
                if lists[i] != None and lists[i].val < min_n:
                    which_lst = i
            self.appendToResult(min_n)
            lists[which_lst] = lists[which_lst].next
            if lists[which_lst] == None:
                x += 1
            
    def appendToResult(self, val):   
        if self.head == None:
            head = ListNode(val)
            end = head
        else :
            end.next = ListNode(val)
            end = end.next
            
        