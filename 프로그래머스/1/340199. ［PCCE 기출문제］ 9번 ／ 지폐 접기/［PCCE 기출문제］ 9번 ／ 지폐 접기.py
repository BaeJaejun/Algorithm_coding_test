def solution(wallet, bill):
    answer = 0
          
    x,y = bill
    i,j = wallet
    
    while True:   
        smallb = min(x,y)
        bigb = max(x,y)

        smallw = min(i,j)
        bigw = max(i,j)

        if smallb > smallw or bigb > bigw:
            x = bigb // 2
            y = smallb
            answer += 1
        else:
            break
            
    return answer