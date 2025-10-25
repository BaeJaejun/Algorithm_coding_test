def solution(players, callings):
    answer = []
    rank = {}
    
    for i in range(len(players)):
        rank[players[i]] = i

    for c in callings:
        i = rank[c]
        if i != 0:
            players[i], players[i-1] = players[i-1], players[i] 
            
            rank[players[i]] = i
            rank[players[i-1]] = i - 1
            
    return players