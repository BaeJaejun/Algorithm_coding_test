import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

miro = [[] for _ in range(N)]

for i in range(N):
    x = input().strip()
    for a in x:
        miro[i].append(int(a))
    
#    상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[0]* M for _ in range(N)]


def bfs(x,y):
    visited[x][y] = 1
    q = deque([(x,y)])
    while q:
        a,b= q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visited[nx][ny] == 0:
               q.append((nx,ny))
               visited[nx][ny] = visited[a][b] +1


bfs(0,0)
print(visited[N-1][M-1])