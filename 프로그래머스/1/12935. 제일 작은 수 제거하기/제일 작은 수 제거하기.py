def solution(arr):
    answer = []
    m = min(arr)
    
    for i in arr:
        if i != m:
            answer.append(i)
            
    if not answer:
        answer.append(-1)
        
    return answer