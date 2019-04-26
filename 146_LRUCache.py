'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It 
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists 
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


'''
ALGORITHM:
The problem can be solved with a hashtable that keeps track of the keys and its 
values in the double linked list. One interesting property about double linked 
list is that the node can remove itself without other reference. In addition, it 
takes constant time to add and remove nodes from the head or tail.

Implement pseudo head and tail to mark the boundary, so that we don't need to 
check the NULL node during the update. This makes the code more concise and 
clean, and also it is good for the performance as well.

RUNTIME COMPLEXITY:
    get(): O(1)
    set(): O(1)
SPACE COMPLEXITY:
    O(N) for hashmap and O(N) for doubly linked list
'''
class DLLNode(object):
    def __init__(self, key, value=None ):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self):
        self.head = DLLNode(key='@') # head
        self.tail = DLLNode(key='$') # tail

    def appned_node_at_front(self, key, value):
        node = DLLNode(key, value)
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
        return node

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def array_to_dll_test(self, arr):
        for i in arr:
            self.appned_node_at_front(i,i, self.head)
        

    def print_dll_test(self):
        cur = self.head
        while cur != self.tail:
            print(cur.prev, cur.value, cur,next)
            cur = cur.next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.lru_hashmap = {}
        self.dll = DLL()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru_hashmap:
            return -1
        node = self.lru_hashmap[key]
        value = node.value
        self.dll.delete_node(node)
        node = self.dll.appned_node_at_front(key, value)
        self.lru_hashmap[key] = node
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lru_hashmap:
            node = self.lru_hashmap[key]
            self.dll.delete_node(node)
        elif len(self.lru_hashmap) >= self.size:
            # pop last element
            least_recently_used_node = self.dll.tail.prev
            self.dll.delete_node(least_recently_used_node)
            del self.lru_hashmap[least_recently_used_node.key]
        # append at front
        node = self.dll.appned_node_at_front(key, value)
        self.lru_hashmap[key] = node
           

                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache( 2 )

cache.put(1, 1);
cache.put(2, 2);
print(cache.get(1));       # returns 1
cache.put(3, 3);    # evicts key 2
print(cache.get(2));       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
print(cache.get(1));       # returns -1 (not found)
print(cache.get(3));       # returns 3
print(cache.get(4));       # returns 4