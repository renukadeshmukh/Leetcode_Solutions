'''
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
ALGORITHM:
1. Iterate on the linkedlist and save the values in a list
2. Check if the list is a palindrome.
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)

BETTER ALGORITHM:
1. Using fast and slow pointer approach reverse the first half of the list
2. Compare the two halves to have the same values
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst1 = []
        
        cur = head
        while cur != None:
            lst1.append(cur.val)
            cur = cur.next
        i,j = 0, len(lst1)-1
        while i < j:
            #print(i,j)
            if lst1[i] != lst1[j]:
                return False
            i, j = i+1, j-1
        return True