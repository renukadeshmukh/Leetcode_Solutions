'''
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

'''
ALGORITHM:
1. If number greater than equal 1 billion, get the hundreds repreasentation for the part that is greater than one billion
2. Similarly for the million and thousand part. 

RUNTIME COMPLEXITY: O(N) -> where n is length of number
SPACE COMPLEXITY: O(N)
'''
class Solution(object):

    def __init__(self):
        self.units_words = {
            0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",
            10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",
            100:"Hundred", 1000:"Thousand", 1000000:"Million", 1000000000:"Billion"
            }
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """    
        res = []
        #Billion component
        if num >= 1000000000:
            q = num/1000000000
            num = num%1000000000
            self.hundredToWords(q, res)
            res.append(self.units_words[1000000000])
        #Million component
        if num >= 1000000:
            q = num/1000000
            num = num%1000000
            self.hundredToWords(q, res)
            res.append(self.units_words[1000000])
        #Thousand component
        if num >= 1000:
            q = num/1000
            num = num%1000
            self.hundredToWords(q, res)
            res.append(self.units_words[1000])
        #Hundred component
        if num:
            self.hundredToWords(num, res)
        print(' '.join(res))
        
    def hundredToWords(self, num, res):
        h = num/100
        num = num%100
        if h:
            res.extend([self.units_words[h], self.units_words[100]])
        if num and num in self.units_words:
            res.append(self.units_words[num])
        else:
            u = num%10
            num = num - u
            if num:
                res.append(self.units_words[num])
            if u:
                res.append(self.units_words[u])


s = Solution()
s.numberToWords(100)
s.numberToWords(123)
s.numberToWords(12345)
s.numberToWords(1234567)
s.numberToWords(1234567891)
s.numberToWords(1000000000)
