'''
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that 
player makes a move consisting of:
Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.

Also, if a player cannot make a move, they lose the game.
Return True if and only if Alice wins the game, assuming both players play 
optimally.

Example 1:
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 
Note:
1 <= N <= 1000
'''

'''
ALGORITHM:
1. Anyone who gets 1 definitely loses since not exist a x in range of (0, 1)
2. Anyone who gets 2 definitely wins since he always/or only can make 2 become 1. 
   Because x can only be 1, 2 % 1 == 0 and 2 - 1 = 1
3. For any N >= 2, N will definitely be reduced to 2

The one who gets even number `N` has the choice to get all the even numbers 
including 2(since 2 is even), so here comes win.

So if N is even initially,
1. What is Alice's optimal strategy?
choose x = 1, N = N - 1
2. What is Bob's optimal strategy?
Choose x as large as possible to make N reduce fast such that the pain can end 
as early as possible

From above, we know that if Alice meets even N, she will win. We just need to 
check if N is divisble by 2.

RUNTIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N%2 == 0


 