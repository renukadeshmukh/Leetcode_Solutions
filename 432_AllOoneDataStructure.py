'''
432. All O`one Data Structure
'''

class AllOne(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mydict = {}
        self.max_stack = []
        self.min_stack = []
        self.max_value = 0
        self.min_value = 0
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.mydict:
            self.mydict[key] += 1
        else:
            self.mydict[key] = 1
        
        if self.max_value == 0:
            self.max_stack.append(key)
            self.max_value = self.mydict[key]
        elif self.mydict[key] >= self.max_value:


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.mydict:
            self.mydict[key] -= 1
            if self.mydict[key] == 0:
                self.mydict.pop(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()