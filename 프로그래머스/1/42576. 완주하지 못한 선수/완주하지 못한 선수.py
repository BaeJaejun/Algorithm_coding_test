from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    
    for c in completion:
        dic[c] += 1
    
    for p in participant:
        if dic[p] == 0: 
            return p
        else:
            dic[p] -= 1
