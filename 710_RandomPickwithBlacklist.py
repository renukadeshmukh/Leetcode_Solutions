'''
710. Random Pick with Blacklist

Given a blacklist B containing unique integers from [0, N), write a function to 
return a uniform random integer from [0, N) which is NOT in B.
Optimize it such that it minimizes the call to system’s Math.random().

Note:
1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.

Example 1:
Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:
Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:
Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:
Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's 
constructor has two arguments, N and the blacklist B. pick has no arguments. 
Arguments are always wrapped with a list, even if there aren't any.
'''

'''
ALGORITHM:
1. Keep track of few non-black listed elements in "store". 
2. For pick(), pick a random number from 1 to N. If this number is blacklisted,
   then return a random number from store. Else return N.

RUNTIME COMPLEXITY: 
        __init__ : O(N)
        pick()   : O(1)
SPACE COMPLEXITY:
        __init__ : O(N)
        pick()   : O(1)
'''

from random import randint

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self._N = N
        self._blacklist = set(blacklist)
        i = 0
        store = []
        while i <= len(blacklist) and i < N:
            if i not in self._blacklist:
                store.append(i)
            i += 1
        self.store = store

    def pick(self):
        """
        :rtype: int
        """
        n = randint(0, self._N-1)
        if n in self._blacklist:
            return self.store[n%len(self.store)]
        return n
        


# Your Solution object will be instantiated and called as such:
obj = Solution(5, [2,1,0])
print obj._dict
for i in xrange(10):
    print(obj.pick())