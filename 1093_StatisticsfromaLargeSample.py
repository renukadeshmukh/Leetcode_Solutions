'''
1093. Statistics from a Large Sample

We sampled integers between 0 and 255, and stored the results in an array count:  
count[k] is the number of integers we sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, 
as an array of floating point numbers.  The mode is guaranteed to be unique.

(Recall that the median of a sample is:
The middle element, if the elements of the sample were sorted and the number of 
elements is odd;
The average of the middle two elements, if the elements of the sample were sorted 
and the number of elements is even.) 

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Example 2:

Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
 

Constraints:
count.length == 256
1 <= sum(count) <= 10^9
The mode of the sample that count represents is unique.
Answers within 10^-5 of the true value will be accepted as correct.
'''

'''
ALGORITHM:
1. For max element, find the last non-zero count in the array
2. For min element, find the first non-zero count in the array
3. For average, sum all numbers and divide by total sample size
4. For median, find the middle elements of the array. 
5. For mode, find the largest count in the array and return its index. 

RUNTIME COMPLEXITY: O(256)
SPACE COMPLEXITY: O(256)
'''


class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        sample = []
        total = 0
        cnt = 0
        mode, mode_cnt = 0, 0
        for i in range(256):
            if count[i]:
                sample.append([i, count[i]])
                total += count[i] * i
                cnt += count[i]
                if count[i] > mode_cnt:
                    mode, mode_cnt = i, count[i]
                
        min_x, max_x = sample[0][0], sample[-1][0]
        median = self.get_median(sample, cnt)
        return [float(min_x), float(max_x), float(total)/cnt, float(median), float(mode)]      
    
    def get_median(self, sample, cnt):
        mid1 = cnt/2 
        mid2 = cnt/2 + 1
        median = 0
        if cnt %2 == 0:
            #something
            #mid -= 1
            i,j = 0,0
            x, y = 0, 0
            for s in sample:
                i,j = i + s[1], j + s[1]
                if not x and  i >= mid1:
                    x = s[0]
                if not y and j >= mid2:
                    y = s[0]
                if x and y:
                    median = float(x+y)/2
                    break
        else:
            #something
            i = 0
            for s in sample:
                i += s[1]
                if i >= mid1:
                    median = s[0]
                    break
        return median
        
s = Solution()
print(s.sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))