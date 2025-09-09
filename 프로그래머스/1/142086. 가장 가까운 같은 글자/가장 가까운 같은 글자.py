def solution(s):
    answer = []
    dict = {}
    for i,k in enumerate(s):
        if k not in dict:
            dict[k] = i
            answer.append(-1)
        else:
            answer.append(i - dict[k])
            dict[k] = i
    return answer