def solution(n):
    answer = 0
    three = ''
    while True:
        if n < 3:
            three = three + str(n)
            break
        three = three + str(n % 3)
        n = n // 3
    
    x = len(three) - 1
    
    for i in three:
        answer += int(i) * (3**x)
        x -= 1
        
    return answer