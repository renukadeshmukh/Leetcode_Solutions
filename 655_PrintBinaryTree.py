#from idlelib.TreeWidget import TreeNode


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        print(self.max_depth_tree(root))
        
    def max_depth_tree(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return max(1 + self.max_depth_tree(root.left) + 1, self.max_depth_tree(root.right) + 1)
        
s = Solution()
t = TreeNode("1", None, None)
t.left = TreeNode("2", None, None)

s.printTree(t)