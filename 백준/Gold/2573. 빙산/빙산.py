import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
        

#    상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def next_year():
    temp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            coor = graph[i][j]
            if coor != 0:
                cnt_zero = 0
                for a,b in zip(dx,dy):
                    nx = a + i
                    ny = b + j
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        cnt_zero += 1
                if coor - cnt_zero <= 0:
                    temp[i][j] = 0  
                else:
                    temp[i][j] = graph[i][j] - cnt_zero
    return temp
    
def bfs(x,y):
   
    visited[x][y] = 50  #방문처리 50으로 해주자
    q = deque([(x,y)])
    while q:
        u,v = q.popleft()
        for i in range(4):
            nx = u + dx[i]
            ny = v + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 50 and graph[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = 50
                
                
year = 0                
while True:
    visited = [[0] * M for _ in range(N)]

    seom_cnt = 0
    for i in range(N):
            for j in range(M):
                if graph[i][j] != 0 and visited[i][j] != 50:
                    bfs(i,j)
                    seom_cnt += 1
    
    if sum(map(sum,graph)) == 0:
        print(0)
        break
    if seom_cnt != 1:
        print(year)
        break
    
    
    graph = next_year()
    year += 1

