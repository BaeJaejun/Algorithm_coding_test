def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        cntx = 0
        cntelse = 0
        for i,k in enumerate(s):
            if k == x:
                cntx += 1
            else:
                cntelse += 1

            if cntx == cntelse:
                s = s[i+1:]
                answer += 1
                break
                
            if i + 1 == len(s):
                answer += 1
                return answer

            
    return answer