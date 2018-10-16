'''
707. Design Linked List

Design your implementation of the linked list. You can choose to use the singly 
linked list or the doubly linked list. A node in a singly linked list should have 
two attributes: val and next. val is the value of the current node, and next is 
a pointer/reference to the next node. If you want to use the doubly linked list, 
you will need one more attribute prev to indicate the previous node in the linked 
list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

>get(index) : Get the value of the index-th node in the linked list. If the index 
is invalid, return -1.
>addAtHead(val) : Add a node of value val before the first element of the linked 
list. After the insertion, the new node will be the first node of the linked list.
>addAtTail(val) : Append a node of value val to the last element of the linked list.
>addAtIndex(index, val) : Add a node of value val before the index-th node in the 
linked list. If index equals to the length of linked list, the node will be appended 
to the end of linked list. If index is greater than the length, the node will not 
be inserted.
>deleteAtIndex(index) : Delete the index-th node in the linked list, if the index 
is valid.

Example:
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.

'''

'''
1. addAtHead
    RUNTIME COMPLEXITY: O(1)
    SPACE COMPLEXITY: O(1)
2. addAtTail
    RUNTIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)
3. addAtIndex
    RUNTIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)
4. get
    RUNTIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)
5. deleteAtIndex
    RUNTIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)
'''

from helpers import linked_list_helper
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        while cur and index>0:
            cur = cur.next
            index -= 1
        if cur:
            return cur.val
        else:
            return -1
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, 
        the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the 
        length of linked list, the node will be appended to the end of linked list. If index is greater 
        than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)

        cur, node = self.head, ListNode(val)
        i = 1
        while cur and i != index:
            cur = cur.next
            i += 1
        if cur:
            nxt = cur.next
            cur.next = node
            cur = cur.next
            cur.next = nxt

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.head
        if cur == None:
            return
        elif index == 0:
            self.head = cur.next

        cur, i = self.head, 1
        while cur and i != index:
            cur = cur.next
            i += 1
        if cur.next == None:
            cur = None
        else:
            cur.next = cur.next.next

        

linkedList =  MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  # linked list becomes 1->2->3
linkedList.addAtIndex(0, -1); # linked list becomes 1->2->3
linkedList.addAtIndex(5, 5);  # linked list becomes 1->2->3
linkedList.addAtIndex(4, 4);  # linked list becomes 1->2->3
print(linkedList.get(5));     # returns 2
linkedList.deleteAtIndex(1);  # now the linked list is 1->3
linkedList.get(1);            # returns 3
linked_list_helper.LinkedList.printLinkedList(linkedList.head)
