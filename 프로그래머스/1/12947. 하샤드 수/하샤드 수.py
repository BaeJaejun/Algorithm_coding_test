def solution(x):
    answer = True
    h = str(x)
    sumh = 0
    for i in h:
        sumh += int(i)
    
    if x % sumh != 0:
        answer = False
    return answer