

def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    answer = [0, 0]
    i = 0
    while i < len(toss):
        heads, tails = 0, 0
        while i < len(toss) and toss[i] == 'Heads':
            heads += 1
            i += 1
        answer[0] = max(answer[0], heads)
        
        while i < len(toss) and toss[i] == 'Tails':
            tails += 1
            i += 1
        answer[1] = max(answer[1], tails)
        print answer

getMaxStreaks(['Heads', 'Tails', 'Tails', 'Tails', 'Heads', 'Heads', 'Tails'])