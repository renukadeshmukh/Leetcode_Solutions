'''
919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly 
the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary 
tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with 
head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value 
node.val = v so that the tree remains complete, and returns the value of the 
parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 
Example 1:
Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]

Example 2:
Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = 
[[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
'''

'''
ALGORITHM:
1. Perform Level Order Traversal and keep all nodes in a queue
2. To insert a node, 
    > Insert the node in queue. Calculate parent of this node using maths. 
    > parent_index = len(queue)-2//2
    > If left of this parent is None, insert left child or insert right child. 
    > Return the parent node
3. To get_root, return the 0th queue element. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N) for n nodes in the tree
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from helpers.binary_tree_helper import BinaryTree
from helpers.binary_tree_helper import TreeNode

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.level_order_traversal = self.level_order_traversal(root)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        if not self.level_order_traversal:
            self.level_order_traversal = [v]
            return
        self.level_order_traversal.append(node)
        parent_index = (len(self.level_order_traversal)-2)//2
        parent = self.level_order_traversal[parent_index]
        if parent.left == None:
            parent.left = node
        else:
            parent.right = node
        return parent
        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        if self.level_order_traversal:
            return self.level_order_traversal[0]
        return None
        
    def level_order_traversal(self, root):
        if not root:
            return []
        traversal = [root]
        i = 0
        while i < len(traversal):
            node = traversal[i]
            if node.left:
                traversal.append(node.left)
            if node.right:
                traversal.append(node.right)
            i += 1
        return traversal 
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

def execute(num, root, inputs, args):
    cbt = None
    for i in range(num):
        if inputs[i] == "CBTInserter":
            cbt = CBTInserter(root)
        elif inputs[i] == "insert":
            parent = cbt.insert(args[i][0])
            print(parent.value)
            root = cbt.get_root()
            tree = BinaryTree.print_binary_tree(root)
            print(tree)
        elif inputs[i] == "get_root":
            root = cbt.get_root()
            tree = BinaryTree.print_binary_tree(root)
            print(tree)

inputs = ["CBTInserter","insert","get_root"]
args = [[[1]],[2],[]]
root = BinaryTree.build_binary_tree(args[0][0])
tree = BinaryTree.print_binary_tree(root)
print(tree)
execute(len(inputs), root, inputs, args)

inputs = ["CBTInserter","insert","insert","get_root"]
args = [[[1,2,3,4,5,6]],[7],[8],[]]
root = BinaryTree.build_binary_tree(args[0][0])
tree = BinaryTree.print_binary_tree(root)
print(tree)
execute(len(inputs), root, inputs, args)
