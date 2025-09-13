def solution(brown, yellow):
    answer = []
    
    yy = []
    for i in range(1,int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            yy.append((i,yellow//i))
    
    for a,b in yy:
        if (a+b) * 2 + 4 == brown:
            answer.append(max(a,b) + 2)
            answer.append(min(a,b) + 2)
    return answer