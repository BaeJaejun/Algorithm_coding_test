import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
graph.append(["0" for _ in range(M+1)])
for i in range(N):
    x = list(input().strip())
    graph.append(['0'] + x)

visited = [[False for _ in range(M+1)]for _ in range(N+1)]


dy = [0,0,-1,1]
dx = [-1,1,0,0]

cnt = 0
def dfs(startx,starty,prev):
    visited[startx][starty] = True
    
    if graph[startx][starty] == "-":
        for i in range(2,4): # -일 땐 좌우로만만
            nx = startx + dx[i]
            ny = starty + dy[i]
            if 0< nx <= N and 0< ny <= M and not visited[nx][ny] and graph[nx][ny] == prev:
                dfs(nx,ny,prev)


    
    elif graph[startx][starty] == "|":
        for i in range(0,2): # | 일땐 상하로만
            nx = startx + dx[i]
            ny = starty + dy[i]
            if 0< nx <= N and 0< ny <= M and not visited[nx][ny] and graph[nx][ny] == prev:
                dfs(nx,ny,prev)

    
for i in range(1,N+1):
    for j in range(1,M+1):
        if not visited[i][j]:
            dfs(i,j,graph[i][j])
            cnt += 1
print(cnt)