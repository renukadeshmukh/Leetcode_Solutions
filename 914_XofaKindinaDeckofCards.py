'''
914. X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
'''

'''
ALGORITHM:
1. Count occurance of each integer and save in a dictionary card_dic.
2. Find GCD of all the elements in card_dic.values()
3. if gcd >= 2, return True else return False

TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
'''
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        card_dic = {}
        
        for i in deck:
            if i not in card_dic:
                card_dic[i] = 0
            card_dic[i] += 1

        count_arr = card_dic.values()
        min_cnt = min(count_arr)
    
        gcd = self.gcd(count_arr)
        if gcd >= 2:
            return True
        return False
                
    def gcd(self, array):
        gcd = 1
        for i in range(2,min_cnt+1):
            flag = True
            for val in array:
                if val % i != 0:
                    flag = False
                    break
            if flag:
                gcd = i
        return gcd
