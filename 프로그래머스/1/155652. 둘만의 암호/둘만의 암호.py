def solution(s, skip, index):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    skipa = []
    for j in skip:
        skipa.append(alpha.index(j))

    for i in s:
        ind = alpha.index(i)
        for _ in range(index):
            ind += 1
            if ind == 26:
                ind = 0
                
            while ind in skipa:
                ind += 1
                if ind == 26:
                    ind = 0
        answer += alpha[ind]
            
            
    return answer