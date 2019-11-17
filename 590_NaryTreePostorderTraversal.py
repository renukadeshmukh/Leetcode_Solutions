'''
590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).
 
Follow up:
Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Explanation: Representation of 3-ary tree.

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 
Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
'''

'''
ALGORITHM:
Maintain all nodes in a stack along a bool "visited" variable. Initially 
visited is False. Every node is considered visited (visited = True), when
that node's children are added to the stack. 

1. Add [root, False] to stack
2. Peek the stack. Add all children of the top node to the stack in right to left
   order. Mark this node as visited. [node, True]
3. If top node(node on top of stack), does not have any children(leaf node), pop 
   the node and append val to result. 
4. Else if visited = True for the top node, pop node and append val to result. 
5. Return result once stack is empty. 

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [[root,False]]
        result = []
        while len(stack) > 0:
            node = stack[-1]
            if node[0].children == None or node[1] == True:
                result.append(node[0].val)
                stack.pop()
            else:
                node[1] = True
                children = node[0].children
                for i in range(len(children)-1, -1, -1):
                    stack.append([children[i], False])
        return result 
