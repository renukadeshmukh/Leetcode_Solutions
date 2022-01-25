'''
1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. 

Note that:
The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot 
never leaves the circle. 

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: 
(0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not 
go into cycles.
Based on that, we return false.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (
0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.
 
Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
'''

'''
RUNTIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)

ALGORITHM:
1. Iterate over the input instruction and keep track of x,y co-ordinates and 
   direction of robot.
2. If the robot comes back to origin the answer is true.
3. If the robot is facing NORTH direction the answer is always false since we 
   are drifting away from origin.
4. If the robot is facing any direction except north the answer will be true 
   since it will loop and come back to origin. 

'''

class Solution(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        '''
        0 = 'North',
        1 : 'East',
        2 : 'South',
        3 : 'West'
        '''
        
        curDirection = 0
        for c in instructions:
            if c == 'R':
                curDirection = (curDirection + 1) % 4
            elif c == 'L':
                curDirection = (curDirection - 1) % 4
            else:
                if curDirection == 0 :
                    self.y += 1
                elif curDirection == 2 :
                    self.y -= 1
                elif curDirection == 1:
                    self.x += 1
                elif curDirection == 3:
                    self.x -= 1
        
        if self.x == self.y == 0:
            return True 
        elif curDirection != 0:
            return True
        return False

