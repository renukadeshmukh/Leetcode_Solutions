'''
1366. Rank Teams by Votes
'''

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        vote_bank = {}
        ln = len(votes[0])
        for vote in votes:
            for i in range(ln):
                if vote[i] not in vote_bank:
                    vote_bank[vote[i]] = [0] * ln
                vote_bank[vote[i]][i] += 1

        scores = [] 
        for team in vote_bank:
            score = 0
            team_votes = vote_bank[team]
            for i in range(ln):
                score += team_votes[i] * (ln-i)
            scores.append([team, score])
        
        scores.sort(key=lambda x: (x[1], x[0]), reverse = True)
        
        return ''.join([x[0] for x in scores])
        
        

s = Solution()
print(s.rankTeams(votes = ["WXYZ","XYZW"]))
print(s.rankTeams(votes = ["ABC","ACB","ABC","ACB","ACB"]))