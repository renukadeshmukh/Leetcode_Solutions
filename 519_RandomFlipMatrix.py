'''
519. Random Flip Matrix

'''

import random
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.matrix,self.r,self.c = [],n_rows, n_cols
        self.end = n_rows*n_cols - 1
        for i in range(n_rows):
            for j in range(n_cols):
                self.matrix.append([i,j])
        print(self.matrix)
        
    def flip(self):
        """
        :rtype: List[int]
        """
        index = random.randint(0,self.end+1)
        result = self.matrix[index]
        self.matrix[index], self.matrix[self.end] = self.matrix[self.end], self.matrix[index]
        print(self.matrix)
        self.end -= 1
        return result

    def reset(self):
        """
        :rtype: void
        """
        self.end = self.r*self.c - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

s = Solution(2,2)
s.flip()
s.flip()
s.flip()
s.flip()