import sys

input = sys.stdin.readline

M,N,L = map(int,input().split())

Mx = list(map(int,input().split()))

animals = []
for _ in range(N):
    x,y = map(int,input().split())
    animals.append([x,y,False]) # 좌표, 사살 여부


for i in range(M):
    for j in range(N):
        if abs(Mx[i]-animals[j][0]) + animals[j][1]  <= L:
            animals[j][2] = True

cnt = 0
for i in range(N):
    if animals[i][2] == True:
        cnt += 1
        
print(cnt)


