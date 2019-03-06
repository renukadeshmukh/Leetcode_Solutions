'''
508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. 
The subtree sum of a node is defined as the sum of all the node values formed by 
the subtree rooted at that node (including the node itself). So what is the most 
frequent subtree sum value? If there is a tie, return all the values with the 
highest frequency in any order.

Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in 
any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit 
signed integer.
'''

'''
ALGORITHM:
1. Sum every subtree and store the frequency of every sum in a dictionary
    <sum-value>:<frequency>
2. Invery the dictionary. <frequency>:<list of sum-value>
3. Return the value associated with the max frequency

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: (N)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        dic = defaultdict(int)
        self.findFrequentTreeSumHelper(root,dic)
        rev_dict = self.invert_dict(dic)
        return rev_dict[max(rev_dict)]
                                
    def invert_dict(self, dic):
        rev_dict = defaultdict(list)
        for key in dic:
            rev_dict[dic[key]].append(key)
        return rev_dict
        
    def findFrequentTreeSumHelper(self, root, dic):
        if root.left == None and root.right == None:
            dic[root.val] += 1
            return root.val
        else:
            left,right=0,0
            if root.left != None:
                left = self.findFrequentTreeSumHelper(root.left, dic)
            if root.right != None:
                right = self.findFrequentTreeSumHelper(root.right, dic)
            sm = left + right + root.val
            dic[sm] += 1
            return sm

