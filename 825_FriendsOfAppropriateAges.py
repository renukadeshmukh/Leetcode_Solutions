'''
825. Friends Of Appropriate Ages
'''
from collections import defaultdict
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
        result = 0
        age_dd = defaultdict( int )
        for a in ages:
            age_dd[a] += 1
        age_arr = list(age_dd.keys())
        ln = len(age_arr)
        for i in range(ln-1):
            for j in range(i+1,ln):
                a, b = age_arr[i], age_arr[j]
                if self.a_friend_b(a, b):
                    result += age_dd[a] * age_dd[b]
                if self.a_friend_b(b, a):
                    result += age_dd[a] * age_dd[b]
                    
        for a in age_dd:
            if age_dd[a] > 1:
                result += age_dd[a]
        return result
                           
        
    def a_friend_b(self, a_age, b_age):
        if (b_age <= 0.5 * a_age + 7) or (b_age > a_age):
            return False
        return True
                
s = Solution()
print(s.numFriendRequests([16,16]))
print(s.numFriendRequests([20,30,100,110,120]))
print(s.numFriendRequests([16,17,18]))