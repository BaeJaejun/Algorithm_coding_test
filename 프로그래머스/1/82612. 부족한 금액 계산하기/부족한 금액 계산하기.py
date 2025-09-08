def solution(price, money, count):
    answer = -1
    p = 0
    for i in range(1, count+1):
        p += i * price
    
    if money >= p:
        answer = 0
    else:
        answer = p - money
    
    return answer