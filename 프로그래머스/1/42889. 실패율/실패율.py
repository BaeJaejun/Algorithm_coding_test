def solution(N, stages):
    answer = []
    notclear = [0] * (N+1)
    result = []
    total = len(stages)
    
    for s in stages:
        if s <= N:
            notclear[s] += 1
            
            
    for i in range(1,N+1):
        if total == 0:
            fail = 0
        else:
            fail = notclear[i] / total
        result.append((i,fail))
        total -= notclear[i]
        
        
    result.sort(key = lambda x : x[1], reverse = True)

    for i,j in result:
        answer.append(i)
    return answer