def solution(babbling):
    answer = 0
    canspeak = ['aya','ye','woo','ma']
    
    for j in babbling:
        valid = True
        x = j 
        for i in canspeak:
            if i*2 in x:
                valid = False
                break
        
        if not valid:
            continue
            
        for i in canspeak:
            while i in x:
                    x = x.replace(i,"_"*len(i))
                
        print(x)
        if x == "_"*len(j):
                answer += 1
                
    return answer