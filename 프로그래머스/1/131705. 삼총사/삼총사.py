def solution(number):
    answer = 0
    x = len(number)
    for i in range(0,x-2):
        for j in range(i+1,x-1):
            for k in range(j+1,x):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer