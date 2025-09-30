def solution(ingredient):
    answer = 0
    result = []
    for i  in ingredient:
        result.append(i)
        
        if len(result) >= 4 and result[-4:] == [1,2,3,1]:
            for i in range(4):
                result.pop()
            answer += 1
    return answer