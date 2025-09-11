def solution(strings, n):
    answer = []
    tmp = []
    for i in strings:
        i = i[n: n+1] + i
        tmp.append(i)
    
    
    tmp.sort()
    
    for i in tmp:
        answer.append(i[1:])
    return answer