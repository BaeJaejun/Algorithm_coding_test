def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
        
    x = sorted(answer,reverse=True)
    
    return int(''.join(x))