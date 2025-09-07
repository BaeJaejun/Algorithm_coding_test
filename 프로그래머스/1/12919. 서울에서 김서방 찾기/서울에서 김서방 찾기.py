def solution(seoul):
    x = 0
    for i,k in enumerate(seoul):
        if k == "Kim":
            x = i
            break
    answer = '김서방은 ' + str(x) +'에 있다'
    return answer