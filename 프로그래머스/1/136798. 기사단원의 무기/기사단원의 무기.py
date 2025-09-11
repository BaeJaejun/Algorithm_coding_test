def solution(number, limit, power):
    answer = 0
    yagnum = []
    for i in range(1,number+1):
        yag = 0
        for j in range(1,int(i**(1/2)) +1):
            if i % j == 0 :
                yag += 1
                if j != i // j:  # 제곱근이 아닌 경우 짝 약수도 추가
                    yag += 1
            if yag > limit:
                yag = power
                break
                
        yagnum.append(yag)
    
    answer = sum(yagnum)
    return answer