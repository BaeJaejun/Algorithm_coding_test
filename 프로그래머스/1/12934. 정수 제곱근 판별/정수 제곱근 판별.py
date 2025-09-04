def solution(n):
    answer = 0
    x = 1
    while(True):
        if x * x == n:
            answer = (x+1) * (x+1)
            break
        if x * x > n:
            return -1
        
        x = x + 1
    return answer