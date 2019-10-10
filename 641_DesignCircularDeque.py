'''
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
'''

'''
ALGORITHM:
1. Define a node structure with prev and next links
2. Maintain a head with value = '#' to mark the start of circular deque
3. Maintain length of circular deque and k
insertFront(): Insert node between head and head.next. Update pointers
insertLast(): Insert node between head and head.prev. Update pointers
deleteFront(): Delete node between head and head.next. Update pointers
deleteLast(): Delete node between head and head.prev. Update pointers
getFront(): Return the value of head.next
getRear(): Return the valof head.prev
isEmpty(): Return length_of_circular_deque == 0
isFull(): Return length_of_circular_deque == k

RUNTIME COMPLEXITY AND SPACE COMPLEXITY:
               RUNTIME            SPACE
insertFront():  O(1)        |      O(1)  
insertLast():   O(1)        |      O(1) 
deleteFront():  O(1)        |      O(1) 
deleteLast():   O(1)        |      O(1)  
getFront():     O(1)        |      O(1) 
getRear():      O(1)        |      O(1)  
isEmpty():      O(1)        |      O(1) 
isFull():       O(1)        |      O(1) 
'''

class CircularDeque:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.head = CircularDeque('#')
    
        self.head.next = self.head
        self.head.prev = self.head
        self.len = 0
        self.k = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        tmp = self.head.next
        
        curr = CircularDeque(value)
        self.head.next = curr
        curr.prev = self.head
        self.head.next.next = tmp
        tmp.prev = curr
        self.len += 1
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False
        tmp = self.head.prev  
        
        curr = CircularDeque(value)
        self.head.prev = curr
        curr.prev = tmp
        curr.next = self.head
        curr.prev.next = curr
        self.len += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.len -= 1
        return True
        
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.len == 0:
            return False
        self.head.prev = self.head.prev.prev
        self.head.prev.next = self.head
        self.len -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.len == 0:
            return -1
        return self.head.next.val
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.len == 0:
            retutn -1
        return self.head.prev.val
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.len == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.len == self.k

    def printCircularDeque(self):
        curr = self.head.next
        circular_deque = ""
        while curr.val != '#':
            circular_deque += (str(curr.val) + '-->')
            curr = curr.next
        print(circular_deque)


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(10)
param_1 = obj.insertFront(4)
obj.printCircularDeque()
param_1 = obj.insertFront(3)
obj.printCircularDeque()
param_1 = obj.insertFront(2)
obj.printCircularDeque()
param_1 = obj.insertFront(1)
obj.printCircularDeque()
param_2 = obj.insertLast(5)
obj.printCircularDeque()
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()