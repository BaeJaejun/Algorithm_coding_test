def solution(dartResult):
    answer = 0
    result = [0,0,0]
    
    i = -1
    for k in dartResult:
        if k.isdigit():   
            if result[i] != 0 and result[i] == 1 and k == '0':
                result[i] = result[i] * 10 + int(k)
            else:
                i += 1
                result[i] = int(k)

        if k == 'S':
            result[i] = result[i]
        if k == 'D':
            result[i] = result[i]**2
        if k == 'T':
            result[i] = result[i]**3

        if k == "*":
            result[i] = result[i] * 2
            if i > 0:
                result[i-1] = result[i-1] * 2
        if k == "#":
            result[i] = result[i] * -1

    answer = sum(result)
    return answer