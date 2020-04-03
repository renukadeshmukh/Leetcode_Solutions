'''
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

'''
ALGORITHM:
1. Perfrom level order traversal and add the 'next' links

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)

'''

class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        q = deque()
        q.extend([root, None])
        while len(q) > 1:
            node = q.popleft()
            if node is None:
                q.append(None)
            else:
                node.next = q[0]
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return root


s = Solution()
s.connect()