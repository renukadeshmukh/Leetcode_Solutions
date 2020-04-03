'''
885. Spiral Matrix III


'''

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        size = R*C
        step = 0
        dirc = 0
        cnt = 1
        res = [[r0, c0]]
        r,c = r0,c0
        while cnt < size:
            j = 0
            if dirc == 0:
                j = 0
                step += 1
                while j < step:
                    c += 1
                    if c < C:
                        res.append([r, c])
                        cnt += 1
                    j += 1
            elif dirc == 1:
                while j < step:
                    r += 1
                    if r < R:
                        res.append([r, c])
                        cnt += 1
                    j += 1 
            elif dirc == 2:
                step += 1
                while j < step:
                    c -= 1
                    if c >= 0:
                        res.append([r, c])
                        cnt += 1
                    j += 1
            else:
                while j < step:
                    r -= 1
                    if r >= 0:
                        res.append([r, c])
                        cnt += 1
                    j += 1
            dirc = (dirc + 1) % 4
        return res

s = Solution()
#print(s.spiralMatrixIII(1,4, 0,0))
print()
print(s.spiralMatrixIII(5, 6, 1, 4))
print([[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])
        