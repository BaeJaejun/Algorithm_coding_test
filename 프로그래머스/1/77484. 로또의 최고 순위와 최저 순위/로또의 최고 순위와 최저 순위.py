def solution(lottos, win_nums):
    answer = []
    
    x = 0
    cnt = 0
    for i in lottos:
        if i in win_nums:
            x += 1   
        if i == 0:
            cnt +=1
    
    if x == 6:
        answer.append(1)
    elif x == 5:
        answer.append(2)
    elif x == 4:
        answer.append(3)
    elif x == 3:
        answer.append(4)
    elif x == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if cnt == 6:
        answer.append(answer[0] - cnt + 1)   
    else:
        answer.append(answer[0] - cnt)   
    
    answer.sort()
    return answer