def solution(keymap, targets):
    answer = []
    
    for target in targets:
        sumx = 0
        for ti in target:
            x = 101
            for key in keymap:
                if x == 1:
                    break
                for i,k in enumerate(key):
                    if k == ti:
                        x = min(x,i + 1)
                        break
            if x == 101: 
                sumx = 10001
                    
            sumx += x
            
        if sumx >= 10001:
            answer.append(-1)
        else:
            answer.append(sumx)
                
    return answer