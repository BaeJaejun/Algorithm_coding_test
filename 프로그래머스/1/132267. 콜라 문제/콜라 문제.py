def solution(a, b, n):
    answer = 0
    
    while n >= a:
        x = n // a
        n = n + (b-a) * x
        answer += x * b
    return answer