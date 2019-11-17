'''
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

'''
ALGORITHM:
Maintain all nodes in a stack along a bool "visited" variable. Initially 
visited is False. Every node is considered visited (visited = True), when
that node's children are added to the stack. 

1. Add [root, False] to stack
2. Peek the stack. Add right and left children of the top node to the stack in 
   right to left order. Mark this node as visited. [node, True]
3. If top node(node on top of stack), does not have any children(leaf node), pop 
   the node and append val to result. 
4. Else if visited = True for the top node, pop node and append val to result. 
5. Return result once stack is empty. 


RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [[root, False]]
        result = []
        while len(stack) > 0:
            top = stack[-1]
            if top[0].left == None and top[0].right == None:
                result.append(top[0].val)
                stack.pop()
            elif top[1] == True:
                result.append(top[0].val)
                stack.pop()
            else:
                top[1] = True
                if top[0].right:
                    stack.append([top[0].right, False])
                if top[0].left:
                    stack.append([top[0].left, False])
        return result 
        
