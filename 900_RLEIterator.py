'''
900. RLE Iterator

Write an iterator that iterates through a run-length encoded sequence.
The iterator is initialized by RLEIterator(int[] A), where A is a run-length 
encoding of some sequence.  More specifically, for all even i, A[i] tells us the 
number of times that the non-negative integer value A[i+1] is repeated in the 
sequence.

The iterator supports one function: next(int n), which exhausts the next n 
elements (n >= 1) and returns the last element exhausted in this way.  If there 
is no element left to exhaust, next returns -1 instead.

For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of 
the sequence [8,8,8,5,5].  This is because the sequence can be read as "three 
eights, zero nines, two fives".
'''

'''
ALGORITHM:
Exhaust first n elements and return the next value. 
All even indices are counts of elements. 
If current indice does not have enough count, exhast it and move to the next
element i += 2 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

class RLEIterator(object):
    
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.iter = 0
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.iter < len(self.A) and self.A[self.iter] - n < 0 :
            n -= self.A[self.iter]
            self.iter += 2

        if self.iter < len(self.A):
            self.A[self.iter] -= n
            return self.A[self.iter + 1]
        else:
            return -1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

