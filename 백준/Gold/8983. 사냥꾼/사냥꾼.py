import sys
from bisect import bisect_left
input = sys.stdin.readline

M,N,L = map(int,input().split())

Mx = list(map(int,input().split()))
Mx.sort()
animals = []
for _ in range(N):
    x,y = map(int,input().split())
    animals.append([x,y,False]) # 좌표, 사살 여부

# 60점짜리 코드
# for i in range(M):
#     for j in range(N): 
#         if abs(Mx[i]-animals[j][0]) + animals[j][1]  <= L and animals[j][2] == False:
#             animals[j][2] = True

# cnt = 0
# for i in range(N):
#     if animals[i][2] == True:
#         cnt += 1
        
# print(cnt)

animals.sort()

for i in range(N): #동물을 기준으로 사대에서 이진탐색. 가까운 사대가 못죽이면 못죽여
    x, y = animals[i][0], animals[i][1]

    if y > L:
        continue
    
    closed_Mx = bisect_left(Mx,x)    #가장 가까운 사대의 x좌표
    
    if closed_Mx < M and (abs(Mx[closed_Mx] - x) + y) <= L: # 우측 사대 or 동물/사대 같은 위치
        animals[i][2] = True
    elif closed_Mx > 0  and (abs(Mx[closed_Mx - 1] - x) + y) <= L: # 좌측 사대
        animals[i][2] = True

cnt = 0
for i in range(N):
    if animals[i][2] == True:
        cnt += 1
print(cnt)