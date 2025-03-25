import sys

input = sys.stdin.readline

N = int(input().strip())

circles = []

for _ in range(N):
    x, r =  map(int,input().split())
    l = x-r
    r = x+r 
    circles.append((0, l)) # 0 == 왼쪽
    circles.append((1, r)) # 1 == 오른쪽
    
circles.sort(key= lambda x: (x[1],-x[0]))


stk = []
cnt = 1
for c in circles:
    if c[0] == 0: #왼쪽 좌표
        stk.append(c)
        
    else: # 오른쪽 좌표
        width = 0
        while stk:
            x = stk.pop()
            if x[0] == 0:
                y = c[1] - x[1]
                
                if y == width:
                    cnt += 2
                else:
                    cnt += 1
                stk.append((2,y))
                break
            elif x[0] == 2: # 원이 있을때
                width += x[1]
  

print(cnt)