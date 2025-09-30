def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    re = []
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
            re.append(i)
    
    x = set(lost) - set(re)
            
    for i in list(x):        
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
            
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
        
    return answer