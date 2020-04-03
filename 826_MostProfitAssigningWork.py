'''
826. Most Profit Assigning Work
'''

class Profit(object):
    def __init__(self, d, p):
        self.difficulty = d
        self.profit = p
        

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        store = []
        for i in range(len(profit)):
            store.append(Profit(difficulty[i], profit[i]))
        store.sort(key=lambda x: x.profit)
        
        total_profit = 0
        for w in worker:
            for i in range(len(profit)-1, -1, -1):
                if store[i].difficulty <= w:
                    total_profit += store[i].profit
                    break
        return total_profit

s = Solution()
print(s.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))