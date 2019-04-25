'''
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on 
day i. If you were only permitted to complete at most one transaction (i.e., buy 
one and sell one share of the stock), design an algorithm to find the maximum 
profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: 
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

'''
ALGORITHM:
1. Keep track of lowest stock price so far, minp
2. Keep updating res with max of current result and cur_price - minp
3. If cur_price is less than minp, update minp

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''

from sys import maxint
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        minp = maxint
        for p in prices:
            if p < minp:
                minp = p
            else:
                r = p - minp
                res = max(res, p - minp)
        return res
