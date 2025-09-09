def solution(s):
    x = list(s.split(' '))
    answer = ''
    for i in x:
        for j,k in enumerate(i):
            if j % 2 == 0:
                answer += k.upper()
            else:
                answer += k.lower()
        answer += ' '
    return answer[:-1]