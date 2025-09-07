def solution(absolutes, signs):
    answer = 0
    for i,k in enumerate(signs):
        if k == False:
            absolutes[i] = absolutes[i] * -1
    
    answer = sum(absolutes)
    return answer