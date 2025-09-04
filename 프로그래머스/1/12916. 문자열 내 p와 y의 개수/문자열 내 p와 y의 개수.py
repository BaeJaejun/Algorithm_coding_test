def solution(s):
    answer = True
    cntp = 0
    cnty = 0
    for i in s:
        if i == 'p' or i == 'P':
            cntp += 1
        elif i == 'y'or i == 'Y':
            cnty += 1
    if cntp != cnty:
        answer = False
    return answer