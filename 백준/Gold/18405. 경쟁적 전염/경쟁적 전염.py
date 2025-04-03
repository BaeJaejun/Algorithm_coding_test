import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

graph = []
graph.append([0 for _ in range(N+1)])
for _ in range(N):
    x = list(map(int,input().split()))
    graph.append([0] + x)
    
S,X,Y = map(int,input().split())


dx = [0,0,-1,1]
dy = [-1,1,0,0] 

visited = [[0 for _ in range(N+1)]for _ in range(N+1)]


q = deque()
for k in range(1,K+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] == k:
                q.append((i,j,k))
                visited[i][j] = k

cnt = 0
while q:
    if cnt == S:
        break
    for _ in range(len(q)):
        x,y,v = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0< nx <= N and 0< ny <= N and visited[nx][ny] == 0:
                visited[nx][ny] = v
                q.append((nx,ny,v))
    cnt += 1



print(visited[X][Y])
