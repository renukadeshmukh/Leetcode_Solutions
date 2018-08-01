'''
874. Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three 
possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still 
continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
'''

'''
TIME COMPLEXITY : O(n)
SPACE COMPLEXITY : O(n)
'''
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dirs = {
            'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3
        }

        y_lookup = {}
        x_lookup = {}
        res = 0

        for o in obstacles:
            if o[0] in x_lookup:
                x_lookup[o[0]].append(o[1])
            else:
                x_lookup[o[0]] = [o[1]]
            
            if o[1] in y_lookup:
                y_lookup[o[1]].append(o[0])
            else:
                y_lookup[o[1]] = [o[0]]
            
        x,y, dir = 0,0,0
        for c in commands:
            if c == -1:
                dir = (dir + 1) % 4
            elif c == -2:
                dir = (dir + 3) % 4
            else:
                if dir == 0:
                    y_arr = None
                    if x in x_lookup:
                        y_arr = [y1 for y1 in x_lookup[x] if y1 > y and y1 <= y+c]
                    if y_arr:
                        y = min(y_arr) - 1
                    else:
                        y += c
                elif dir == 1:
                    x_arr = None
                    if y in y_lookup:
                        x_arr = [x1 for x1 in y_lookup[y] if x1 > x and x1 <= x+c]
                    if x_arr:
                        x = min(x_arr) - 1
                    else:
                        x += c
                elif dir == 2:
                    y_arr = None
                    if x in x_lookup:
                        y_arr = [y1 for y1 in x_lookup[x] if y1 < y and y1 >= y-c]
                    if y_arr:
                        y =  max(y_arr) + 1 
                    else:
                        y -= c
                else:
                    x_arr = None
                    if y in y_lookup:
                        x_arr = [x1 for x1 in y_lookup[y] if x1 < x and x1 >= x-c]
                    if x_arr:
                        x = max(x_arr) + 1
                    else:
                        x -= c
                res = max(res, x*x + y*y)
        return res

s = Solution()
'''
res = s.robotSim([4,-1,3], [])
print(res)

res = s.robotSim([4,-1,4,-2,4], [[2,4]])
print(res)

res = s.robotSim([7,-2,-2,7,5], [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]])
print(res)
'''

res = s.robotSim([1,2,-2,5,-1,-2,-1,8,3,-1,9,4,-2,3,2,4,3,9,2,-1,-1,-2,1,3,-2,4,1,4,-1,1,9,-1,-2,5,-1,5,5,-2,6,6,7,7,2,8,9,-1,7,4,6,9,9,9,-1,5,1,3,3,-1,5,9,7,4,8,-1,-2,1,3,2,9,3,-1,-2,8,8,7,5,-2,6,8,4,6,2,7,2,-1,7,-2,3,3,2,-2,6,9,8,1,-2,-1,1,4,7],
[[-57,-58],[-72,91],[-55,35],[-20,29],[51,70],[-61,88],[-62,99],[52,17],[-75,-32],[91,-22],[54,33],[-45,-59],[47,-48],[53,-98],[-91,83],[81,12],[-34,-90],[-79,-82],[-15,-86],[-24,66],[-35,35],[3,31],[87,93],[2,-19],[87,-93],[24,-10],[84,-53],[86,87],[-88,-18],[-51,89],[96,66],[-77,-94],[-39,-1],[89,51],[-23,-72],[27,24],[53,-80],[52,-33],[32,4],[78,-55],[-25,18],[-23,47],[79,-5],[-23,-22],[14,-25],[-11,69],[63,36],[35,-99],[-24,82],[-29,-98],[-50,-70],[72,95],[80,80],[-68,-40],[65,70],[-92,78],[-45,-63],[1,34],[81,50],[14,91],[-77,-54],[13,-88],[24,37],[-12,59],[-48,-62],[57,-22],[-8,85],[48,71],[12,1],[-20,36],[-32,-14],[39,46],[-41,75],[13,-23],[98,10],[-88,64],[50,37],[-95,-32],[46,-91],[10,79],[-11,43],[-94,98],[79,42],[51,71],[4,-30],[2,74],[4,10],[61,98],[57,98],[46,43],[-16,72],[53,-69],[54,-96],[22,0],[-7,92],[-69,80],[68,-73],[-24,-92],[-21,82],[32,-1],[-6,16],[15,-29],[70,-66],[-85,80],[50,-3],[6,13],[-30,-98],[-30,59],[-67,40],[17,72],[79,82],[89,-100],[2,79],[-95,-46],[17,68],[-46,81],[-5,-57],[7,58],[-42,68],[19,-95],[-17,-76],[81,-86],[79,78],[-82,-67],[6,0],[35,-16],[98,83],[-81,100],[-11,46],[-21,-38],[-30,-41],[86,18],[-68,6],[80,75],[-96,-44],[-19,66],[21,84],[-56,-64],[39,-15],[0,45],[-81,-54],[-66,-93],[-4,2],[-42,-67],[-15,-33],[1,-32],[-74,-24],[7,18],[-62,84],[19,61],[39,79],[60,-98],[-76,45],[58,-98],[33,26],[-74,-95],[22,30],[-68,-62],[-59,4],[-62,35],[-78,80],[-82,54],[-42,81],[56,-15],[32,-19],[34,93],[57,-100],[-1,-87],[68,-26],[18,86],[-55,-19],[-68,-99],[-9,47],[24,94],[92,97],[5,67],[97,-71],[63,-57],[-52,-14],[-86,-78],[-17,92],[-61,-83],[-84,-10],[20,13],[-68,-47],[7,28],[66,89],[-41,-17],[-14,-46],[-72,-91],[4,52],[-17,-59],[-85,-46],[-94,-23],[-48,-3],[-64,-37],[2,26],[76,88],[-8,-46],[-19,-68]])
print(res)
                
