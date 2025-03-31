import sys
from collections import deque

input = sys.stdin.readline

#가로,세로,높이
M,N,H = map(int,input().split())

visited = [[[-1 for _ in range(M)]for _ in range(N)] for _ in range(H)]

box = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        x = list(map(int,input().split()))
        box[i].append(x)
        

# 상 하 좌 우 위 아래
dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,1,-1]



q = deque()    
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i,j,k))
                visited[i][j][k] = 0
    
while q:
    c,b,a = q.popleft()
    for i in range(6):
        nx = a + dx[i]
        ny = b + dy[i]
        nz = c + dz[i]
        if  0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0  and visited[nz][ny][nx] == -1:
            q.append((nz,ny,nx))
            visited[nz][ny][nx] = visited[c][b][a] + 1
            box[nz][ny][nx] = 1


def check_result():
    result = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    result = -1
                    return result    
                result = max(result,visited[i][j][k])    
    return result

print(check_result())