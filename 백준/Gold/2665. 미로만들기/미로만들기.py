import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

n = int(input().strip())

# -1 로 인덱스 1부터 시작하게 만들기
miro = [[-1 for _ in range(n+1)]]
for _ in range(n):
    miro.append([-1] + list(map(int,input().strip())))
    
# 0 검은방 // 1 흰 방

# 상 하 좌 우
dx =[0,0,-1,1]
dy =[-1,1,0,0]

def dijk(x,y):
    distance = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    distance[x][y] = 0
    heap = []
    heappush(heap,(0,x,y))
    while heap:
        cost, a,b = heappop(heap)

        if distance[a][b] < cost:
            continue
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 < nx < n+1 and  0 < ny < n+1:
                if miro[nx][ny] == 0:
                    cost1 = 1
                else: cost1 = 0
                new_cost = cost1 + distance[a][b]
                if distance[nx][ny] > new_cost:
                    distance[nx][ny] = new_cost
                    heappush(heap,(new_cost,nx,ny))
     
    return distance               
                    
result = dijk(1,1)

print(result[n][n])