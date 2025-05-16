import sys

input = sys.stdin.readline

M, n = map(int,input().split())
cmd = list()
num = list()
for _ in range(n):
    a,b = input().split()
    cmd.append(a)
    num.append(int(b))
    
    #오 아래 왼 위 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ddir = 0
x,y = 0,0

valid = 1

for i in range(n):
    if cmd[i] == 'MOVE':
        mx = x + (dx[ddir] * num[i])
        my = y + (dy[ddir] * num[i])
        if 0 <= mx <= M and 0 <= my <= M:
            x = mx
            y = my
        else:
            valid = 0
            break
    else: # TURN
        if num[i] == 0: #좌 90 회전
            ddir = (ddir + 3) % 4
        else: # 우 90 회전
            ddir = (ddir + 1) % 4
        
        
if valid == 1:
    print(f"{x} {y}")
else: 
    print(-1)