def solution(a, b):
    answer = 0
    if a > b : 
        big = a
        small = b
    else:
        big = b
        small = a
    for i in range(small,big+1):
        answer = answer + i 
    return answer