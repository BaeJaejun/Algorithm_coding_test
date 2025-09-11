def solution(dots):
    answer = 0
    for i in range(4):
        a = dots[i][:]
        for j in range(4):
            if(j == i):
                continue
            b = dots[j][:]
            for k in range(4):
                if(k== j or k==i):
                    continue
                c = dots[k][:]
                d = dots[6-k-j-i][:]
            
                if((a[1]-b[1])/(a[0]-b[0]) == (c[1]-d[1])/(c[0]-d[0])):
                    answer =1
        
    return answer