def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        x = i**(1/2)
        if x == int(x):
            answer -= i
        else:
            answer += i
    return answer