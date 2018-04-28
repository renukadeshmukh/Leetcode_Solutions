'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
Note:
Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
#class TreeNode(object):
#        def __init__(self, x):
#            self.val = x
#            self.left = None
#            self.right = None

from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool    
        """
        
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        else:
            return self.isSymmetricRecursive(root.left, root.right)
        
    def isSymmetricRecursive(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        elif root1.val != root2.val:
            return False
        else:
            return self.isSymmetricRecursive(root1.left, root2.right) and self.isSymmetricRecursive(root1.right, root2.left) 
    
    def isSymmetricIterative(self, root):
        
        if root == None:
            return True
        
        q = deque()
        q.extend([root,'#'])
        
        temp = []
        result = False
        while True:
            if len(q) == 1:
                result = True
                break
            node = q.popleft()
            
            if node == None:
                temp.append(None)
                continue
            if node == '#':
                q.append('#')
                print temp
                if not self.checkSymmetry(temp):
                    return False
                temp = []
            else:
                temp.append(node.val)
                q.extend([node.left, node.right])
        return result
        
        
    def checkSymmetry(self, arr):
        i, j = (0, len(arr)-1)
        print arr
        while i <= j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
  


        