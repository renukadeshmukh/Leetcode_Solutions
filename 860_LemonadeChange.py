'''
860. Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue 
to buy from you, and order one at a time (in the order specified by bills). Each 
customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
You must provide the correct change to each customer, so that the net transaction 
is that the customer pays $5. Return true if and only if you can provide every 
customer with correct change.

Note that you don't have any change in hand at first.

Example 1:
Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: [5,5,10]
Output: true

Example 3:
Input: [10,10]
Output: false

Example 4:
Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
 
Note:

0 <= bills.length <= 10000
bills[i] will be either 5, 10, or 20.
'''

'''
ALGORITHM:
1. Initially, we start with no five dollar bills, and no ten dollar bills.
2. If a customer brings a $5 bill, then we take it.
3. If a customer brings a $10 bill, we must return a five dollar bill. If we 
don't have a $5 bill, the answer is False, since we can't make correct change.
4. If a customer brings a $20 bill, we must return $15.
   4.1 If we have a $10 and a $5, then we always prefer giving change in that
   4.2 Otherwise, if we have three $5 bills, then we'll give that.
   4.3 Otherwise, we won't be able to give $15 in change, and the answer is False.

RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        fives, tens = 0, 0
        result = True
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives:
                tens += 1
                fives -= 1
            elif bill == 20 and fives and tens:
                tens -= 1
                fives -= 1
            elif bill == 20 and fives >= 3:
                fives -= 3
            else:
                result = False
                break
            
        return result