'''
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear 
data structure in which the operations are performed based on FIFO (First In First 
Out) principle and the last position is connected back to the first position to 
make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces 
in front of the queue. In a normal queue, once the queue becomes full, we cannot 
insert the next element even if there is a space in front of the queue. But using 
the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
'''

'''
ALGORITHM:
1. Define a node structure with prev and next links
2. Maintain a head with value = '#' to mark the start of circular deque
3. Maintain length of circular deque and k
enQueue(): Insert node between head and head.prev. Update pointers
deQueue(): Insert node between head and head.next. Update pointers
Front(): Return the value of head.next
Rear(): Return the valof head.prev
isEmpty(): Return length_of_circular_deque == 0
isFull(): Return length_of_circular_deque == k

RUNTIME COMPLEXITY AND SPACE COMPLEXITY:
               RUNTIME            SPACE
enQueue():   O(1)        |      O(1)  
deQueue():   O(1)        |      O(1) 
Front():     O(1)        |      O(1) 
Rear():      O(1)        |      O(1)  
isEmpty():   O(1)        |      O(1) 
isFull():    O(1)        |      O(1) 
'''


class CircularDeque:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head = CircularDeque('#')
    
        self.head.next = self.head
        self.head.prev = self.head
        self.len = 0
        self.k = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        tmp = self.head.prev
        curr = CircularDeque(value)
        self.len += 1
        
        self.head.prev = curr
        curr.next = self.head
        curr.prev = tmp
        tmp.next = curr
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.len -= 1
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.next.val
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.prev.val
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.len == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.len == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()