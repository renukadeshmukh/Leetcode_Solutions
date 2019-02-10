'''
725. Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the 
linked list into k consecutive linked list "parts". The length of each part 
should be as equal as possible: no two parts should have a size differing by 
more than 1. This may lead to some parts being null. The parts should be in 
order of occurrence in the input list, and parts occurring earlier should always 
have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, 
\root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode 
is [].

Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
'''

'''
ALGORITHM
1. Convert linked list to array
2. Find how many elements to insert in each part. 
3. Insert the elements in each part accordingly.
4. Return result 

RUNTIME COMPLEXITY: O(N*k) where n is length of linked list
SPACE COMPLEITY = O(N) where n is length of linked list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from helpers import linked_list_helper

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        

        stk = self._linked_list_to_arr(root)
        ln = len(stk)
        result,i = [],0
        
        for j in range(k):
            x,r = divmod(ln, k)
            if r:
                x += 1
            ln -= x
            k -= 1
            
            temp = []
            for l in range(x):
                temp.append(stk[i])
                i += 1
            result.append(temp)
        return result       
    
    def _linked_list_to_arr(self, head):
        cur = head
        stk = []
        while cur != None:
            stk.append(cur.val)
            cur = cur.next
        return st
        
s = Solution()

head = linked_list_helper.LinkedList.array_to_linkedlist([1,2,3,4])
print(s.splitListToParts(head, 5))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = linked_list_helper.LinkedList.array_to_linkedlist(arr)
print(s.splitListToParts(head, 3))
